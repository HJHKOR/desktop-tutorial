#!/usr/bin/env python
# coding: utf-8

# In[126]:


import pandas as pd
import numpy as np

import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State

import plotly.graph_objects as go
from plotly.colors import DEFAULT_PLOTLY_COLORS


# In[127]:


df = pd.read_csv('C:/Users/ray77/OneDrive/바탕 화면/종합데이터/데마종합데이터1.csv', encoding = 'euc-kr')
df


# In[128]:


#fig1	교육, 인프라	공교육 만족도

df1 = df.sort_values(by='공교육만족점수', ascending=False)

trace1 = go.Bar(
    x=df1['도시'],
    y=df1['공교육만족점수'],
    name='공교육 평가 점수',
    orientation='v')

data = [trace1]

layout = go.Layout(
    title='광역시별 공교육 만족도',
    yaxis=dict(range=[290, 325]),
    annotations=[
        dict(
            x=0.5,
            y=1.15,  # Adjust the y value to move the subtitle below the title
            xref='paper',
            yref='paper',
            text='개인마다 격차가 발생할 수 있는 사교육 대신 모두가 공평하게 받는 <br> 공교육 만족도가 해당 도시의 교육의 질을 나타낼 수 있음.', 
            showarrow=False,
            font=dict(size=12)
        )
    ]
)

fig1 = go.Figure(data, layout)
fig1.show()


# In[129]:


#fig2	교육, 인프라	공공문화시설만족도

df2=df.sort_values(by='공공문화여가시설만족도',ascending=False)

trace = go.Bar(
    x=df2['도시'],
    y=df2['공공문화여가시설만족도']
)

data = [trace]

layout = go.Layout(
    title='광역시별 공공문화여가시설 서비스 만족도',
    yaxis=dict(range=[400, 453]),
    annotations=[
        dict(
            x=0.5,
            y=1.15,  # Adjust the y value to move the subtitle below the title
            xref='paper',
            yref='paper',
            text='여가 및 문화시설은 도시민의 삶의 질과 만족도를 높여 삶을 풍요롭게 만들',  # Add your subtitle here
            showarrow=False,
            font=dict(size=12)
        )
    ]
)

fig2=go.Figure(data, layout)
fig2.show()


# In[130]:


#fig3	교육, 인프라	종합

df3=df.sort_values(by='교육인프라점수합산',ascending=False)

trace=go.Bar(
    x=df3['도시'],
    y=df3['교육인프라점수합산'],
    marker=dict(color='#636EFB'))
    
data=[trace]
    
layout = go.Layout(
    title='광역시별 교육,인프라 점수 총합',
    annotations=[
        dict(
            x=0.5,
            y=1.15,  # Fixing y value to consistently position the subtitle below the title
            xref='paper',
            yref='paper',
            text='각 분야별 순위로<br>1등: 6점. 2등: 5점, 3등: 4점, 4등: 3점. 5등: 2점, 6등: 1점을 배정 후 합산',  # Add your subtitle here
            showarrow=False,
            font=dict(size=12)
        )
    ]
)

fig3 = go.Figure(data, layout)
fig3.show()


# In[131]:


#fig4	경제	재정자립도

df4 = df.sort_values(by='재정자립도', ascending=False)

trace = go.Bar(
    x=df4['도시'],
    y=df4['재정자립도'],
    marker=dict(color='#EF553B')
)

data = [trace]

layout = go.Layout(
    title='광역시별 재정자립도',
    yaxis=dict(range=[35, 55]),
    annotations=[
        dict(
            x=0.5,
            y=1.15,  # Fixing y value to consistently position the subtitle below the title
            xref='paper',
            yref='paper',
            text='중앙정부 지원 예산과 시 자체 충당예산의 비율로 해당 도시의 재원이 건강한지 나타내는 지표',  # Add your subtitle here
            showarrow=False,
            font=dict(size=12)
        )
    ]
)

fig4 = go.Figure(data, layout)
fig4.show()


# In[132]:


#fig5	경제	소비자 물가 지수

df5 = df.sort_values(by='소비자물가지수', ascending=True)

trace = go.Bar(
    x=df5['도시'],
    y=df5['소비자물가지수'],
    marker=dict(color='#EF553B')
)

data = [trace]

layout = go.Layout(
    title='광역시별 소비자물가지수 (20년~23년)',
    yaxis=dict(range=[110, 115]),
    annotations=[
        dict(
            x=0.5,
            y=1.15,  # Fixing y value to consistently position the subtitle below the title
            xref='paper',
            yref='paper',
            text='기준이 되는 해의 물품가를 100으로 놓고 비교시점의 물가수준이 얼마나 되는가를 상대적인 크기로 표시한 것',  # Add your subtitle here
            showarrow=False,
            font=dict(size=12)
        )
    ]
)

fig5 = go.Figure(data, layout)
fig5.show()


# In[133]:


#fig6	경제	종합
df6 = df.sort_values(by='경제점수합산', ascending=False)

trace = go.Bar(
    x=df6['도시'],
    y=df6['경제점수합산'],
    marker=dict(color='#EF553B'))

data = [trace]

layout = go.Layout(
    title='광역시별 경제 점수 총합',
    annotations=[
        dict(
            x=0.5,
            y=1.15,  # Fixing y value to consistently position the subtitle below the title
            xref='paper',
            yref='paper',
            text='각 분야별 순위로 <br> 1등: 6점. 2등: 5점, 3등: 4점, 4등: 3점. 5등: 2점, 6등: 1점을 배정 후 합산',  # Add your subtitle here
            showarrow=False,
            font=dict(size=12)
        )
    ]
)

fig6 = go.Figure(data, layout)
fig6.show()


# In[134]:


#fig7	교통	대중교통 접근시간

df7 = df.sort_values(by='대중교통접근시간', ascending=False)

trace = go.Bar(
    x=df7['도시'],
    y=df7['대중교통접근시간'],
    marker=dict(color='#00CC96')
)

data = [trace]

layout = go.Layout(
    title='광역시별 대중교통접근시간',
    yaxis=dict(range=[15, 23]),
    annotations=[
        dict(
            x=0.5,
            y=1.15,  # Fixing y value to consistently position the subtitle below the title
            xref='paper',
            yref='paper',
            text='대중교통 서비스를 편하게 누리는 것은 접근성과 삶의 질에 중요',  # Add your subtitle here
            showarrow=False,
            font=dict(size=12)
        )
    ]
)

fig7 = go.Figure(data, layout)
fig7.show()


# In[135]:


#fig8	교통	도로포장률

df8 = df.sort_values(by='도로포장률', ascending=False)

trace = go.Bar(
    x=df8['도시'],
    y=df8['도로포장률'],
    marker=dict(color='#00CC96')
)

data = [trace]

layout = go.Layout(
    title='광역시별 도로포장률',
    yaxis=dict(range=[95, 100]),
    annotations=[
        dict(
            x=0.5,
            y=1.15,  # Fixing y value to consistently position the subtitle below the title
            xref='paper',
            yref='paper',
            text='낮은 도로 포장률은 지역 발전의 저해 요소로 꼽히고 있으며<br> 잘 정비된 도로는 통행에 큰 도움',  # Add your subtitle here
            showarrow=False,
            font=dict(size=12)
        )
    ]
)

fig8 = go.Figure(data, layout)
fig8.show()


# In[136]:


#fig9	교통	종합

df9=df.sort_values(by='교통점수합산',ascending=False)

trace=go.Bar(
    x=df9['도시'],
    y=df9['교통점수합산'],
    marker=dict(color='#00CC96'))
    
data=[trace]
    
layout = go.Layout(
    title='광역시별 교통 점수 종합',
    annotations=[
        dict(
            x=0.5,
            y=1.15,  # Fixing y value to consistently position the subtitle below the title
            xref='paper',
            yref='paper',
            text='각 분야별 순위로 <br> 1등: 6점. 2등: 5점, 3등: 4점, 4등: 3점. 5등: 2점, 6등: 1점을 배정 후 합산',  # Add your subtitle here
            showarrow=False,
            font=dict(size=12)
        )
    ]
)

fig9=go.Figure(data, layout)
fig9.show()


# In[137]:


#fig10	보건	응급실도착시간

df10 = df.sort_values(by='응급실도착시간', ascending=True)

trace = go.Bar(
    x=df10['도시'],
    y=df10['응급실도착시간'],
    marker=dict(color='#AB63FA')
)

data = [trace]

layout = go.Layout(
    title='광역시별 응급실도착시간',
    annotations=[
        dict(
            x=0.5,
            y=1.15,  # Fixing y value to consistently position the subtitle below the title
            xref='paper',
            yref='paper',
            text=' 의료기관의 접근성을 알아보기 위해 건수를 시간대로 나누어 가중치를 부과한 후<br>건수만큼 평균을 낸 응급실도착시간을 산출',  # Add your subtitle here
            showarrow=False,
            font=dict(size=12)
        )
    ]
)

fig10 = go.Figure(data, layout)
fig10.show()


# In[138]:


#fig11	보건	의사수

df11=df.sort_values(by='면적당병상수',ascending=False)

trace=go.Bar(
    x=df11['도시'],
    y=df11['면적당병상수'],
    marker=dict(color='#AB63FA')
    )
    
data=[trace]
    
layout=go.Layout(
    title='광역시별 면적당병상수',
    annotations=[
        dict(
            x=0.5,
            y=1.15,  # Fixing y value to consistently position the subtitle below the title
            xref='paper',
            yref='paper',
            text='병원 규모의 척도는 병상수로 병상수에 면적을 나눈 값',  # Add your subtitle here
            showarrow=False,
            font=dict(size=12)                 
                )]
)

fig11=go.Figure(data, layout)
fig11.show()


# In[139]:


#fig12	보건	종합

df12=df.sort_values(by='보건점수합산',ascending=False)

trace=go.Bar(
    x=df12['도시'],
    y=df12['보건점수합산'],
    marker=dict(color='#AB63FA'))
    
data=[trace]
    
layout = go.Layout(
    title='광역시별 보건 점수 종합',
    annotations=[
        dict(
            x=0.5,
            y=1.15,  # Fixing y value to consistently position the subtitle below the title
            xref='paper',
            yref='paper',
            text='각 분야별 순위로 <br> 1등: 6점. 2등: 5점, 3등: 4점, 4등: 3점. 5등: 2점, 6등: 1점을 배정 후 합산',  # Add your subtitle here
            showarrow=False,
            font=dict(size=12)
        )
    ]
)

fig12=go.Figure(data, layout)
fig12.show()


# In[140]:


#fig13	치안	범죄율

df13=df.sort_values(by='범죄율',ascending=True)

trace=go.Bar(
    x=df13['도시'],
    y=df13['범죄율'],
 marker=dict(color='#FFA15A'))
    
data=[trace]
    
layout=go.Layout(title='광역시별 범죄율',
                    annotations=[
        dict(
            x=0.5,
            y=1.15,  # Fixing y value to consistently position the subtitle below the title
            xref='paper',
            yref='paper',
            text='지역의 평균적인 준법의식을 파악하기 위해<br>범죄발생건수에 지역 전체 인구를 나눈 값',  # Add your subtitle here
            showarrow=False,
            font=dict(size=12))])

fig13=go.Figure(data, layout)
fig13.show()


# In[141]:


#fig14	치안	경찰관서수

df14=df.sort_values(by='면적당경찰관서수',ascending=False)

trace=go.Bar(
    x=df14['도시'],
    y=df14['면적당경찰관서수'],
 marker=dict(color='#FFA15A'))
    
data=[trace]
    
layout=go.Layout(title='광역시별 면적당경찰관서수',
                                    annotations=[
        dict(
            x=0.5,
            y=1.15,  # Fixing y value to consistently position the subtitle below the title
            xref='paper',
            yref='paper',
            text='경찰관서 1개소가 담당하는 지역의 면적을 확인함으로써 치안공백의 여부를 파악',  # Add your subtitle here
            showarrow=False,
            font=dict(size=12))])

fig14=go.Figure(data, layout)
fig14.show()


# In[142]:


#fig15	치안	종합
df15=df.sort_values(by='치안점수합산',ascending=False)

trace=go.Bar(
    x=df15['도시'],
    y=df15['치안점수합산'],
    marker=dict(color='#FFA15A'))
    
data=[trace]
    
layout = go.Layout(
    title='광역시별 치안 점수 종합',
    annotations=[
        dict(
            x=0.5,
            y=1.15,  # Fixing y value to consistently position the subtitle below the title
            xref='paper',
            yref='paper',
            text='각 분야별 순위로 <br> 1등: 6점. 2등: 5점, 3등: 4점, 4등: 3점. 5등: 2점, 6등: 1점을 배정 후 합산',  # Add your subtitle here
            showarrow=False,
            font=dict(size=12)
        )
    ]
)

fig15=go.Figure(data, layout)
fig15.show()


# In[143]:


#fig16	환경	대기오염물질 배출량

df16=df.sort_values(by='대기오염물질배출량',ascending=True)

trace=go.Bar(
    x=df16['도시'],
    y=df16['대기오염물질배출량'],
marker=dict(color='#1BD3F3'))
    
data=[trace]
    
layout=go.Layout(title='광역시별 대기오염물질배출량',
                                    annotations=[
        dict(
            x=0.5,
            y=1.15,  # Fixing y value to consistently position the subtitle below the title
            xref='paper',
            yref='paper',
            text='정주에 적합한 쾌적한 환경을 가진 지역을 확인하기 위해<br>총 대기오염물질 배출량을 합산',  # Add your subtitle here
            showarrow=False,
            font=dict(size=12))])

fig16=go.Figure(data, layout)
fig16.show()


# In[144]:


#fig17	환경	종합

df17=df.sort_values(by='환경점수합산',ascending=False)

trace=go.Bar(
    x=df17['도시'],
    y=df17['환경점수합산'],
    marker=dict(color='#1BD3F3'))
    
data=[trace]
    
layout = go.Layout(
    title='광역시별 환경 점수 종합',
    annotations=[
        dict(
            x=0.5,
            y=1.15,  # Fixing y value to consistently position the subtitle below the title
            xref='paper',
            yref='paper',
            text='각 분야별 순위로 <br> 1등: 6점. 2등: 5점, 3등: 4점, 4등: 3점. 5등: 2점, 6등: 1점을 배정 후 합산',  # Add your subtitle here
            showarrow=False,
            font=dict(size=12)
        )
    ]
)

fig17=go.Figure(data, layout)
fig17.show()


# In[145]:


import plotly.express as px

file11=pd.read_csv("C:/Users/ray77/OneDrive/바탕 화면/종합데이터/11점수합산.csv", encoding='euc-kr')
df18=file11.sort_values(by='합계',ascending=True)


fig18 = px.bar(df18, y="도시", x=['교육,인프라', '교통', '경제','범죄','환경','보건'], title="점수 합산", orientation='h')
fig18.show()


# In[146]:


#fig19	종합순위 2

file22=pd.read_csv("C:/Users/ray77/OneDrive/바탕 화면/종합데이터/가보자점수최종11세로.csv", encoding='euc-kr')

fig19 = px.bar(file22, x="도시", y="점수", color="도시", title="분야별 점수",
  animation_frame="분류", animation_group="도시", range_y=[0,45])
fig19.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 1000
fig19.show()


# In[147]:


#fig 1
import plotly.graph_objects as go
import plotly.express as px

import geopandas as gpd
gdf = gpd.read_file("C:/Users/ray77/OneDrive/바탕 화면/종합데이터/Z_NGII_N3A_G0010000.shp",)
gdf.to_crs(4326)
gdf1 = gdf.loc[[4,5,6,7,10,11]]
gdf2 =gdf1[['NAME','geometry']]


# In[149]:


qq = pd.read_csv("C:/Users/ray77/OneDrive/바탕 화면/종합데이터/데마종합데이터2.csv",encoding = 'euc-kr')
qqq = qq.loc[:]
geo = gdf2.merge(qqq, left_on = 'NAME',right_on = '도시',how = 'inner').to_crs(epsg = 4326)
geo.to_csv("C:/Users/ray77/OneDrive/바탕 화면/종합데이터/geo.csv")


# In[168]:


#map_group1
# Create a bar trace for the chart
bar_trace = go.Scattermapbox(
    lat=geo['geometry'].centroid.y,
    lon=geo['geometry'].centroid.x,
    mode='markers',
    marker=dict(
        size=geo['교육인프라점수합산'] * 6,  # Adjust the size by multiplying with a scaling factor
        colorscale="jet",
        color=geo['교육인프라점수합산'],
        colorbar=dict(title='교육인프라점수합산'),
    ),
    text=geo['교육인프라점수합산'],
)

# Create the figure
map_group1 = go.Figure()

# Add the bar trace to the figure
map_group1.add_trace(bar_trace)

# Update the layout to use mapbox
map_group1.update_layout(
    mapbox=dict(
        style="carto-positron",
        center=dict(lon=geo['geometry'].centroid.x.mean(), lat=geo['geometry'].centroid.y.mean()),
        zoom=4,
    ),
)

# Update the layout to add a legend
map_group1.update_layout(
    legend=dict(
        title=dict(text='교육인프라점수합산'),
        itemsizing='constant',  # Ensure constant item size
        itemwidth=30,  # Set the width of legend item symbols
    )
)

# Update the layout to adjust coloraxis
map_group1.update_layout(
    coloraxis=dict(
        colorbar=dict(title='교육인프라점수합산'),
        colorscale="pubu",
    )
)

# Show the figure
map_group1.show()


# In[165]:


#map_group2
import plotly.graph_objects as go
import plotly.express as px

import plotly.graph_objects as go
import geopandas as gpd

# Assuming you have a GeoDataFrame named 'geo' with a '치안점수합산' column

# Create a bar trace for the chart
bar_trace = go.Scattermapbox(
    lat=geo['geometry'].centroid.y,
    lon=geo['geometry'].centroid.x,
    mode='markers',
    marker=dict(
        size=geo['경제점수합산'] * 10,  # Adjust the size by multiplying with a scaling factor
        colorscale="jet",
        color=geo['경제점수합산'],
        colorbar=dict(title='경제점수합산'),
    ),
    text=geo['경제점수합산'],
)

# Create the figure
map_group2 = go.Figure()

# Add the bar trace to the figure
map_group2.add_trace(bar_trace)

# Update the layout to use mapbox
map_group2.update_layout(
    mapbox=dict(
        style="carto-positron",
        center=dict(lon=geo['geometry'].centroid.x.mean(), lat=geo['geometry'].centroid.y.mean()),
        zoom=4,
    ),
)

# Update the layout to add a legend
map_group2.update_layout(
    legend=dict(
        title=dict(text='경제점수합산'),
        itemsizing='constant',  # Ensure constant item size
        itemwidth=30,  # Set the width of legend item symbols
    )
)

# Update the layout to adjust coloraxis
map_group2.update_layout(
    coloraxis=dict(
        colorbar=dict(title='경제점수합산'),
        colorscale="pubu",
    )
)

# Show the figure
map_group2.show()


# In[164]:


import plotly.graph_objects as go
import plotly.express as px

import plotly.graph_objects as go
import geopandas as gpd

# Assuming you have a GeoDataFrame named 'geo' with a '치안점수합산' column

# Create a bar trace for the chart
bar_trace = go.Scattermapbox(
    lat=geo['geometry'].centroid.y,
    lon=geo['geometry'].centroid.x,
    mode='markers',
    marker=dict(
        size=geo['교통점수합산'] * 10,  # Adjust the size by multiplying with a scaling factor
        colorscale="jet",
        color=geo['교통점수합산'],
        colorbar=dict(title='교통점수합산'),
    ),
    text=geo['교통점수합산'],
)

# Create the figure
map_group3 = go.Figure()

# Add the bar trace to the figure
map_group3.add_trace(bar_trace)

# Update the layout to use mapbox
map_group3.update_layout(
    mapbox=dict(
        style="carto-positron",
        center=dict(lon=geo['geometry'].centroid.x.mean(), lat=geo['geometry'].centroid.y.mean()),
        zoom=4,
    ),
)

# Update the layout to add a legend
map_group3.update_layout(
    legend=dict(
        title=dict(text='교통점수합산'),
        itemsizing='constant',  # Ensure constant item size
        itemwidth=30,  # Set the width of legend item symbols
    )
)

# Update the layout to adjust coloraxis
map_group3.update_layout(
    coloraxis=dict(
        colorbar=dict(title='교통점수합산'),
        colorscale="pubu",
    )
)

# Show the figure
map_group3.show()


# In[163]:


#map_group4
import plotly.graph_objects as go
import plotly.express as px

# geo가 GeoDataFrame이라고 가정하고 '병상수' 열이 있다고 가정합니다.
import plotly.graph_objects as go
import geopandas as gpd

# Assuming you have a GeoDataFrame named 'geo' with a '치안점수합산' column

# Create a bar trace for the chart
bar_trace = go.Scattermapbox(
    lat=geo['geometry'].centroid.y,
    lon=geo['geometry'].centroid.x,
    mode='markers',
    marker=dict(
        size=geo['보건점수합산'] * 10,  # Adjust the size by multiplying with a scaling factor
        colorscale="jet",
        color=geo['보건점수합산'],
        colorbar=dict(title='보건점수합산'),
    ),
    text=geo['보건점수합산'],
)

# Create the figure
map_group4 = go.Figure()

# Add the bar trace to the figure
map_group4.add_trace(bar_trace)

# Update the layout to use mapbox
map_group4.update_layout(
    mapbox=dict(
        style="carto-positron",
        center=dict(lon=geo['geometry'].centroid.x.mean(), lat=geo['geometry'].centroid.y.mean()),
        zoom=4,
    ),
)

# Update the layout to add a legend
map_group4.update_layout(
    legend=dict(
        title=dict(text='보건점수합산'),
        itemsizing='constant',  # Ensure constant item size
        itemwidth=30,  # Set the width of legend item symbols
    )
)

# Update the layout to adjust coloraxis
map_group4.update_layout(
    coloraxis=dict(
        colorbar=dict(title='보건점수합산'),
        colorscale="pubu",
    )
)

# Show the figure
map_group4.show()


# In[162]:


#map_group5

# Create a bar trace for the chart
import plotly.graph_objects as go
import geopandas as gpd

# Assuming you have a GeoDataFrame named 'geo' with a '치안점수합산' column

# Create a bar trace for the chart
bar_trace = go.Scattermapbox(
    lat=geo['geometry'].centroid.y,
    lon=geo['geometry'].centroid.x,
    mode='markers',
    marker=dict(
        size=geo['치안점수합산'] * 10,  # Adjust the size by multiplying with a scaling factor
        colorscale="jet",
        color=geo['치안점수합산'],
        colorbar=dict(title='치안점수합산'),
    ),
    text=geo['치안점수합산'],
)

# Create the figure
map_group5 = go.Figure()

# Add the bar trace to the figure
map_group5.add_trace(bar_trace)

# Update the layout to use mapbox
map_group5.update_layout(
    mapbox=dict(
        style="carto-positron",
        center=dict(lon=geo['geometry'].centroid.x.mean(), lat=geo['geometry'].centroid.y.mean()),
        zoom=4,
    ),
)

# Update the layout to add a legend
map_group5.update_layout(
    legend=dict(
        title=dict(text='치안점수합산'),
        itemsizing='constant',  # Ensure constant item size
        itemwidth=30,  # Set the width of legend item symbols
    )
)

# Update the layout to adjust coloraxis
map_group5.update_layout(
    coloraxis=dict(
        colorbar=dict(title='치안점수합산'),
        colorscale="pubu",
    )
)

# Show the figure
map_group5.show()


# In[158]:


import plotly.graph_objects as go
import plotly.express as px

import plotly.graph_objects as go
import geopandas as gpd

# Assuming you have a GeoDataFrame named 'geo' with a '치안점수합산' column

# Create a bar trace for the chart
bar_trace = go.Scattermapbox(
    lat=geo['geometry'].centroid.y,
    lon=geo['geometry'].centroid.x,
    mode='markers',
    marker=dict(
        size=geo['환경점수합산'] * 10,  # Adjust the size by multiplying with a scaling factor
        colorscale="jet",
        color=geo['환경점수합산'],
        colorbar=dict(title='환경점수합산'),
    ),
    text=geo['환경점수합산'],
)

# Create the figure
map_group6 = go.Figure()

# Add the bar trace to the figure
map_group6.add_trace(bar_trace)

# Update the layout to use mapbox
map_group6.update_layout(
    mapbox=dict(
        style="carto-positron",
        center=dict(lon=geo['geometry'].centroid.x.mean(), lat=geo['geometry'].centroid.y.mean()),
        zoom=4,
    ),
)

# Update the layout to add a legend
map_group6.update_layout(
    legend=dict(
        title=dict(text='환경점수합산'),
        itemsizing='constant',  # Ensure constant item size
        itemwidth=30,  # Set the width of legend item symbols
    )
)

# Update the layout to adjust coloraxis
map_group6.update_layout(
    coloraxis=dict(
        colorbar=dict(title='환경점수합산'),
        colorscale="pubu",
    )
)

# Show the figure
map_group6.show()


# In[159]:


#map_group7
import plotly.graph_objects as go
import plotly.express as px

import plotly.graph_objects as go
import geopandas as gpd

# Assuming you have a GeoDataFrame named 'geo' with a '치안점수합산' column

# Create a bar trace for the chart
bar_trace = go.Scattermapbox(
    lat=geo['geometry'].centroid.y,
    lon=geo['geometry'].centroid.x,
    mode='markers',
    marker=dict(
        size=geo['종합순위'] * 1.5,  # Adjust the size by multiplying with a scaling factor
        colorscale="jet",
        color=geo['종합순위'],
        colorbar=dict(title='종합순위'),
    ),
    text=geo['종합순위'],
)

# Create the figure
map_group7 = go.Figure()

# Add the bar trace to the figure
map_group7.add_trace(bar_trace)

# Update the layout to use mapbox
map_group7.update_layout(
    mapbox=dict(
        style="carto-positron",
        center=dict(lon=geo['geometry'].centroid.x.mean(), lat=geo['geometry'].centroid.y.mean()),
        zoom=4,
    ),
)

# Update the layout to add a legend
map_group7.update_layout(
    legend=dict(
        title=dict(text='종합순위'),
        itemsizing='constant',  # Ensure constant item size
        itemwidth=30,  # Set the width of legend item symbols
    )
)

# Update the layout to adjust coloraxis
map_group7.update_layout(
    coloraxis=dict(
        colorbar=dict(title='종합순위'),
        colorscale="pubu",
    )
)

# Show the figure
map_group7.show()


# In[169]:


import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go

# ... (your data and figures)

# Assume you have 7 figures (fig1, fig2, ..., fig7)
all_figures = [globals()[f'fig{i}'] for i in range(1, 20)]

# Extract titles from layout for dropdown labels
graph_names = [fig.layout.title.text for fig in all_figures]

# Assume you have 7 map figures (map_group1, map_group2, ..., map_group7)
all_maps = [globals()[f'map_group{i}'] if f'map_group{i}' in globals() else go.Figure() for i in range(1, 8)]

# ... (your initial map data)
initial_lat = 36
initial_lon = 128
mapbox_style = "open-street-map"
initial_zoom = 5.5

# Dash application initialization
app = dash.Dash(__name__)
app.title = '기숙사가이즈_데이터마이닝_주제발표'

# Define your title as a separate component
title_component = html.H2('분야별 광역시 현황',
                          style={'textAlign': 'center', 'marginBottom': 10, 'marginTop': 10})

# Layout setup using an html.Div container
app.layout = html.Div([
    title_component,

    html.Div([
        dcc.Dropdown(
            id='group-dropdown',
            options=[
                {'label': '교육,인프라', 'value': 1},
                {'label': '경제', 'value': 2},
                {'label': '교통', 'value': 3},
                {'label': '보건', 'value': 4},
                {'label': '치안', 'value': 5},
                {'label': '환경', 'value': 6},
                {'label': '종합순위', 'value': 7}
            ],
            value=1,
            style={'width': '50%', 'display': 'inline-block'}
        ),
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Br(),
    
    html.Div([
        # Map container
        dcc.Graph(id='map-output'),
    ], style={'width': '50%', 'display': 'inline-block', 'float': 'right', 'height': '550px'}),
    
    html.Br(),

    html.Div([
        dcc.Dropdown(
            id='group1-dropdown',
            options=[
                {'label': name, 'value': j} for j, name in enumerate(graph_names[:3], start=1)
            ],
            value=1,
            style={'width': '100%', 'display': 'inline-block'}
        ),
        dcc.Graph(id='graph-output1'),
    ], style={'width': '50%', 'display': 'none', 'float': 'left'}, id='group1-container'),

    html.Div([
        dcc.Dropdown(
            id='group2-dropdown',
            options=[
                {'label': name, 'value': j} for j, name in enumerate(graph_names[3:6], start=4)
            ],
            value=4,
            style={'width': '100%', 'display': 'inline-block', 'margin-right': '10px'}
        ),
        dcc.Graph(id='graph-output2'),
    ], style={'width': '50%', 'display': 'none', 'float': 'left'}, id='group2-container'),

    html.Div([
        dcc.Dropdown(
            id='group3-dropdown',
            options=[
                {'label': name, 'value': j} for j, name in enumerate(graph_names[6:9], start=7)
            ],
            value=7,
            style={'width': '100%', 'display': 'inline-block', 'margin-right': '10px'}
        ),
        dcc.Graph(id='graph-output3'),
    ], style={'width': '50%', 'display': 'none', 'float': 'left'}, id='group3-container'),

    html.Div([
        dcc.Dropdown(
            id='group4-dropdown',
            options=[
                {'label': name, 'value': j} for j, name in enumerate(graph_names[9:12], start=10)
            ],
            value=10,
            style={'width': '100%', 'display': 'inline-block', 'margin-right': '10px'}
        ),
        dcc.Graph(id='graph-output4'),
    ], style={'width': '50%', 'display': 'none', 'float': 'left'}, id='group4-container'),

    html.Div([
        dcc.Dropdown(
            id='group5-dropdown',
            options=[
                {'label': name, 'value': j} for j, name in enumerate(graph_names[12:15], start=13)
            ],
            value=13,
            style={'width': '100%', 'display': 'inline-block', 'margin-right': '10px'}
        ),
        dcc.Graph(id='graph-output5'),
    ], style={'width': '50%', 'display': 'none', 'float': 'left'}, id='group5-container'),

    html.Div([
        dcc.Dropdown(
            id='group6-dropdown',
            options=[
                {'label': name, 'value': j} for j, name in enumerate(graph_names[15:17], start=16)
            ],
            value=16,
            style={'width': '100%', 'display': 'inline-block', 'margin-right': '10px'}
        ),
        dcc.Graph(id='graph-output6'),
    ], style={'width': '50%', 'display': 'none', 'float': 'left'}, id='group6-container'),

    html.Div([
        dcc.Dropdown(
            id='group7-dropdown',
            options=[
                {'label': name, 'value': j} for j, name in enumerate(graph_names[17:], start=18)
            ],
            value=17,
            style={'width': '100%', 'display': 'inline-block', 'margin-right': '10px'}
        ),
        dcc.Graph(id='graph-output7'),
    ], style={'width': '50%', 'display': 'none', 'float': 'left'}, id='group7-container'),

        html.Br(),
        html.Br(),
        html.Br(),
    
    html.Div([
        html.Div([
            dcc.Graph(
                id='bar-chart-1',
                figure=fig3
            ),
        ], style={'width': '100%', 'display': 'inline-block'}),

        html.Div([
            dcc.Graph(
                id='bar-chart-2',
                figure=fig6
            ),
        ], style={'width': '100%', 'display': 'inline-block'}),

        html.Div([
            dcc.Graph(
                id='bar-chart-3',
                figure=fig9
            ),
        ], style={'width': '100%', 'display': 'inline-block'}),
        
        html.Br(),

        html.Div([
            dcc.Graph(
                id='bar-chart-4',
                figure=fig12
            ),
        ], style={'width': '100%', 'display': 'inline-block'}),

        html.Div([
            dcc.Graph(
                id='bar-chart-5',
                figure=fig15
            ),
        ], style={'width': '100%', 'display': 'inline-block'}),

        html.Div([
            dcc.Graph(
                id='bar-chart-6',
                figure=fig17
            ),
        ], style={'width': '100%', 'display': 'inline-block'}),

        html.Br(),
        
        html.Div([
            dcc.Graph(
                id='bar-chart-7',
                figure=fig18
            ),
        ], style={'width': '100%', 'display': 'inline-block'})
    ])
])

# Callback function to toggle the visibility of each group
@app.callback(
    [Output(f'group{i}-container', 'style') for i in range(1, 8)],
    [Input('group-dropdown', 'value')]
)
def toggle_group_visibility(selected_group):
    styles = [{'width': '100%', 'display': 'none'}] * 7
    styles[selected_group - 1] = {'width': '50%', 'display': 'inline-block', 'float': 'left'}
    return styles

# Callback function for updating the map
@app.callback(
    Output('map-output', 'figure'),
    [Input('group-dropdown', 'value')]
)
def update_map(selected_group):
    # Determine the index of the selected group
    group_index = selected_group - 1

    # Assume map_figures is a list containing map figures corresponding to fig(i)
    map_figure = all_maps[group_index] if group_index < len(all_maps) else go.Figure()

    # You can customize the map layout if needed
    map_figure.update_layout(
        mapbox=dict(
            center=dict(lat=initial_lat, lon=initial_lon),
            style=mapbox_style,
            zoom=initial_zoom
        ),
        showlegend=False,
        height=500,
        width=600,
        title=f'분야별 총점- {selected_group}'  # Set the title here
    )

    return map_figure

# Callback functions for updating graph outputs for each group
for i in range(1, 8):
    @app.callback(
        [Output(f'graph-output{i}', 'figure')],
        [Input(f'group{i}-dropdown', 'value')],
        [State(f'group{i}-dropdown', 'id')]
    )
    def update_content(selected_graph, dropdown_id):
        try:
            # If 'clear value' is selected, return the initial graph of the group
            if selected_graph is None and f'group{i}' in dropdown_id:
                return [all_figures[i - 1]]

            # If a specific graph is selected, return that graph
            return [all_figures[selected_graph - 1]]
        except IndexError:
            return [go.Figure()]

if __name__ == '__main__':
    app.run_server(debug=True, port=8060)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




