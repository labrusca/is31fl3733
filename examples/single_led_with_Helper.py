import is31fl3733

led_num = 64
pixels = is31fl3733.Helper(led_num, byteorder="RGB")
pixels.brightness = 1.0 # range: 0-1.0

pixels[0] = (0xff, 0xff, 0xff) # White
pixels[1] = (0xff, 0, 0)       # Red
pixels[2] = (0, 0xff, 0)       # Green
pixels[3] = (0, 0, 0xff)       # Blue

pixels.show()
