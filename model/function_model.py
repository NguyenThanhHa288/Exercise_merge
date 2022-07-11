import numpy as np
from sklearn.impute import SimpleImputer


def miss_value(object):
    sim = SimpleImputer(missing_values=np.nan, strategy='mean')
    imputed_data_X = sim.fit_transform(object)
    m=1
    return imputed_data_X


def normalize(x):
    Test = x[:, 1:]
    mu = np.mean(x, axis=0)
    sigma = np.std(x, axis=0)
    x[:, 1:] = np.divide(np.subtract(Test, mu[1:]),
                         sigma[1:])
    return x


def add_bias(x):
    m = len(x)
    bias = np.ones(m)
    x = np.vstack((bias, x.T)).T
    return x
