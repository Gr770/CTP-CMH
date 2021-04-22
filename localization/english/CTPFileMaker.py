import pandas as pd
import numpy as np
df = pd.read_csv("/CTP.csv",index_col=0)
df.fillna(value= "", inplace=True)
X =[]
for ind in df.index :
  for column in df.columns:
    if df.loc[ind,column] == "" and column != df.columns[0]:
      X.append(str(ind)+str(column)+':"'+'$'+str(ind)+str(df.columns[0])+'$'+'"'+ '\n')
    else:
      X.append(str(ind)+str(column)+':"'+str(df.loc[ind,column])+'"'+ '\n')
file1 = open("/text.txt",'w',encoding='utf-8')
file1.writelines(X)
file1.close()