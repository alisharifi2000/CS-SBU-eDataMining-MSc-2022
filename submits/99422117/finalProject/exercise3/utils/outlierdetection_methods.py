import numpy
import pandas


def zscorefilter(col):
    # OPTION 1: z-score filter: z-score < 3
    lim = numpy.abs((col - col.mean()) / col.std(ddof=0)) < 3
    return lim


def quantilefilter(col):
    # OPTION 2: quantile filter: discard 1% upper / lower values
    lim = numpy.logical_and(col < col.quantile(0.99), col > col.quantile(0.01))
    return lim


def iqrfilter(col):
    # OPTION 3: iqr filter: within 2.22 IQR (equiv. to z-score < 3)
    iqr = col.quantile(0.75) - col.quantile(0.25)
    lim = col.abs((col - col.median()) / iqr) < 2.22
    return lim