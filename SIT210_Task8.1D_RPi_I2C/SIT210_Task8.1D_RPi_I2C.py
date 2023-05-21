
import smbus
import time

ADDRESS = 0x23  
# Default sensor I2C address

bus = smbus.SMBus(1)  
# initialize the 12C bus

def read_light():
    data = bus.read_i2c_block_data(ADDRESS, 0x20)
    return ((data[1] + (256 * data[0])) / 1.2)
    # read 2-bytes data and return the decimal num (lux value)


def light_categ(light_data):
    if light_data > 1500:
        return "Too bright"
    elif light_data > 700:
        return "Bright"
    elif light_data > 300:
        return "Medium"
    elif light_data > 30:
        return "Dark"
    else:
        return "Too dark"

def main():
    try:
        # same as loop
        while True:
            print(light_categ(read_light()))
            time.sleep(0.5)
    
    except KeyboardInterrupt:

        print("program terminated")
        

if __name__ == "__main__":
    main()
