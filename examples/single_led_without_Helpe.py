import is31fl3733

driver = is31fl3733.IS31FL3733()
pixels.brightness = 1.0 # range: 0-1.0

driver.set_pwm_pixel(0, 0xff, 0xff, 0xff) # White
driver.set_pwm_pixel(0, 0xff, 0, 0)       # Red
driver.set_pwm_pixel(0, 0, 0xff, 0)       # Green
driver.set_pwm_pixel(0, 0, 0, 0xff)       # Blue

driver.update_pwm_pixels()
