
# -*- coding: UTF-8 -*-

from . import CLI;
from . import TEL;

from .OLDLog import logger;
from .OLDLog import loggergetter;



__all__ = [
    "CLI",
    "TEL",
    "logger",
    "loggergetter"
]

__author__ = "Tarcadia, Mundanity-fc";
__url__ = "https://github.com/Tarcadia/Old-Linkage-Dev";
__copyright__ = "Copyright 2021";
__credits__ = ["Tarcadia", "Mundanity-fc"];
__license__ = "GNU GENERAL PUBLIC LICENSE VERSION 3";
__version__ = "ProtoType 1.0.0";

logger.info('OLD Loaded.');
logger.info('Locense: %s' % __license__);
logger.info('Version: %s' % __version__);
logger.info('Find on: %s' % __url__);
logger.info('%s (c) %s' % (__author__, __copyright__));
