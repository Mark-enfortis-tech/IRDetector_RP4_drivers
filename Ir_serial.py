import time
import serial


class IrSerial:
    rx_buffer = []

    def __init__(self, baudrate):
        # self.ser = serial.Serial('/dev/ttyAMA0', baudrate=baudrate)    # RP4 device
        self.ser = serial.Serial('/dev/cu.usbserial-AB0JNXOO', baudrate=baudrate, timeout=2.0)  # Macbook device

    def isOpen(self):
        return self.ser.isOpen()

    def close(self):
        self.ser.close()

    def read(self):
        try:
            self.rx_buffer = self.ser.read(size=50)
            print('rx_buffer %s' % self.rx_buffer)

        except KeyboardInterrupt:
            print('leaving program')

        except:
            print('Error occured, exit reading')


if __name__ == '__main__':
    ser = IrSerial(9600)
    print('is port open? %s' % ser.isOpen())

    ser.read()

    print('closing port')
    ser.close()

    #print()
