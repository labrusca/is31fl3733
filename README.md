# is31fl3733 LED driver
It's a helper of IS31FL3733 LED driver for **CircuitPython**.


## Dependencies

This driver depends on:

* [Adafruit  CircuitPython Pixelbuf](https://github.com/adafruit/Adafruit_CircuitPython_Pixelbuf)

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
[the Adafruit library and driver bundle](https://circuitpython.org/libraries)
or individual libraries can be installed using
[circup](https://github.com/adafruit/circup).




## Usage Example

**Single LED:**

```
import is31fl3733

led_num = 64
pixels = is31fl3733.Helper(led_num)
pixels.brightness = 1.0 # range: 0-1.0

pixels[0] = (0xff, 0xff, 0xff) # White
pixels[1] = (0xff, 0, 0)       # Red
pixels[2] = (0, 0xff, 0)       # Green
pixels[3] = (0, 0, 0xff)       # Blue

while True:
    pixels.show()
```

**Use with adafruit_led_animation:**

```
import is31fl3733
from adafruit_led_animation.animation.blink import Blink
import adafruit_led_animation.color as color

led_num = 64
pixels = is31fl3733.Helper(led_num)
pixels.brightness = 0.9 # range: 0-1.0

blink = Blink(pixels, 0.5, color.PURPLE)

while True:
    blink.animate()
```

Other examples: **[here](https://github.com/labrusca/is31fl3733_driver/tree/main/examples)**

**Test on [M60 keyboard](https://circuitpython.org/board/makerdiary_m60_keyboard/)**

## Contributors

- [mfranck](https://github.com/y4m-y4m)

and me ;p