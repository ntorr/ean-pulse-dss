import os
import re
import hashlib
import logging

logging.basicConfig(level="DEBUG")
logger = logging.getLogger(__file__)


def hash_notebook(module_name):
    """
    Takes notebook module alias as argument and produces unique hash
    :param module_name: str, notebook module name
    :return: str, sha1 hash
    """
    mod = __import__(module_name)
    path = os.path.abspath(mod.__file__)

    # hash on python rendering, not .ipynb to prevent saving when actual code doesn't change
    file = open(path)
    char = str(file.readlines())
    char = re.sub('[\s+]', '', char)
    sha1 = hashlib.sha1(char.encode()).hexdigest()
    logger.debug('hashing object string ...')
    logger.debug('object string = %s' % char)
    logger.debug('object hash = %s' % sha1)
    return sha1


if __name__ == '__main__':
    logger.info(hash_notebook('notebooks.user.test_new'))
