"""Object Oriented Programming example
"""

class Cake:
    """A "recipe" class for how to bake a cake."""
    x = 2
    
    def __init__(self):
        self.baked = False


    def baked(self):
        self.baked = True
        print("All Done")

class DataCleaner:
    """A class for cleaning up your data!"""
    import numpy as np
    import pandas as pd

    def __init__(self, df):
        self.df = df

    def replace_values(self, value=np.nan, new=0):
      """Replace values in a dataframe"""
        self.df = self.df.replace(value, new)

    def impute_values(self):
        pass 

class LemonTart(Cake):
    y = 3

    def bake(self):
        self.baked = True
        print("Yummy, a tart!")
