# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/03_simulators.ipynb.

# %% auto 0
__all__ = []

# %% ../nbs/03_simulators.ipynb 4
# from collections import namedtuple, defaultdict
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
# from copy import copy
# import time
# import math
# from pprint import pprint
## !pip install -U "ray"
# import ray
# import json

# from AIShiftScheduler_KE5.config import *
import AIShiftScheduler_KE5.config as cf
# from AIShiftScheduler_KE5.loader import *
import AIShiftScheduler_KE5.loader as ldr

# %% ../nbs/03_simulators.ipynb 8
pd.options.display.float_format = '{:,.4f}'.format
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
