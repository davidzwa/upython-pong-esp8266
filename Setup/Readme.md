## Setup 
(https://bigl.es/tooling-tuesday-wemos-d1-mini-micropython/)

- Step 1: install pip (python 3)
- Step 2: install esptool 
- Step 3: wipe the flash (change the port accordingly, for me it was COM5)
Linux:
> esptool.py --port /dev/ttyUSB0 erase_flash
Windows:
> python -m esptool --port COM5 erase_flash
- Step 4: install the firmware (change the port accordingly, for me it was COM5)
Linux:
> esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash -fm dio --flash_size=detect 0 esp8266-20191220-v1.12.bin
Windows:
> python -m esptool --port COM5 --baud 460800 write_flash -fm dio --flash_size=detect 0 esp8266-20191220-v1.12.bin

- Step 5: run uPyCraft.exe (or look up Linux install online, or apt install?)
- Step 6: run example code from workspace by running `blink.py` by pressing F5 once that file is opened.
