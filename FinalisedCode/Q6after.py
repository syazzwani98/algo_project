import plotly.graph_objs as go
import plotly.offline as ply

trace1 = go.Scatter(
    x=['Spain', 'Brazil','Thailand', 'London', 'India','US','China', 'Rusia'],
    y=[538,548,388,516,778,361,700,295]
)

data = [trace1]


layout = dict(title='Word Count & Newspaper After Filter',
              xaxis=dict(title='Newspaper Country'),
              yaxis=dict(title='Word Count'),
              )



fig = dict(data=data, layout=layout)


ply.plot(fig, filename='countWord.html')