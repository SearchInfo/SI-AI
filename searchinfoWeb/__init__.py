from flask import Flask

app= Flask(name)
from filter import filters
from bayes import BayesianFilter
import nltk
from nltk.collocations import *
from nltk.metrics import ContingencyMeasures, BigramAssocMeasures, TrigramAssocMeasures, QuadgramAssocMeasures
from numpy import show_config as show_numpy_config
from . import core
from . import multiarray
from . import overrides
import add_docstring
from scipy.stats.stats import betai
