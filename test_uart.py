import serial as pySerial
import uart_connection_utils as utils

if __name__ == "__main__":
    ser: pySerial.Serial = pySerial.Serial(
        port='COM3',
        baudrate=115200,
        parity=pySerial.PARITY_NONE,
        stopbits=pySerial.STOPBITS_ONE,
        bytesize=pySerial.EIGHTBITS,
        timeout=1,
    )

    if ser.isOpen():
        print("yupi!")

    while True:
        try:
            data = ser.read(size=utils.MESSAGE_LINE_SIZE)
            if data:
                print(data)
                data = data.decode()
                print(data, len(data))
        except UnicodeDecodeError as ex:
            print(ex)

    print("We are on a mission from God!")