# -*- coding: utf-8 -*-
"""VendorRating.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1emZdzp6HG-lcXGozbKu0QV4yW0h_tZcV
"""

from google.colab import files
uploaded = files.upload()

import pandas as pd
import seaborn as sns
from plotly.offline import init_notebook_mode,iplot
import plotly.graph_objects as go
import cufflinks as cf
import numpy as np
init_notebook_mode(connected=True)
import plotly.express as px
import matplotlib.pyplot as plt
import io
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv(io.StringIO(uploaded['compiled.csv'].decode('utf-8')))

df.iloc[26:27 ]

df.info()
# RemainingQty = EnteredReceivedQuantity - QuantityDemandedFinal
# DeliveryTime = EarlyDeliveryDate - ReceivedDate

# Because there are some null values in PercentOfQuantityReturned
df.fillna(0,inplace=True)
df.info()

df['EarlyDeliveryDate'] = pd.to_datetime(df['EarlyDeliveryDate'])
df['ReceivedDate'] = pd.to_datetime(df['ReceivedDate'])
df.info()

vendor1=df[df['Vendor']==1].count()[0]
vendor2=df[df['Vendor']==2].count()[0]
vendor5=df[df['Vendor']==5].count()[0]
vendor8=df[df['Vendor']==8].count()[0]
Remaining_vendors=df[(df['Vendor']!=1) & (df['Vendor']!=2) & (df['Vendor']!=5) & (df['Vendor']!=8)].count()[0]

trace = go.Bar(x = ["Vendor1","Vendor2","Vendor5","Vendor8","Remaining_Vendors"],y=[vendor1,vendor2,vendor5,vendor8,Remaining_vendors],marker=dict(color=[vendor1,vendor2,vendor5,vendor8,Remaining_vendors],colorscale='Viridis',showscale=True))
data=[trace]
#defining layout
layout = go.Layout(xaxis=dict(title='VendorID'),yaxis=dict(title='Top 4 vendors Vs Remaining_Vendors '),hovermode='closest')
#defining figure and plotting
figure = go.Figure(data=data,layout=layout)
figure.update_layout(paper_bgcolor="LightSteelBlue")
figure.show(renderer='colab')

Vendor1_late=len(df[df['Vendor'] == 1]['DeliveryTime'][df[df['Vendor'] == 1]['DeliveryTime'] < 0])
Vendor1_total=len(df[df['Vendor'] == 1]['DeliveryTime'])
Vendor1_fraction=Vendor1_late/Vendor1_total
Vendor2_late=len(df[df['Vendor'] == 2]['DeliveryTime'][df[df['Vendor'] == 2]['DeliveryTime'] < 0])
Vendor2_total=len(df[df['Vendor'] == 2]['DeliveryTime'])
Vendor2_fraction=Vendor2_late/Vendor2_total
Vendor5_late=len(df[df['Vendor'] == 5]['DeliveryTime'][df[df['Vendor'] == 5]['DeliveryTime'] < 0])
Vendor5_total=len(df[df['Vendor'] == 5]['DeliveryTime'])
Vendor5_fraction=Vendor5_late/Vendor5_total
Vendor8_late=len(df[df['Vendor'] == 8]['DeliveryTime'][df[df['Vendor'] == 8]['DeliveryTime'] < 0])
Vendor8_total=len(df[df['Vendor'] == 8]['DeliveryTime'])
Vendor8_fraction=Vendor8_late/Vendor8_total

fig1 = go.Figure(data=[
    go.Bar(name='Vendor1', x=['No. of late deliveries (Comparison between top 4 vendors)','Total deliveries (Comparison between top4 vendors)'], y=[Vendor1_late,Vendor1_total]),
    go.Bar(name='Vendor2', x=['No. of late deliveries (Comparison between top 4 vendors)','Total deliveries (Comparison between top4 vendors)'], y=[Vendor2_late,Vendor2_total]),
    go.Bar(name='Vendor5', x=['No. of late deliveries (Comparison between top 4 vendors)','Total deliveries (Comparison between top4 vendors)'], y=[Vendor5_late,Vendor5_total]),
    go.Bar(name='Vendor8', x=['No. of late deliveries (Comparison between top 4 vendors)','Total deliveries (Comparison between top4 vendors)'], y=[Vendor8_late,Vendor8_total])
])
fig1.update_layout(barmode='group',paper_bgcolor="LightSteelBlue")
fig1.show(renderer="colab")

fig2 = go.Figure(data=[
    go.Bar(name='Vendor1', x=['Fraction of late-deliveries (Comparison between top4 vendors)'], y=[Vendor1_fraction]),
    go.Bar(name='Vendor2', x=['Fraction of late-deliveries (Comparison between top4 vendors)'], y=[Vendor2_fraction]),
    go.Bar(name='Vendor5', x=['Fraction of late-deliveries (Comparison between top4 vendors)'], y=[Vendor5_fraction]),
    go.Bar(name='Vendor8', x=['Fraction of late-deliveries (Comparison between top4 vendors)'], y=[Vendor8_fraction])
])
fig2.update_layout(barmode='group',paper_bgcolor="LightSteelBlue")
fig2.show(renderer="colab")

plt.figure(figsize = (20,7))
sns.distplot(df[df['Vendor'] == 1]['DeliveryTime'], kde = False, color = 'r') #1
sns.distplot(df[df['Vendor'] == 2]['DeliveryTime'], kde = False, color = 'b')  #2
sns.distplot(df[df['Vendor'] == 5]['DeliveryTime'], kde = False, color = 'g')  #3
sns.distplot(df[df['Vendor'] == 8]['DeliveryTime'], kde = False, color = 'y') #4 #worst

vendorID,count=np.unique(df[df['RemainingQuantity'] < 0]['Vendor'], return_counts = True)
# number of occurences of vendors where the quantities are delivered less then demanded
# 1 -> 43
# 2 -> 6
# 5 -> 4
# 8 -> 32
trace = go.Bar(x = ["Vendor1","Vendor2","Vendor5","Vendor8"],y=[43,6,4,32],marker=dict(color=count,colorscale='Viridis',showscale=True))
data=[trace]
#defining layout
layout = go.Layout(xaxis=dict(title='VendorID'),yaxis=dict(title='Count of top 4 Vendors with less supply '),hovermode='closest')
#defining figure and plotting
figure = go.Figure(data=data,layout=layout)
figure.update_layout(
    paper_bgcolor="LightBlue",
)
figure.show(renderer='colab')

vendor1=df[df['Vendor']==1].count()[0]
vendor2=df[df['Vendor']==2].count()[0]
vendor5=df[df['Vendor']==5].count()[0]
vendor8=df[df['Vendor']==8].count()[0]
Remaining_vendors=df[(df['Vendor']!=1) & (df['Vendor']!=2) & (df['Vendor']!=5) & (df['Vendor']!=8)].count()[0]

trace = go.Bar(x = ["Vendor1","Vendor2","Vendor5","Vendor8","Remaining_Vendors"],y=[vendor1,vendor2,vendor5,vendor8,Remaining_vendors],marker=dict(color=[vendor1,vendor2,vendor5,vendor8,Remaining_vendors],colorscale='Viridis',showscale=True))
data=[trace]
#defining layout
layout = go.Layout(xaxis=dict(title='VendorID'),yaxis=dict(title='Top 4 vendors Vs Remaining_Vendors '),hovermode='closest')
#defining figure and plotting
figure = go.Figure(data=data,layout=layout)
figure.update_layout(
    paper_bgcolor="Turquoise",
)
figure.show(renderer='colab')

fig = px.scatter(df, x="PercentOfQuantityReceived", color="Vendor",
                  hover_data=['Vendor'])
fig.update_layout(
    paper_bgcolor="LightBlue",
)
fig.show(renderer='colab')

fig = px.scatter(df, x="PercentOfQuantityReceived", color="Vendor",
                  hover_data=['Vendor'])
fig.update_layout(
    paper_bgcolor="LightSteelBlue",
)
fig.show(renderer='colab')

fig = px.scatter(df, x="DeliveryTime", color="Vendor",
                  hover_data=['Vendor'])
fig.update_layout(
    paper_bgcolor="Turquoise",
)
fig.show(renderer='colab')

for i in range(df['DeliveryTime'].shape[0]):
    if((df["DeliveryTime"].iloc[i]>0) and (df["DeliveryTime"].iloc[i]<=3)):
        df["DeliveryTime"].iloc[i]=np.log(df["DeliveryTime"].iloc[i])
df['DeliveryTime'] = [x/10 if x>0 else x for x in df.DeliveryTime]

df['NormDeliveryTime'] = 0-df.DeliveryTime.abs()
from sklearn.preprocessing import MinMaxScaler
scale = MinMaxScaler()
df['NormDeliveryTime'] = scale.fit_transform(df[['NormDeliveryTime']])
fig = px.scatter(df, x="NormDeliveryTime", color="Vendor",
                  hover_data=['Vendor'])
fig.update_layout(
    paper_bgcolor="LightBlue",
)
fig.show(renderer='colab')

df.head()

df.info()

df['PercentKept'] = 1-df.PercentOfQuantityReturned
df.head()

import datetime as dt

df['ReceivedMonth'] = df['ReceivedDate'].dt.month
df['ReceivedYear'] = df['ReceivedDate'].dt.year


grouped_monthly = df.groupby(['ReceivedYear', 
                              'ReceivedMonth', 
                              'Vendor']).agg(MonthlyNormDeliveryTime = pd.NamedAgg(column = 'NormDeliveryTime', 
                                                                                   aggfunc='mean'), 
                                             MonthlyPercentReceived = pd.NamedAgg(column = 'PercentOfQuantityReceived', 
                                                                                   aggfunc='mean'), 
                                             MonthlyPercentKept = pd.NamedAgg(column = 'PercentKept', 
                                                                                  aggfunc='mean'), 
                                             VendorId = pd.NamedAgg(column = 'Vendor', 
                                                                                  aggfunc='first'))
grouped_monthly.head(60)

import numpy as np
from numpy import linalg as LA

def Rater(Alternatives):
  length=Alternatives.shape[0]
  matrix=np.ones((length,length))
  for i in range(length):
      if(Alternatives[i]==0):
        Alternatives[i]=0.000000001    #Columns with zero value aren't acceptable in AHP algo ; So just assigned it a close to zero value
      div_array=Alternatives/Alternatives[i]
      for k in range(length):
          matrix[k][i]=div_array[k]
          
  return matrix
    
def Weight(matrix):
  eigen_v,eigen_vec=LA.eig(matrix)
  eigen_v=np.real(eigen_v)
  eigen_vec=np.real(eigen_vec)
  index=np.argmax(eigen_v)
  weight_arr=eigen_vec[:,index]/eigen_vec[:,index].sum()
  return np.abs(weight_arr)

def main(matrix):
    
    criteria=np.array([[1,2,0.5],[0.5,1,1/3],[2,3,1]]) #Need to ask mam about this factors
    w,v=LA.eig(criteria)
    w=np.real(w)
    v=np.real(v)
    
    index=np.argmax(w)
    matrix_b=v[:,index]/v[:,index].sum()
    matrix_b=matrix_b.reshape(-1,1)
    
    
    matrix_1=Rater(matrix[:,0])
    matrix_2=Rater(matrix[:,1])
    matrix_3=Rater(matrix[:,2])
    weight_1=Weight(matrix_1).reshape(-1,1)
    weight_2=Weight(matrix_2).reshape(-1,1)
    weight_3=Weight(matrix_3).reshape(-1,1)
    
    
    matrix_a=np.concatenate((weight_1,weight_2,weight_3),axis=1)
    
    return matrix_a.dot(matrix_b)

Rating_df = df.groupby(['ReceivedYear', 'ReceivedMonth', 'Vendor']).agg(MonthlyNormDeliveryTime = pd.NamedAgg(column = 'NormDeliveryTime', aggfunc='mean'), MonthlyPercentReceived = pd.NamedAgg(column = 'PercentOfQuantityReceived', aggfunc='mean'), MonthlyPercentKept = pd.NamedAgg(column = 'PercentKept', aggfunc='mean'),AHP_Score = pd.NamedAgg(column = 'Vendor', aggfunc='first'),Vendor_Monthly_Score=pd.NamedAgg(column='Vendor',aggfunc='first') ,Month = pd.NamedAgg(column = 'ReceivedMonth', aggfunc='first'),Year = pd.NamedAgg(column = 'ReceivedYear', aggfunc='first'))
Year = Rating_df['Year'].unique()   
Month =Rating_df['Month'].unique()
Vendor=grouped_monthly['VendorId'].unique()
Vendor=np.sort(Vendor)
Month =np.sort(Month)

res = {Vendor[i]: 0 for i in range(len(Vendor))} 
print(res)


Rating_df['Year']=Rating_df['Year'].astype(int)
Rating_df['Month']=Rating_df['Month'].astype(int)

ans=None
ans1=None
for i in Year:
  for j in Month:
    matrix=np.array(Rating_df[(Rating_df['Month']==j) & (Rating_df['Year']==i)][['MonthlyNormDeliveryTime','MonthlyPercentReceived','MonthlyPercentKept']])
    temp=Rating_df[(Rating_df['Month']==j) & (Rating_df['Year']==i)]['AHP_Score']
    if(matrix.shape[0]!=0):
      part_ans=main(matrix)
      maxim=np.max(part_ans)
      ind=[i for i, j in enumerate(part_ans) if j == maxim]
      for k in ind:
          wy=res[temp[k]]+1
          res[temp[k]]=wy
      part_ans1=part_ans/maxim
      if ans is None:
        ans = part_ans
        ans1 = part_ans1
      else:
        ans = np.concatenate(([ans , part_ans ]), axis=0)
        ans1 = np.concatenate(([ans1 , part_ans1 ]), axis=0)

x=[]
y=[]
for key, value in res.items():
    x.append("Vendor"+str(key))
    y.append(value)
    
trace = go.Bar(x = x,y=y,marker=dict(color=y,colorscale='Viridis',showscale=True))
data=[trace]
#defining layout
layout = go.Layout(xaxis=dict(title='The count of number of times vendor had the highest score in Month'),yaxis=dict(title='count'),hovermode='closest')
#defining figure and plotting
figure = go.Figure(data=data,layout=layout)
figure.update_layout(
    paper_bgcolor="Turquoise",
)
figure.show(renderer='colab')

Rating_df['AHP_Score']=ans
Rating_df['Vendor_Monthly_Score']=ans1
Rating_df.head(60)

from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
X=Rating_df[['MonthlyNormDeliveryTime',	'MonthlyPercentReceived',	'MonthlyPercentKept']]
y=Rating_df['Vendor_Monthly_Score']
X_train, X_test, y_train, y_test = train_test_split(X,y )
model = XGBRegressor()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
r2_score(y_test,predictions)

rating = RandomForestRegressor(n_estimators=200,max_depth=5, random_state=0)
rating.fit(Rating_df[['MonthlyNormDeliveryTime',	'MonthlyPercentReceived',	'MonthlyPercentKept']],Rating_df['Vendor_Monthly_Score'])

rating.score(Rating_df[['MonthlyNormDeliveryTime',	'MonthlyPercentReceived',	'MonthlyPercentKept']],Rating_df['Vendor_Monthly_Score'])

fig4 = px.scatter_3d(grouped_monthly, x='MonthlyPercentReceived', y='MonthlyNormDeliveryTime', z='MonthlyPercentKept',
                     color='VendorId')
fig4.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="LightBlue",
)
fig4.show(renderer='colab')

"""*Categorization* of orders into performing and non-performing along with the reason. (Promptness, Quantity, Quality)"""

from sklearn.cluster import KMeans
cls = KMeans(n_clusters = 4)
cls_assignment = cls.fit_predict(grouped_monthly[['MonthlyPercentReceived',
                                                  'MonthlyNormDeliveryTime',
                                                  'MonthlyPercentKept']])
grouped_monthly['label'] = cls_assignment

trace1=go.Scatter3d(
    x=grouped_monthly[grouped_monthly['label']==0]['MonthlyPercentReceived'],
    y=grouped_monthly[grouped_monthly['label']==0]['MonthlyNormDeliveryTime'],
    z=grouped_monthly[grouped_monthly['label']==0]['MonthlyPercentKept'],
    mode='markers',
    marker=dict(
        size=12,
        color='red',                # set color to an array/list of desired values
        colorscale='Viridis',   # choose a colorscale
        opacity=0.8
    ),
     hovertemplate= '<b>Quantity</b>: %{x:.2f}' +
                        '<br><b>Promptness</b>: %{y}<br>' +
                        '<b>Quality</b> : %{z}',
    name="Performing-Vendors"
)
layout = go.Layout(scene = dict(
                    xaxis_title='Quantity',
                    yaxis_title='Promptness',
                    zaxis_title='Quality'))
trace2=go.Scatter3d(
    x=grouped_monthly[grouped_monthly['label']==1]['MonthlyPercentReceived'],
    y=grouped_monthly[grouped_monthly['label']==1]['MonthlyNormDeliveryTime'],
    z=grouped_monthly[grouped_monthly['label']==1]['MonthlyPercentKept'],
    mode='markers',
    marker=dict(
        size=12,
        color='yellow',                # set color to an array/list of desired values
        colorscale='Viridis',   # choose a colorscale
        opacity=0.8
    ),
    hovertemplate= '<b>Quantity</b>: %{x:.2f}' +
                        '<br><b>Promptness</b>: %{y}<br>' +
                        '<b>Quality</b> : %{z}',
    name="Non-Performing-Vendors(Due to Quantity issue)"
)
trace3=go.Scatter3d(
    x=grouped_monthly[grouped_monthly['label']==2]['MonthlyPercentReceived'],
    y=grouped_monthly[grouped_monthly['label']==2]['MonthlyNormDeliveryTime'],
    z=grouped_monthly[grouped_monthly['label']==2]['MonthlyPercentKept'],
    mode='markers',
    marker=dict(
        size=12,
        color='blue',                # set color to an array/list of desired values
        colorscale='Viridis',   # choose a colorscale
        opacity=0.8
    ),
    hovertemplate= '<b>Quantity</b>: %{x:.2f}' +
                        '<br><b>Promptness</b>: %{y}<br>' +
                        '<b>Quality</b> : %{z}',
    name="Non-Performing-Vendors(Due to Quality issue)"
)
trace4 =go.Scatter3d(
    x=grouped_monthly[grouped_monthly['label']==3]['MonthlyPercentReceived'],
    y=grouped_monthly[grouped_monthly['label']==3]['MonthlyNormDeliveryTime'],
    z=grouped_monthly[grouped_monthly['label']==3]['MonthlyPercentKept'],
    mode='markers',
    marker=dict(
        size=12,
        color='green',                # set color to an array/list of desired values
        colorscale='Viridis',   # choose a colorscale
        opacity=0.8
    ),
    hovertemplate= '<b>Quantity</b>: %{x:.2f}' +
                        '<br><b>Promptness</b>: %{y}<br>' +
                        '<b>Quality</b> : %{z}',
    name="Non-Performing-Vendors(Due to Promptness issue)"
)
data=[trace1,trace2,trace3,trace4]


fig2 = go.Figure(data,layout)

fig2.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="LightBlue",
)
fig2.show(renderer='colab')

grouped = grouped_monthly.groupby("VendorId")
vendor_output = pd.DataFrame(columns=['Vendor_ID', 'Performance', 'Performance_Percent','UnderPerformance (Quality)', 'UnderPerformance (Quantity)', 'UnderPerformance (Promptness)'])
for name, group in grouped:
    values = group['label'].value_counts()
    values1 = values
    for i in range(0,4):
        if i not in values1.index:
            values1[i] = 0
    total = np.sum(group['label'].value_counts())

    for i,value in enumerate(values):
        values1[values[values == value].index] = value/total

    maxperc_index = values1[values1 == np.max(values1)].index[0]
    mydict = {0:'Performing', 1: 'Quality Issue', 2: 'Quantity Issue', 3: 'Promptness Issue'}
    
    if maxperc_index == 0 and values1[maxperc_index] < 0.75:
            maxperc_index = values1.sort()[-2].index[0]
    
    vendor_output = vendor_output.append({'Vendor_ID': group['VendorId'][group['VendorId'].first_valid_index()],'Performance': mydict[maxperc_index], 'Performance_Percent': values1[0],'UnderPerformance (Quantity)': values1[2],'UnderPerformance (Promptness)' : values1[3], 'UnderPerformance (Quality)': values1[1]}, ignore_index=True)
vendor_output

distortions = []
K = range(1,10)
for k in K:
    kmeanModel = KMeans(n_clusters=k)
    kmeanModel.fit(grouped_monthly[['MonthlyPercentReceived','MonthlyNormDeliveryTime','MonthlyPercentKept']])
    distortions.append(kmeanModel.inertia_)
plt.figure(figsize=(7,6))
plt.plot(K, distortions)
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k')
plt.show()#curve straightens out at 4, so optimal =4

count1 = vendor_output['Performance'].value_counts()[0]
count2 = vendor_output['Performance'].value_counts()[1]
count3 = vendor_output['Performance'].value_counts()[2]
count4 = 0

label=["Performing_vendors","Non-Performing_vendors_Promptness","Non-Performing_vendor_Quality","Non-Performing_vendors_Quantity"]
trace = go.Bar(x = label,y=[count1,count2,count3,count4],marker=dict(color=[count1,count2,count3,count4],colorscale='Viridis',showscale=True))
data=[trace]
#defining layout
layout = go.Layout(xaxis=dict(title='Clustering-Output'),yaxis=dict(title='Count'),hovermode='closest')
#defining figure and plotting
figure = go.Figure(data=data,layout=layout)
figure.show(renderer='colab')

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
X = grouped_monthly[['MonthlyPercentReceived','MonthlyNormDeliveryTime','MonthlyPercentKept']]
y = grouped_monthly['label']
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix , accuracy_score, classification_report
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
clf.fit(X_train,y_train)
print(pd.Series(clf.predict(X)).value_counts())
print(grouped_monthly.label.value_counts())
clf.score(X_train,y_train),clf.score(X_test,y_test)
pred = clf.predict(X_test)
results = confusion_matrix(y_test, pred) 
print('Confusion Matrix :')
print(results) 
print('Accuracy Score :',accuracy_score(y_test, pred)) 
print('Report : ')
print(classification_report(y_test, pred))

!setup.py