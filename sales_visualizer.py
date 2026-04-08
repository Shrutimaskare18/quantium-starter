import dash
from dash import dcc, html
import pandas as pd

# output.csv padhna jo Task 2 mein banaya tha
df = pd.read_csv('output.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualisation"),
    dcc.Graph(
        id='sales-chart',
        figure={
            'data': [{
                'x': df['date'],
                'y': df['sales'],
                'type': 'line',
                'name': 'Sales'
            }],
            'layout': {
                'title': 'Pink Morsel Sales Over Time',
                'xaxis': {'title': 'Date'},
                'yaxis': {'title': 'Sales ($)'}
            }
        }
    )
])

if __name__ == '__main__':
    app.run(debug=True)