
# -*- coding: UTF-8 -*-

import logging;

LOG_FILE = './OLD.log';

logger = logging.getLogger("OLD");
logger.setLevel(logging.DEBUG);

_logger_formatter_scrn = logging.Formatter(fmt='\033[0m%(asctime)s \033[1;34m[%(levelname)s]\033[35m[%(name)s]\033[33m >> \033[0m%(message)s', datefmt='%H:%M');
_logger_ch_scrn = logging.StreamHandler();
_logger_ch_scrn.setLevel(logging.INFO);
_logger_ch_scrn.setFormatter(_logger_formatter_scrn);

_logger_formatter_file = logging.Formatter(fmt='[%(asctime)s][%(levelname)s][%(name)s] >> %(message)s', datefmt='%Y-%m-%d-%H:%M:%S');
_logger_ch_file = logging.FileHandler(LOG_FILE, encoding = 'utf8');
_logger_ch_file.setLevel(logging.DEBUG);
_logger_ch_file.setFormatter(_logger_formatter_file);

logger.addHandler(_logger_ch_scrn);
logger.addHandler(_logger_ch_file);

def loggergetter(name = "OLD_loggergetted"):
    logger = logging.getLogger(name);
    logger.setLevel(logging.DEBUG);

    _logger_formatter_scrn = logging.Formatter(fmt='\033[0m%(asctime)s \033[1;34m[%(levelname)s]\033[36m[%(name)s]\033[33m >> \033[0m%(message)s', datefmt='%H:%M');
    _logger_ch_scrn = logging.StreamHandler();
    _logger_ch_scrn.setLevel(logging.INFO);
    _logger_ch_scrn.setFormatter(_logger_formatter_scrn);

    _logger_formatter_file = logging.Formatter(fmt='[%(asctime)s][%(levelname)s][%(name)s] >> %(message)s', datefmt='%Y-%m-%d-%H:%M:%S');
    _logger_ch_file = logging.FileHandler(LOG_FILE, encoding = 'utf8');
    _logger_ch_file.setLevel(logging.DEBUG);
    _logger_ch_file.setFormatter(_logger_formatter_file);

    logger.addHandler(_logger_ch_scrn);
    logger.addHandler(_logger_ch_file);

    return logger;
