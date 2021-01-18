import plotly.graph_objs as go
import plotly.offline as ply

trace2 = go.Scatter(
    x=['Spain', 'Brazil','Thailand', 'London', 'India','US','China', 'Rusia'],
    y=[2001,2255,1212,1498,1791,1028,1990,646]
)


data2 = [trace2]

layout2 = dict(title='Word Count & Newspaper BEFORE Filter',
              xaxis=dict(title='Newspaper Country'),
              yaxis=dict(title='Word Count'),
)

fig2 = dict(data=data2, layout=layout2)


ply.plot(fig2, filename='countWord2.html')