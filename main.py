def on_button_pressed_b():
    pins.digital_write_pin(DigitalPin.P10, 0)
    pins.digital_write_pin(DigitalPin.P11, 0)
    pins.digital_write_pin(DigitalPin.P12, 0)
    basic.pause(500)
    pins.digital_write_pin(DigitalPin.P10, 1)
    pins.digital_write_pin(DigitalPin.P11, 1)
    pins.digital_write_pin(DigitalPin.P12, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

lcd_text = ""
lcd_text2 = ""
tinkercademy.crash_sensor_setup(DigitalPin.P13)
pins.digital_read_pin(DigitalPin.P0)
I2C_LCD1602.show_string(lcd_text, 0, 0)

def on_forever():
    global lcd_text
    global lcd_text2
    if input.button_is_pressed(Button.A):
        pins.digital_write_pin(DigitalPin.P14, 1)
    else:
        pins.digital_write_pin(DigitalPin.P14, 0)
    if tinkercademy.crash_sensor():
        if len(lcd_text) < 16:
            I2C_LCD1602.lcd_init(39)
            lcd_text = "" + lcd_text + "."
            I2C_LCD1602.show_string(lcd_text, 0, 0)
            led.plot(3, 3)
        elif len(lcd_text2) < 16:
            I2C_LCD1602.lcd_init(39)
            lcd_text = "" + lcd_text + "."
            I2C_LCD1602.show_string(lcd_text, 0, 0)
            ###########################
            led.plot(3, 3)
        else:
            lcd_text = 'ESPACE'
            lcd_text2 = 'INSUFFISANT'
    else:
        led.unplot(3, 3)
basic.forever(on_forever)
