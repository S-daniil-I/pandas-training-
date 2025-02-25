import pandas as pd
import numpy as np

series_from_list=pd.Series([5,6,9.8,1,7],
                           index=['row_1','row_2 ','row_3','row_4','row_5 '],
                           name='Pd_Series'
                           )
print(series_from_list)