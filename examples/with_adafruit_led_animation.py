import is31fl3733
from adafruit_led_animation.animation.blink import Blink
import adafruit_led_animation.color as color

led_num = 64
pixels = is31fl3733.Helper(led_num, byteorder="RGB")
pixels.brightness = 0.9 # range: 0-1.0

blink = Blink(pixels, 0.5, color.PURPLE)

while True:
    blink.animate()