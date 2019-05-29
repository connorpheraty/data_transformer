import numpy as np 
import pandas as pd 
from jeff_rowe_module import NullHelper
from Data_Transformers import DataTransformer as DT

df = pd.read_csv("/Users/connorheraty/Desktop/Datasets/UCI/adult.csv",
                 names=['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status',
                       'spouse_absent', 'occupation', 'relationship', 'race', 'sex', 'capital-gain',
                       'capital-loss', 'hours-per-week', 'native-country'])



df = df.replace(' ?',np.nan)

DT.cardinality(df) 

