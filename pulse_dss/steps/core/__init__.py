import numpy as np
import pandas as pd
import logging
from pulse_dss.steps import Step

logger = logging.getLogger(__name__)


class SimpleAverage(Step):
    def __init__(self, method='mean'):
        Step.__init__(self, __name__)
        self._method = method

    def execute(self, df):
        if self._method == 'mean':
            average = pd.DataFrame(df.mean()).transpose().join(pd.DataFrame(df.std()).transpose(),
                                                               rsuffix='_std', lsuffix='_mean')
        else:
            if self._method != 'median':
                logger.warning('unknown method %s, using median instead' % self._method)
            average = pd.DataFrame(df.median()).transpose().join(pd.DataFrame(df.std()).transpose(),
                                                                 rsuffix='_std', lsuffix='_median')
        return average


class AnomalyRule(Step):
    def __init__(self, factor=3):
        Step.__init__(self, __name__)
        self._factor = factor

    def execute(self, df):
        value = df.ix[0, df.columns[0]] >= abs(self._factor * df.ix[0, df.columns[1]])
        return pd.DataFrame([value], columns=[df.columns[0] + '_rule'])


if __name__ == '__main__':
    avg = SimpleAverage()
    rule = AnomalyRule(factor=-1.0)

    data = pd.DataFrame(data=[np.random.normal() for i in range(10000)],
                        columns=['normal'])  # , 'uniform']) , np.random.uniform()

    data = avg.execute(data)
    print(rule.execute(data))

