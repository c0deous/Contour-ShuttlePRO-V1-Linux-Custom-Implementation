import os, sys
from evdev import InputDevice, categorize, ecodes

deviceloc = '/dev/input/by-id/usb-Contour_Design_ShuttlePRO-event-if00'

def readloop(device):
    global lastwheelaction
    lastwheelaction = 0
    device = InputDevice(device)
    for event in device.read_loop():
      # Lower Buttons
      if event.code == 265 and event.value == 1:
          print('Lower TL Pressed')
      elif event.code == 267 and event.value == 1:
          print('Lower BL Pressed')
      elif event.code == 268 and event.value == 1:
          print('Lower BR Pressed')
      elif event.code == 266 and event.value == 1:
          print('Lower TR Pressed')
      # Wheel Control
      elif event.code == 7:
          if lastwheelaction != event.value:
              print('Main wheel: ' + str(event.value))
              lastwheelaction = event.value
      elif event.code == 8:
          print('Outer wheel: ' + str(event.value))
      # Mid Buttons
      elif event.code == 260 and event.value == 1:
          print('Mid 1 Pressed')
      elif event.code == 261 and event.value == 1:
          print('Mid 2 Pressed')
      elif event.code == 262 and event.value == 1:
          print('Mid 3 Pressed')
      elif event.code == 263 and event.value == 1:
          print('Mid 4 Pressed')
      elif event.code == 264 and event.value == 1:
          print('Mid 5 Pressed')
      # Upper Buttons
      elif event.code == 256 and event.value == 1:
          print('Upper 1 Pressed')
      elif event.code == 257 and event.value == 1:
          print('Upper 2 Pressed')
      elif event.code == 258 and event.value == 1:
          print('Upper 3 Pressed')
      elif event.code == 259 and event.value == 1:
          print('Upper 4 Pressed')


if __name__ == '__main__':
    try:
        readloop(deviceloc)
    except OSError:
        print('[-] Root permissions required to access device on ' + deviceloc)
    except KeyboardInterrupt:
        print('Quitting..')
        quit()
