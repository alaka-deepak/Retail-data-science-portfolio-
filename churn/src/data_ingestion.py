
import os
import pandas as pd

def load_data():

    folder="/Users/deepaksivas/Documents/GitHub/Retail-data-science-portfolio-/churn/data"
    filename="E Commerce Dataset.xlsx"
    file_path=os.path.join(folder, filename)
    data=pd.read_excel(file_path,sheet_name='E Comm')
    print(data.head(5))
    return data
