# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_config.ipynb.

# %% auto 0
__all__ = ['MODES', 'BASE_DIR', 'FILE_NAME', 'SICK_PROBS', 'MERIT_PROBS', 'EXOG_INFO', 'BEST_THETA_Alloc', 'MAX_RESOURCE_TYPES',
           'MAX_RESOURCE_IDS', 'RESOURCE_TYPES', 'RESOURCE_TYPE_COUNTS', 'TYPES', 'RESOURCE_IDS',
           'DEMANDS_PER_BUSYNESS', 'DEMAND_PER_BUSYNESS', 'DEMANDS_PER_VOLUME', 'DEMAND_PER_VOLUME',
           'DEMANDS_PER_REVENUE', 'DEMAND_PER_REVENUE', 'RESOURCE_EXPENSES', 'RESOURCE_EXPENSE', 'aNAMES', 'bNAMES',
           'abNAMES', 'piNAMES', 'thNAMES', 'RESOLUTION', 'SLOTS_PER_DAY', 'DATE_TIME_DELTA', 'BLOCK_START_HOUR',
           'SEED_TRAIN', 'SEED_EVALU', 'TH_CumSlots_SPEC', 'TH_SickProb_SPEC', 'TH_CumMerits_SPEC', 'TH_ContSlots_SPEC',
           'TH_Select_SPEC', 'SIM_T', 'SIM_MU_D', 'SIM_EVENT_TIME_D', 'SIM_MU_DELTA_D', 'START_DATE_TIME', 'sd',
           'MAX_DAILY_SLOT_RUN', 'CONTIGUOUS_REWARD', 'GOV_UTIL_THESH', 'slots_per_day_and_date_time_delta',
           'get_availabilities', 'get_dow_qod_capacities', 'get_dow_hod_capacities', 'get_dow_bod_capacities',
           'get_capacities']

# %% ../nbs/02_config.ipynb 4
# from collections import namedtuple, defaultdict
# import numpy as np
import pandas as pd
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# from copy import copy
# import time
# import math
# from pprint import pprint
## !pip install -U "ray"
# import ray
# import json

# from AIShiftScheduler_KE5.loader import *
import AIShiftScheduler_KE5.loader as ldr

# %% ../nbs/02_config.ipynb 9
## PARAMETERS
## MODES:
## TRAIN|LEARN
## EVALU
## INFER|APPLY|SERVE
# MODES = ['LEARN']
MODES = ['TRAIN', 'EVALU']
# MODES = ['TRAIN', 'EVALU', 'INFER']
# MODES = ['EVALU', 'INFER']
# MODES = ['INFER']

# %% ../nbs/02_config.ipynb 10
# BASE_DIR = '.'
BASE_DIR = '..'
FILE_NAME = 'shift_scheduler_data.xlsx'

# %% ../nbs/02_config.ipynb 11
SICK_PROBS = ldr.load_sick_probs(f'{BASE_DIR}/{FILE_NAME}')
MERIT_PROBS = ldr.load_merit_probs(f'{BASE_DIR}/{FILE_NAME}')
EXOG_INFO = ldr.load_exog_info(f'{BASE_DIR}/{FILE_NAME}')

# %% ../nbs/02_config.ipynb 12
BEST_THETA_Alloc = (0, 0, 0, 1, 'random') #will be written/read eventually

# %% ../nbs/02_config.ipynb 14
MAX_RESOURCE_TYPES = 3
MAX_RESOURCE_IDS = 13

# %% ../nbs/02_config.ipynb 15
## RESOURCE_TYPES = ['Courtesy', 'Stocker', 'Cleaner', 'Curbsider'] ## <<< ========= INPUT ==============
RESOURCE_TYPES = ['Manager', 'AssistMngr', 'RetailAssoc'] ## <<< ========= INPUT ==============

# %% ../nbs/02_config.ipynb 16
RESOURCE_TYPE_COUNTS = [1, 2, 10] ## <<< ========= INPUT ==============
assert len(RESOURCE_TYPES) == len(RESOURCE_TYPE_COUNTS)
assert len(RESOURCE_TYPES) <= MAX_RESOURCE_TYPES
print(f'\n{len(RESOURCE_TYPES)=}')
print(RESOURCE_TYPES)

# %% ../nbs/02_config.ipynb 17
## TYPES = ['Courtesy']*7 + ['Stocker']*3 + ['Cleaner']*2 + ['Curbsider']*4
TYPES = []
for i in range(len(RESOURCE_TYPES)):
  additional_types = [RESOURCE_TYPES[i]]*RESOURCE_TYPE_COUNTS[i]
  for item in additional_types:
    TYPES.append(item)
print(f'\n{len(TYPES)=}')
print(TYPES)

# %% ../nbs/02_config.ipynb 18
RESOURCE_IDS = [ ## <<< ========= INPUT ==============
  'Matt', 
  'Mike', 'Tanner', 
  'Jake', 'James', 'Jane', 'John', 'Jim', 'Jenny', 'Jeremy', 'Judy', 'Julie', 'Jeffrey']
assert len(RESOURCE_IDS) == len(TYPES)
assert len(RESOURCE_IDS) <= MAX_RESOURCE_IDS

# %% ../nbs/02_config.ipynb 19
## eventually learn, call thBusyRate
## demand/busyness ## <<< ========= INPUT ==============
## add demands of 0 up to these values as busyness varies from 0 to 100%
DEMANDS_PER_BUSYNESS = [.005, .008, .02] ##set to [0, 0, 0] to disregard
DEMAND_PER_BUSYNESS = {e: DEMANDS_PER_BUSYNESS[i] for i,e in enumerate(RESOURCE_TYPES)}
assert len(DEMANDS_PER_BUSYNESS) == len(RESOURCE_TYPES)

# %% ../nbs/02_config.ipynb 20
## eventually learn, call thVolumeRate
## demand/volume ## <<< ========= INPUT ==============
DEMANDS_PER_VOLUME = [.03, .08, .2] ##set to [0, 0, 0] to disregard
DEMAND_PER_VOLUME = {e: DEMANDS_PER_VOLUME[i] for i,e in enumerate(RESOURCE_TYPES)}
assert len(DEMANDS_PER_VOLUME) == len(RESOURCE_TYPES)

# %% ../nbs/02_config.ipynb 21
## eventually learn, call thRevenueRate
## demand/revenue ## <<< ========= INPUT ==============
DEMANDS_PER_REVENUE = [.00005, .0001, .0008] ##set to [0, 0, 0] to disregard
DEMAND_PER_REVENUE = {e: DEMANDS_PER_REVENUE[i] for i,e in enumerate(RESOURCE_TYPES)}
assert len(DEMANDS_PER_REVENUE) == len(RESOURCE_TYPES)

# %% ../nbs/02_config.ipynb 22
## what it costs to pay the human resources being scheduled
RESOURCE_EXPENSES = [25.00, 20.00, 18.00] ## <<< ========= INPUT ==============
RESOURCE_EXPENSE = {e: RESOURCE_EXPENSES[i] for i,e in enumerate(RESOURCE_TYPES)}
assert len(RESOURCE_EXPENSES) == len(RESOURCE_TYPES)

# %% ../nbs/02_config.ipynb 23
## *resource* attribute vectors
aNAMES = [tup[0]+'_'+tup[1] for tup in zip(TYPES, RESOURCE_IDS)]
print(f'{len(aNAMES)=}')
print(aNAMES)

# %% ../nbs/02_config.ipynb 24
## *demand* attribute vectors
bNAMES = RESOURCE_TYPES
print(f'\n{len(bNAMES)=}')
print(bNAMES)

# %% ../nbs/02_config.ipynb 25
## *decision* 'attribute' vectors
abNAMES = [] ##to DEMAND b
for a in aNAMES:
  a0,a1 = a.split('_')
  for b in bNAMES:
    if(a0==b):
      abn = (a + '___' + b)
      abNAMES.append(abn)
print(f'\n{len(abNAMES)=}')
print(abNAMES)

# %% ../nbs/02_config.ipynb 26
piNAMES = ['X__Alloc'] ##policy names
thNAMES = [ ##theta names
  'thCumSlots',
  'thSickProb',
  'thCumMerits',
  'thContSlots',
  'thSelect'
  ## 'thBusyRate' ##later
]
print(f'\n{len(thNAMES)=}')
print(f'{thNAMES=}')

# %% ../nbs/02_config.ipynb 27
# RESOLUTION = 'HOUR' ## 'BLOCK_8_HOUR', 'HOUR', 'QUARTER_HOUR', 
# if RESOLUTION == 'QUARTER_HOUR':
#   SLOTS_PER_DAY = 96
#   DATE_TIME_DELTA = '15min'
# elif RESOLUTION == 'HOUR':
#   SLOTS_PER_DAY = 24
#   DATE_TIME_DELTA = '1H'
# elif RESOLUTION == 'BLOCK_8_HOUR':
#   SLOTS_PER_DAY = 3
#   DATE_TIME_DELTA = '8H'
#   ## DATE_TIME_DELTA = {0: '6H', 1: '10H', 2: '8H'} ##maybe in future?
# else:
#   print(f'ERROR: Invalid RESOLUTION: {RESOLUTION}')
def slots_per_day_and_date_time_delta(resolution):
    if resolution == 'QUARTER_HOUR':
      slots_per_day = 96
      date_time_delta = '15min'
    elif resolution == 'HOUR':
      slots_per_day = 24
      date_time_delta = '1H'
    elif resolution == 'BLOCK_8_HOUR':
      slots_per_day = 3
      date_time_delta = '8H'
      ## DATE_TIME_DELTA = {0: '6H', 1: '10H', 2: '8H'} ##maybe in future?
    else:
      print(f'ERROR: Invalid resolution: {resolution}')
      slots_per_day = 0
      date_time_delta = 'error'    
    return slots_per_day, date_time_delta

# %% ../nbs/02_config.ipynb 28
RESOLUTION = 'HOUR' ## 'BLOCK_8_HOUR', 'HOUR', 'QUARTER_HOUR', 
SLOTS_PER_DAY, DATE_TIME_DELTA = slots_per_day_and_date_time_delta(RESOLUTION)

# %% ../nbs/02_config.ipynb 29
BLOCK_START_HOUR = {0: 0, 1: 8, 2:16}

# %% ../nbs/02_config.ipynb 31
def get_availabilities(dt):
  avails = \
    EXOG_INFO.loc[
      EXOG_INFO['Date']==dt,
      [col for col in EXOG_INFO.columns if col in [f'A_{a}' for a in range(len(RESOURCE_IDS))]]
    ].iloc[0]
  avails.reset_index(drop=True, inplace=True) ##to start index at 0
  return avails

# %% ../nbs/02_config.ipynb 32
def get_dow_qod_capacities(dow):
  capacities = \
    EXOG_INFO.loc[
      (EXOG_INFO['DOW']==dow),
      [col for col in EXOG_INFO.columns if col in [f'A_{a}' for a in range(len(RESOURCE_IDS))]]
    ].sum(axis=0) ##total daily capacity
  capacities.reset_index(drop=True, inplace=True)
  return capacities

# %% ../nbs/02_config.ipynb 33
def get_dow_hod_capacities(dow):
  capacities = \
    EXOG_INFO.loc[
      (EXOG_INFO['DOW']==dow),
    ].groupby(['HOD']).first()
  capacities = capacities[[col for col in EXOG_INFO.columns if col in [f'A_{a}' for a in range(len(RESOURCE_IDS))]]]
  capacities = capacities.sum(axis=0) ##total daily capacity
  capacities.reset_index(drop=True, inplace=True)
  return capacities

# %% ../nbs/02_config.ipynb 34
def get_dow_bod_capacities(dow):
  capacities = \
    EXOG_INFO.loc[
      (EXOG_INFO['DOW']==dow),
    ].groupby(['BOD']).first()
  capacities = capacities[[col for col in EXOG_INFO.columns if col in [f'A_{a}' for a in range(len(RESOURCE_IDS))]]]
  capacities = capacities.sum(axis=0) ##total daily capacity
  capacities.reset_index(drop=True, inplace=True)
  return capacities

# %% ../nbs/02_config.ipynb 35
def get_capacities(dow):
  if RESOLUTION == 'QUARTER_HOUR':
    return get_dow_qod_capacities(dow)
  elif RESOLUTION == 'HOUR':
    return get_dow_hod_capacities(dow)
  elif RESOLUTION == 'BLOCK_8_HOUR':
    return get_dow_bod_capacities(dow)
  else:
    print(f'ERROR: Invalid RESOLUTION: {RESOLUTION}')
    return None

# %% ../nbs/02_config.ipynb 36
SEED_TRAIN = 77777777
SEED_EVALU = 88888888
## N_SAMPLEPATHS = 100; L = N_SAMPLEPATHS
## N_TRANSITIONS = 100; T = N_TRANSITIONS

# %% ../nbs/02_config.ipynb 37
TH_CumSlots_SPEC = (0, 1, .2)
TH_SickProb_SPEC = (0, 1, .2)
TH_CumMerits_SPEC = (0, 1, .2)
TH_ContSlots_SPEC = (0, 1, .2)
## TH_Select_SPEC = ('random', 'ranked_CumMerits')
TH_Select_SPEC = ('random',)
## TH_Select_SPEC = ('ranked_CumMerits',)

# %% ../nbs/02_config.ipynb 38
SIM_T = 60
## SIM_MU_D = {bNAMES[0]: 4, bNAMES[1]: 2}
SIM_MU_D = {bNAMES[0]: 4, bNAMES[1]: 2, bNAMES[2]: 2}
print(f'\n{SIM_MU_D=}')
assert len(SIM_MU_D.items())==len(bNAMES)

## SIM_EVENT_TIME_D = {bNAMES[0]: None, bNAMES[1]: None, bNAMES[2]: None, bNAMES[3]: None}
## SIM_EVENT_TIME_D = {bNAMES[0]: None, bNAMES[1]: None}
SIM_EVENT_TIME_D = {bNAMES[0]: None, bNAMES[1]: None, bNAMES[2]: None}
print(f'\n{SIM_EVENT_TIME_D=}')
assert len(SIM_EVENT_TIME_D.items())==len(bNAMES)

## SIM_MU_DELTA_D = {bNAMES[0]: None, bNAMES[1]: None, bNAMES[2]: None, bNAMES[3]: None}
SIM_MU_DELTA_D = {bNAMES[0]: None, bNAMES[1]: None, bNAMES[2]: None}
print(f'\n{SIM_MU_DELTA_D=}')
assert len(SIM_MU_DELTA_D.items())==len(bNAMES)

# %% ../nbs/02_config.ipynb 39
START_DATE_TIME = '2023-12-04'
## START_DATE_TIME = '2023-10-30T22:00' ##works too
sd = pd.to_datetime(START_DATE_TIME)
assert sd.strftime('%a')=='Mon'

# %% ../nbs/02_config.ipynb 40
MAX_DAILY_SLOT_RUN = 8
assert MAX_DAILY_SLOT_RUN<=SLOTS_PER_DAY

# %% ../nbs/02_config.ipynb 41
CONTIGUOUS_REWARD = 1

# %% ../nbs/02_config.ipynb 42
GOV_UTIL_THESH = 0.40
