
#!/usr/bin/env python
# coding: utf-8
 
__author__ = "Glon Ho"
 
import logging
 
 
def get_logger(logger_name, log_file, level=logging.INFO):
    l = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(asctime)s : %(message)s', "%Y-%m-%d %H:%M:%S")
    fileHandler = logging.FileHandler(log_file, mode='a')
    fileHandler.setFormatter(formatter)
 
    l.setLevel(level)
    l.addHandler(fileHandler)
 
    return l
 
 
if __name__ == '__main__':
 
    log_file1='C:\\Users\\zhtang\\Desktop\\pythoncode\\getloggerlogger_test1.log'
    log_file2='C:\\Users\\zhtang\\Desktop\\pythoncode\\getloggerlogger_test2.log'
    
    logger1 = get_logger('Glon', log_file1)
    logger2 = get_logger('GlonHo', log_file2)
 
    logger1.info('>>> test1 log msg: %s', "111111111111111111111")
    logger2.info('>>> test2 log msg: %s', "222222222222222222222")
