#!/usr/bin/env python
# coding: utf-8

# In[1]:


#홈페이지 제작 연습


# In[2]:


import pandas as pd
import numpy as np

import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State

import plotly.graph_objects as go
from plotly.colors import DEFAULT_PLOTLY_COLORS


# In[3]:


# 데이터 호출
df = pd.read_csv('C:/Users/ray77/OneDrive/바탕 화면/과제/2-2/데이터마이닝/metro_data_2021_1_rank.csv', encoding = 'euc-kr')
df2 = df.sort_values(by='공교육만족점수',ascending=False)


# In[4]:


trace1 = go.Bar(
    x=df2['도시'],
    y=df2['공교육만족점수'],
    name='공교육 평가 점수',
    orientation='v'
)

data = [trace1]

layout = go.Layout(title = '광역시별 공교육 만족도',
barmode = 'group',
 yaxis=dict(range=[290, 325]))


fig1 = go.Figure(data, layout)
fig1.show()


# In[5]:


df3 = df.sort_values(by='21년 재정자립도(%)',ascending=False)


# In[7]:


trace1 = go.Bar(
x = df3['도시'],
y = df3['21년 재정자립도(%)'],
name = '21년 재정자립도(%)', 
orientation = 'v')


data = [trace1]

layout = go.Layout(title = '광역시별 경제지표(21년 재정자립도)',
barmode = 'group')


fig2 = go.Figure(data, layout)
fig2.show()


# In[8]:


app = dash.Dash(__name__) # app 정의
app.title = ('데이터마이닝 웹페이지 프로토타입 1호기')

server = app.server

app.layout = html.Div([
 html.H2('데이터마이닝 웹페이지 프로토타입 1호기',
            style={'textAlign': 'center', 'marginBottom': 10, 'marginTop': 10}),
    
    # Two charts arranged horizontally
    html.Div([
        # First chart (60% width)
        html.Div([
            dcc.Graph(
                id='bar-chart-1',
                figure=fig1
            ),
        ], style={'width': '60%', 'display': 'inline-block'}),
        
        # Second chart (40% width)
        html.Div([
            dcc.Graph(
                id='bar-chart-2',
                figure=fig2
            ),
        ], style={'width': '40%', 'display': 'inline-block'}),
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)


# In[ ]:




