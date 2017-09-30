
# coding: utf-8

# In[7]:

"""
Always have this in the header of a Notebook
"""
# Allow modules and files to be loaded with relative paths
from pkg_resources import resource_filename
import sys
sys.path.append(resource_filename(__name__, ""))

# We don't execute everything unless we're viewing in a notebook
IN_JUPYTER = 'get_ipython' in globals() and get_ipython().__class__.__name__ == "ZMQInteractiveShell"


# In[8]:

import logging
logging.basicConfig(level="INFO")

logger = logging.getLogger('notebook')
logger.info('Test')


# In[ ]:


