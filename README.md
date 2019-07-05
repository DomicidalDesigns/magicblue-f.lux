![magicblue-f.lux](./magicblue-flux.png)

A simple python program that uses Bleak to sync your monitor's color temperature (controlled by f.lux) to your magic blue smart bulb.
Made possible thanks to Uri Shaked for reverse engineering the magicblue smartbulb
(https://medium.com/@urish/reverse-engineering-a-bluetooth-lightbulb-56580fcb7546)
# Before you start
You will need a bluetooth 4.0 usb adapter, windows 10 / Linux, a magic blue smartbulb, f.lux, Python 3.x, and Bleak.
## Bleak [https://github.com/hbldh/bleak]
Documentation: https://bleak.readthedocs.io.
* Supports Windows 10, version 16299 (Fall Creators Update) or greater
* Supports Linux distributions with BlueZ >= 5.43
* Plans on macOS support via Core Bluetooth API (see develop branch for progress)

>Bleak supports reading, writing and getting notifications from GATT servers, as well as a function for discovering BLE devices.
Bleak is a GATT client software, capable of connecting to BLE devices acting as GATT servers. It is designed to provide a asynchronous, cross-platform Python API to connect and communicate with e.g. sensors.
### Bleak Installation
In your favorite terminal:
```
$ pip install bleak
```

## Other info
The Color temperature to RGB conversion was performed using this algorithm: http://www.tannerhelland.com/4435/convert-temperature-rgb-algorithm-code/

## Directions
[Just get f.lux](https://justgetflux.com/)

*(well actually there's a little more than that lol)*

* Open the magicblue-f.lux directory in a terminal of your choosing and run:
```
$ python httpserver.py
```
* In f.lux, set the POST URL to the local address for this server (http://127.0.0.1:8001 by default).
The color temp and brightness from f.lux will be logged in flux.txt.

* Finally, run this command in another terminal
```
$ python magicblue-flux.py
```
## Todo
* make it look good
* rewrite this mess of a code
* cry, a lot
## Troubleshooting
* sorry
