import plotly.graph_objs as go
import plotly.offline as ply

mapbox_access_token = 'pk.eyJ1IjoiamFzc2hhZmlxYWgiLCJhIjoiY2p3NGwxbGxhMHJlYjQ5bm1rdWw3aXE2ciJ9.dqKczbyhvAm5Dtrq6EEShQ'

data = [
    go.Scattermapbox(
        lat=['3.139003', '35.86166', '51.507351', '20.593683', '61.52401', '37.09024', '15.870032', '40.463669', '-14.235004'],
        lon=['101.686852', '104.195396', '-0.127758', '78.962883', '105.318756', '-95.712891', '100.992538', '-3.74922', '-51.925282'],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=9
        ),
        text=["Kuala Lumpur", "China", "London", "India", "Russia", "United States", "Thailand", "Spain", "Brazil"],
    ),
]
layout = go.Layout(
    autosize=True,
    hovermode='closest',
    mapbox=go.layout.Mapbox(
        accesstoken=mapbox_access_token,
    ),
    title = go.layout.Title(
        text = 'Location of All Destination for Flight System 2.0'
    ),
)


fig = dict(data=data, layout=layout)
ply.plot(fig, filename='map.html')