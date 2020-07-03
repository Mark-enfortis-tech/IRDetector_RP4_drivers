from gpiozero import Button
import time


class IR_detector_gpio:

    def __init__(self, gpio_pin):
        self.input_pin = gpio_pin
        self.input = Button(self.input_pin)

    def is_present(self):
        if self.input.is_active:
            return True
        else:
            return False


if __name__ == '__main__':
    gpio = IR_detector_gpio(2)

    while True:
        if gpio.is_present():
            print('object is present')
        else:
            print('object is not present')

        time.sleep(1)
