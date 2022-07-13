import is31fl3733

driver = is31fl3733.IS31FL3733()
driver.brightness = 255 # driver.brightness's range: 0-255

driver.set_pwm_pixel(0, 0xff, 0xff, 0xff) # White
driver.set_pwm_pixel(0, 0xff, 0, 0)       # Red
driver.set_pwm_pixel(0, 0, 0xff, 0)       # Green
driver.set_pwm_pixel(0, 0, 0, 0xff)       # Blue

while True:
    driver.update_pwm_pixels()
