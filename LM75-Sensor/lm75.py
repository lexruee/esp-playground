import ustruct

class LM75:
    """
    A basic I2C driver implementation for the LM75 temperature sensor.
    """
    I2C_ADDR = 0x48

    REG_TMP = 0x00
    REG_CONF = 0x01
    REG_THYST = 0x02
    REG_TOS = 0x03

    def __init__(self, addr=I2C_ADDR, i2c=None, **kwargs):
        if i2c is None:
            raise ValueError('An I2C object is required.')

        self.addr = addr
        self.i2c = i2c

    def read_temperature(self):
        bytes = self.i2c.readfrom_mem(self.addr, self.REG_TMP, 2)
        msb, lsb = ustruct.unpack(">bB", bytes)
        temp = msb + 0.5 * (lsb >> 7)
        return temp