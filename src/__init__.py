import smbus

# I2C1で初期化
i2c = smbus.SMBus(1)

class pcf8575ts:
    def __init__(self, addr):
        self.addr = addr
    
    def write(self, data):
        i2c.write_byte_data(self.addr, data & 0xFF, data >> 8)