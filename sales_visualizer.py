import dash
from dash import dcc, html, Input, Output
import pandas as pd

df = pd.read_csv('output.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualisation",
            style={'textAlign': 'center', 'color': '#e91e8c', 'fontFamily': 'Arial'}),

    html.Div([
        html.Label("Filter by Region:", style={'fontWeight': 'bold'}),
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'All', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
            ],
            value='all',
            inline=True,
            style={'margin': '20px 0'}
        )
    ], style={'textAlign': 'center'}),

    dcc.Graph(id='sales-chart')

], style={'maxWidth': '900px', 'margin': 'auto', 'padding': '20px'})


@app.callback(
    Output('sales-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(region):
    if region == 'all':
        filtered = df
    else:
        filtered = df[df['region'] == region]

    return {
        'data': [{
            'x': filtered['date'],
            'y': filtered['sales'],
            'type': 'line',
            'name': 'Sales'
        }],
        'layout': {
            'title': f'Pink Morsel Sales — {region.capitalize()}',
            'xaxis': {'title': 'Date'},
            'yaxis': {'title': 'Sales ($)'}
        }
    }


if __name__ == '__main__':
    app.run(debug=True)