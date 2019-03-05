import plotly.offline as py
import plotly.graph_objs as go

import numpy as np
x = np.random.randn(2000)
y = np.random.randn(2000)


data = []
data.append(
    go.Histogram2dContour(
        x =x, 
        y =y, 
        contours=dict(coloring='heatmap')
    ),
)
data.append(
    go.Scatter(
        x=x, 
        y=y, 
        mode='markers', 
        marker=dict(color='white', size=3, opacity=0.3)
    )
)
py.plot(data=data, show_link=True,)