"""
Simple configuration object
"""
import logging
logger = logging.getLogger(__file__)


class Config(object):
    def __init__(self, config=None):
        object.__init__(self)
        self.__cfg = config if config is not None else dict()

    def get(self, name, default):
        if isinstance(self.__cfg, dict):
            try:
                return self[name]
            except KeyError:
                pass
        logger.warning('Setting default parameter %s = %s' % (name, default))
        return default

    def __getitem__(self, item):
        return self.__cfg[item]
