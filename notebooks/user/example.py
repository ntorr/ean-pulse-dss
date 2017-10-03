
# coding: utf-8

# In[1]:

"""
Always have this in the header of the Notebook
"""
# Setup logging
import logging
logging.basicConfig(level="INFO")
logger = logging.getLogger('Notebook')

# Allow modules and files to be loaded with relative paths ...
from pkg_resources import resource_filename
import sys
sys.path.append(resource_filename(__name__, ""))
# ... or rather this way?
# TODO - understand the best way to import development code
import os
module_path = os.path.abspath(os.path.join('..', '..'))
if module_path not in sys.path:
    sys.path.append(module_path)

# Set variable to remove functions that are not useful in production e.g. rendering images
IN_JUPYTER = 'get_ipython' in globals() and get_ipython().__class__.__name__ == "ZMQInteractiveShell"

# standard imports
from pulse_dss.config import Config


# In[2]:

"""
The execute function must be included in all notebooks that are to be run in production
This allows Jupyter Notebooks to implement an abstracted execute() function
It returns a Pandas DataFrame
"""
def execute(train, score, config=Config()):
    logger.info('Calling notebook execute')
    logger.debug('Training data = %s' % str(train))
    logger.debug('Scoring data = %s' % str(score))
    
    # safe way to get configurable
    parameter = config.get('parameter', default=1.0)
    
    # in this example, simply merge the train and score data
    return train.append(score, ignore_index=True)


# In[3]:

"""
Below you can put code for testing, plotting and collecting local data whilst prototyping
Nesting in the condition means none of this code will be called in production
"""
if IN_JUPYTER:
    # Place prototyping code here
    pass

