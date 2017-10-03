
# coding: utf-8

# In[ ]:

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


# In[ ]:

"""
The execute function must be included in all notebooks that are to be run in production
This allows Jupyter Notebooks to implement an abstracted execute() function
It returns a Pandas DataFrame
"""
def execute(train, score, config=None):
    logger.info('Calling notebook execute ...')
    logger.debug('Training data = %s' % str(train))
    logger.debug('Scoring data = %s' % str(score))
    
    # imports
    import pandas as pd
    
    # check input data and cut if needed
    assert(len(train) >= config['lookback'])
    train = train[-lookback:]
    
    # compute median
    median = train['observation'].median()

    # compute std deviation on residuals
    train['residuals'] = train['observation'] - median
    std = train['residuals'].std()
    n_sigma = config['n_sigma']
    
    # decide if last point is anomalous
    observation = score.ix[score.index[0], 'observation']
    anomaly = int(abs(observation - median) > n_sigma * std)

    # return result
    return pd.DataFrame(index=score.index, columns=['observation', 'anomaly', 'median'], 
                        data=[[observation, anomaly, median]])


# In[ ]:

"""
Below you can put code for testing, plotting and collecting local data whilst prototyping
Nesting in the condition means none of this code will be called in production
"""
if IN_JUPYTER:
    # Place prototyping code here
    logging.basicConfig(level='DEBUG')
    
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    
    conf = dict()
    conf['n_sigma'] = 1.0
    lookback = 30
    conf['lookback'] = lookback
    lookforward = 200
    
    train_cols = ['observation', 'anomaly', 'median']
    train_data = [[np.random.normal(), None, None] for i in range(lookback)]
    train_index = [i for i in range(lookback)]
    train = pd.DataFrame(data=train_data, columns=train_cols, index=train_index)
    
    score_cols = ['observation']
    score_data = [[np.random.normal()] for i in range(lookforward)]
    score_index = [i + lookback for i in range(lookforward)]
    score = pd.DataFrame(data=score_data, columns=score_cols, index=score_index)
    
    for i in range(lookforward):
        this_train = train[i:lookback + i]
        this_score = score[i:i + 1]
        result = execute(this_train, this_score, conf)
        train = train.append(result, ignore_index=True)
    
    print('final results: \n%s' % train)
    
    train.plot(y=['observation', 'median'])
    plt.show()
    train.plot(y='anomaly')
    plt.show()
    
    pass

