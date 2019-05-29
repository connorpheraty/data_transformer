class DataTransformer:
    "A class with functions designed to help clean data in a dataset."

    import pandas as pd 
    import numpy as np 

    def __init__(self, df):
        self.df = df
    
    def root_squared(self, col):
        '''Function that squares and roots all the values in a column.'''
        #num = self[col] ** 2
        #num = num ** .5
        #return(num)

    def cardinality(self, thresh=10):
        '''Function for machine learning preprocessing that bins columns into
        high and low cardinality lists'''
        import pandas as pd

        high_card = []
        low_card = []

        unique_df = self.nunique()
        unique_df = pd.DataFrame(self.nunique())
        unique_df = unique_df.reset_index()

        for col, num in unique_df.values:
            if num > thresh:
                high_card.append(col)
            else:
                low_card.append(col)
          
        print("The High Cardinality columns are: ", high_card, "\n",
             "The Low Cardinality columns are: ", low_card)

    def cat_num_split(self):

        numeric = ['int_', 'intc', 'intp', 'int8', 'int16', 'int32', 'int64',
                  'uint8', 'uint16', 'uint32', 'uint64', 'float_', 'float16',
                  'float64', 'complex_', 'complex64', 'complex128']

        df_num = self.select_dtypes(include=numeric)
        df_cat = self.drop(df_num, axis='columns')

        print("The numeric columns are: ", df_num.columns, '\n \n',
              "The categorical columns are: ",df_cat.columns)


        

        
        
        
        

        



