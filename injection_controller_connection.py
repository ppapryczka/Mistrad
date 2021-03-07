import logging

from uart_connection import UARTConnection
from uart_connection_utils import *
import injection_conf
import fault_injection_messages


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def check_if_state_header_correct(data: bytes, expected_data_header: bytes) -> bool:
    return data[0:len(expected_data_header)] == expected_data_header


class InjectionControllerConnection:
    connection: UARTConnection
    conf: injection_conf.InjectionConf

    def __init__(self, connection: UARTConnection, conf: injection_conf.InjectionConf):
        self.connection = connection
        self.conf = conf

    def start_connection(self, max_retries: int = 5):
        retries = 0
        conf_send_success: bool = False

        while retries<max_retries and not conf_send_success:
            # step 1 -  WAITING_FOR_CONF_MSG
            line_msg = self.connection.read_line()

            if check_if_state_header_correct(line_msg, WAITING_FOR_CONF_MSG):
                # send configuration
                self.connection.write_lines(self.conf.get_conf_as_lines())
            else:
                # not expected msg
                logger.debug(f"Get not expected message, expected msg = {WAITING_FOR_CONF_MSG}")
                retries = retries + 1
                continue

            # step 2 - CONF_RECEIVED_MSG
            line_msg = self.connection.read_line()
            if not check_if_state_header_correct(line_msg, CONF_RECEIVED_MSG):
                logger.debug(f"Get not expected message, expected msg = {CONF_RECEIVED_MSG}")
                retries = retries + 1
                continue

            # step 3 - CONF_INFO_MSG
            line_msg = self.connection.read_line()

            if check_if_state_header_correct(line_msg, CONF_INFO_MSG):
                # TODO: for now is always correct and it is not "0/1" when encode in such way!
                self.connection.write_lines([str(create_empty_line(1))])

            else:
                logger.debug(f"Get not expected message, expected msg = {CONF_RECEIVED_MSG}")
                retries = retries + 1
                continue

            conf_send_success = True


        while(1):
            line_msg = self.connection.read_line()
            logger.debug(f"Get log msg = {line_msg}")


if __name__ == "__main__":
    connection = UARTConnection(timeout=None)

    conf: injection_conf.InjectionConf = injection_conf.get_dummy_configuration()

    controller = InjectionControllerConnection(connection=connection, conf=conf)

    controller.start_connection()

