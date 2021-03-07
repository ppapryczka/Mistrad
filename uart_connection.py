import serial as pySerial
import logging
import uart_connection_utils as utils
from typing import List

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class UARTConnection():
    connection: pySerial.Serial

    def __init__(self, port: str = '/dev/ttyACM0',
                 baudrate: int = 115200,
                 parity: str = pySerial.PARITY_NONE,
                 stopbits: int = pySerial.STOPBITS_ONE,
                 bytesize: int = pySerial.EIGHTBITS,
                 timeout: float = 1.0):
        self.connection = pySerial.Serial(
            port=port,
            baudrate=baudrate,
            parity=parity,
            stopbits=stopbits,
            bytesize=bytesize,
            timeout=timeout,
        )

    def read_line(self) -> bytes:
        # TODO - reading should check length and append as long as don't occur line end character
        data: bytes = self.connection.read(size=utils.MESSAGE_LINE_SIZE)
        logger.debug(f"Read bytes: {data}")
        return data

    def write(self, data_to_write: bytes) -> None:
        # TODO - send lines?
        logger.debug(f"Write bytes: {data_to_write}")
        self.connection.write(data_to_write)

    def write_lines(self, data_lines: List[str]) -> None:
        for line in data_lines:
            logger.debug(f"Write str: {line}")
            logger.debug(f"Write bytes: {line.encode()}")
            self.connection.write(line.encode())
