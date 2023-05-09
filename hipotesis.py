import numpy as np
import scipy.stats as stats

def z_test(x, mu, sigma):
    xbar = np.mean(x)
    n = len(x)
    zo = (xbar - mu)/(sigma/np.sqrt(n))
    valorp = (1 - stats.norm.cdf(zo))*2
    return zo, valorp