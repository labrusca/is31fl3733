# is31fl3733 LED driver
It's a helper of IS31FL3733 LED driver for CircuitPython.


## Dependencies

This driver depends on:

* `Adafruit  CircuitPython Pixelbuf <https://github.com/adafruit/Adafruit_CircuitPython_Pixelbuf>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.




## Usage Example

```
import is31fl3733
from adafruit_led_animation.animation.blink import Blink
import adafruit_led_animation.color as color

pixels = is31fl3733.Helper(63, byteorder="RGB")
pixels.brightness = 0.9 # range: 0-1.0

blink = Blink(pixels, 0.5, color.PURPLE)

while True:
    blink.animate()
```

## Contributors

- [mfranck](https://github.com/y4m-y4m)

and me ;P