import pandas
import matplotlib.pyplot as plt
df=pandas.read_excel('/translog.xls')
df=df.drop(['To Date','Rep Date','Date','Time','Initial','Member/Tkt'],axis=1)
df.dropna(inplace=True)
df=df.rename(columns={'Txn Type':'use'})
df=df.rename(columns={'Accn Id':'book'})
df.loc[df['use'].str.contains('Chrging'), 'use'] = 'issue'
df.loc[df['use'].str.contains('Rchrgng'), 'use'] = 'issue'
df[df.use == 'issue']
cf=df['book'].value_counts()
x=list(cf.index[0:4])
y=list(cf.values[0:4])
plt.bar(x,y)
plt.show()

