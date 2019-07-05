import re
import asyncio
import time
from bleak import BleakClient
import math

def main():
    temperature=1200
    offset=1199

    f=open("flux.txt", "r")
    #print(f.read())

    # Loop this
    while True:
        f1=list(f.readlines())
        line=len(f1)-1
        while line > 0:
            line=len(f1)-1
            print(line)
            if '?ct=' in f1[line]:
                s=f1[line]
                result = re.search('/?ct=(.*)&bri=', s)
                temperature=int(result.group(1))-offset
                print("Monitor Temperature:",str(temperature+offset)+"K")
                break
            else:
                line-=1

        address = "98:7B:F3:68:00:6B"
        Color_Char_UUID = "0000ffe9-0000-1000-8000-00805f9b34fb"
        color_hex=CT2RGB(temperature)
        white='ff'
        whiteMode=False
        identifier="f0aa"
        if whiteMode:
            identifier="0faa"
        try:
            async def run(address, loop):
                async with BleakClient(address, loop=loop) as client:
                    await client.write_gatt_char(Color_Char_UUID,bytes.fromhex('56'+color_hex+white+identifier),False)

            loop = asyncio.get_event_loop()
            loop.run_until_complete(run(address, loop))
        except:
            continue
        print("Current Color Temp:",str(temperature)+'K')
        print("RGB:",color_hex)
        time.sleep(20)

def CT2RGB(temperature):
    # note: I noticed the blue LED was much brighter than the red and green LEDs
    # To fix this, I reduced the intensity of the blue light
    blue_a=55 #adjustment value for blue amount function
    #blue_a=138.5177312231 #default value
    blue_b=120 # adjustment value for blue light function
    #blue_b=305.0447927307 #default value
    maxBlue=100 # The maximum blue RGB value
    #maxBlue=255 #default value

    temperature=temperature/100
    #Calculate red
    if temperature <= 66:
        red = 255
    else:
        red = temperature - 60
        red = 329.698727446 * (red ** -0.1332047592)
        red=255
        if red < 0:
            red = 0
        if red > 255:
            red = 255
    #Calculate green:
    if temperature <= 66 :
        green = temperature
        green = (99.4708025861 * math.log(green)) - 161.1195681661
        if green < 0:
            green = 0
        if green > 255:
            green = 255
    else:
        green = temperature - 60
        green = 288.1221695283 * (green ** -0.0755148492)
        if green < 0:
            green = 0
        if green > 255:
            green = 255
    #Calculate blue
    if temperature >= 66:
        blue = maxBlue
    else:
        if temperature <= 19:
            blue = 0
        else:
            blue = temperature - 10
            blue = (blue_a * math.log(blue)) - blue_b
            if blue < 0:
                blue = 0
            if blue > maxBlue:
                blue = maxBlue
    return '%02x%02x%02x' %(int(red),int(green),int(blue))

main()
