class DataTransformer:
    "A class with functions designed to help clean data in a dataset."

    import pandas as pd 
    import numpy as np 

    def __init__(self, df):
        self.df = df
    
    def root_squared(self, col):
        num = self[col] ** 2
        num = num ** .5
        print(num)

    def print_head(self):
        head = self.head()
        print(head)

    def cardinality(self):
        import pandas as pd
        high_card = []
        low_card = []

        unique_df = pd.DataFrame(self.nunique())
        unique_df = unique_df.reset_index()
        #unique_df = unique_df.rename({'index':'col', })
        print(unique_df)

        for ind, num in unique_df:
            for i in num:
                print(i)    
                if i > 10:
                    high_card.append(i)
                else:
                    low_card.append(i)
          
        print("The High Cardinality columns are: ", high_card, "\n",
             "The Low Cardinality columns are: ", low_card)
        
        

        



