import fault_injection_messages
import serial as pySerial

if __name__ == "__main__":
    connection = pySerial.Serial(
        port = '/dev/ttyACM0',
        baudrate = 115200,
        parity= pySerial.PARITY_NONE,
        stopbits = pySerial.STOPBITS_ONE,
        bytesize = pySerial.EIGHTBITS,
        timeout= 1.0)

    conf = fault_injection_messages.get_InjectionConfiguration(logging=True,
                                                        memory_injection_actions=0,
                                                        register_injection_actions=0)

    conf_array = fault_injection_messages.encode_InjectionConfiguration(conf)

    to_send = bytearray(conf_array)

    connection.write(data=to_send)
    # while 1:
    #    connection.write([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])


    print("We are on a mission from God!")