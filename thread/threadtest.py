import threading
import time 
import logging
def get_logger(name):
    logger = logging.getLogger("threading_example")
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler(name + ".log")
    fmt = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)

    logger.addHandler(fh)
    return logger


def doubler(number, logger):
    """
    """
    logger.debug('doubler function executing')
    result = number * 2
    logger.debug('doubler function ended with: {}'.format(
        result))


if __name__ == '__main__':
    thread_names = ['Mike', 'George', 'Wanda', 'Dingbat', 'Nina']
    logger = [get_logger(name) for name in thread_names]
    for i in range(5):
        my_thread = threading.Thread(
            target=doubler, name=thread_names[i], args=(i,logger[i]))
        my_thread.start()