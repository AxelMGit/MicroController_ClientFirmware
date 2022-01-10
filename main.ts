input.onButtonPressed(Button.B, function on_button_pressed_b() {
    pins.digitalWritePin(DigitalPin.P10, 0)
    pins.digitalWritePin(DigitalPin.P11, 0)
    pins.digitalWritePin(DigitalPin.P12, 0)
    basic.pause(500)
    pins.digitalWritePin(DigitalPin.P10, 1)
    pins.digitalWritePin(DigitalPin.P11, 1)
    pins.digitalWritePin(DigitalPin.P12, 1)
})
let lcd_text = ""
tinkercademy.crashSensorSetup(DigitalPin.P13)
pins.digitalReadPin(DigitalPin.P0)
I2C_LCD1602.ShowString(lcd_text, 0, 0)
basic.forever(function on_forever() {
    
    if (input.buttonIsPressed(Button.A)) {
        pins.digitalWritePin(DigitalPin.P14, 1)
    } else {
        pins.digitalWritePin(DigitalPin.P14, 0)
    }
    
    if (tinkercademy.crashSensor()) {
        I2C_LCD1602.LcdInit(39)
        lcd_text = "" + lcd_text + "."
        I2C_LCD1602.ShowString(lcd_text, 0, 0)
        //  ##########################
        led.plot(3, 3)
    } else {
        led.unplot(3, 3)
    }
    
})
