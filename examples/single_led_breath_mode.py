import is31fl3733

led_num = 64
pixels = is31fl3733.Helper(led_num)

# set breath mode
pixels.driver.breathing_enable_mode = is31fl3733.LED_MODE_ABM2
#  breath mode colour: Blue
pixels.driver.set_abm_pixel(63, [0,0,0xFF]) 

while True:
    pixels.driver.update_abm_pixels()