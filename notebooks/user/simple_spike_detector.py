
# coding: utf-8

# In[30]:

"""
Always have this in the header of the Notebook
"""
# Setup logging
import logging
logging.basicConfig(level="INFO")
logger = logging.getLogger('Notebook')

# Allow modules and files to be loaded with relative paths
from pkg_resources import resource_filename
import sys
sys.path.append(resource_filename(__name__, ""))

# Set variable to remove functions that are not useful in production e.g. rendering images
IN_JUPYTER = 'get_ipython' in globals() and get_ipython().__class__.__name__ == "ZMQInteractiveShell"


# In[31]:

"""
The execute function must be included in all notebooks that are to be run in production
This allows Jupyter Notebooks to implement an abstracted execute() function
It returns a Pandas DataFrame
"""
def execute(train, score):
    logger.info('Calling notebook execute ...')
    logger.debug('Training data = %s' % str(train))
    logger.debug('Scoring data = %s' % str(score))
    
    # compute median
    median = train['observation'].median()
    merged = train.append(score, ignore_index=True)
    last_index = merged.index[-1]
    train['residuals'] = train['observation'] - median
    std = train['residuals'].std()
    merged.loc[last_index, 'anomaly'] = merged.loc[last_index, 'observation'] > 3.0 * std
    
    return merged.loc[[last_index]]


# In[32]:

"""
Below you can put code for testing, plotting and collecting local data whilst prototyping
Nesting in the condition means none of this code will be called in production
"""
if IN_JUPYTER:
    # Place prototyping code here
    import pandas as pd
    
    train_cols = ['observation', 'anomaly']
    train_data = [[1.0, 0], [1.1, 0], [10.0, 1], [1.0, 0], [0.8, 0]]
    train_index = [1, 2, 3, 4, 5]
    train = pd.DataFrame(data=train_data, columns=train_cols, index=train_index)
    
    score_cols = ['observation']
    score_data = [[2.0]]
    score_index = [6]
    score = pd.DataFrame(data=score_data, columns=score_cols, index=score_index)
    
    print(execute(train, score))
    
    pass

