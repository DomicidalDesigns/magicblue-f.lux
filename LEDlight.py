import re
import asyncio
import time
from bleak import BleakClient
from CT2RGB import CT2RGB

temperature=1200
offset=1000 #This makes the bulb color temp less than the monitor color temp by this much (more Red; do not exceed 1199)

f=open("flux.txt", "r")

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

    address = "LED BULB MAC ADDRESS GOES HERE"
    Color_Char_UUID = "0000ffe9-0000-1000-8000-00805f9b34fb" #This varies for different smart bulbs
    color_hex=CT2RGB(temperature) # A function that converts color temp to hexadecimal RGB
    
    #bleak stuff
    async def run(address, loop):
        async with BleakClient(address, loop=loop) as client:
            #convert hexadecimal to bytes and send to the bulb over bluetooth
            await client.write_gatt_char(Color_Char_UUID,bytes.fromhex('56'+color_hex+'fff0aa'),False) 

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(address, loop))
    #prints the bulb's current color temperature
    print("Current CT:",str(temperature)+'K')
    
    # Waiting helps with connecting to the bulb for some reason
    time.sleep(20)
