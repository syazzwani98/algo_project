import plotly.graph_objs as go
import plotly.offline as ply

mapbox_access_token = 'pk.eyJ1IjoiamFzc2hhZmlxYWgiLCJhIjoiY2p3NGwxbGxhMHJlYjQ5bm1rdWw3aXE2ciJ9.dqKczbyhvAm5Dtrq6EEShQ'

latA = (3.139003) # A for Kuala Lumpur,
latB = (35.86166) # B for China,
latC = (51.507351) # C for London,
latD = (20.593683) # D for India,
latE = (61.52401) # E for Russia,
latF = (37.09024) # F for United States,
latG = (15.870032) # G for Thailand,
latH = (40.463669) # H for Spain,
latI = (-14.235004) # I for Brazil,

lonA = (101.686852) # A for Kuala Lumpur,
lonB = (104.195396) # B for China,
lonC = (-0.127758) # C for London,
lonD = (78.962883) # D for India,
lonE = (105.318756) # E for Russia,
lonF = (-95.712891) # F for United States,
lonG = (100.992538) # G for Thailand,
lonH = (-3.74922) # H for Spain,
lonI = (-51.925282) # I for Brazil,

line= go.Scattermapbox(
        lat=[latA, latB, latC, latD, latE, latF, latG, latH, latI],
        lon=[lonA, lonB, lonC, lonD, lonE, lonF, lonG, lonH, lonI],
        mode = 'lines',
        marker=go.scattermapbox.Marker(
        size=9
        ),
        line = go.scattermapbox.Line(
        width = 2,
        color = 'blue',
        ),
	text=["Kuala Lumpur", "China", "London", "India", "Russia", "United States", "Thailand", "Spain", "Brazil"],
    ),
layout = go.Layout(
    autosize=True,
    hovermode='closest',
    mapbox=go.layout.Mapbox(
        accesstoken=mapbox_access_token,
    ),
    title = go.layout.Title(
        text = 'Before The Chosen Route'
    ),
)

fig = go.Figure(data = line, layout = layout)
ply.plot(fig, filename='route-before.html')