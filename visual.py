from dash import Dash, dcc, html, Input, Output
import plotly.express as px

import pandas as pd

df = pd.read_csv('modified_data.csv')

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        df['sales'].min(),
        df['sales'].max(),
        step=None,
        value=df['sales'].min(),
        marks={str(sales): str(sales) for sales in df['sales'].unique()},
        id='sales-slider'
    )
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('sales-slider', 'value'))
def update_figure(selected_sales):
    filtered_df = df[df.sales == selected_sales]

    fig = px.scatter(filtered_df, x="sales", y="date",
                     log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig


#if __name__ == '__main__':
    #app.run_server(debug=True)

import dash
from dash import callback, html, dcc, Input, Output, ctx

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Button('Button 1', id='btn-1'),
    html.Button('Button 2', id='btn-2'),
    html.Button('Button 3', id='btn-3'),
    html.Div(id='container'),
    html.Div(id='container-no-ctx')
])

@callback(
    Output('container-no-ctx', 'children'),
    Input('btn-1', 'n_clicks'),
    Input('btn-2', 'n_clicks'))
def update(btn1, btn2):
    return f'button 1: {btn1} & button 2: {btn2}'


@callback(Output('container','children'),
              Input('btn-1', 'n_clicks'),
              Input('btn-2', 'n_clicks'),
              Input('btn-3', 'n_clicks'))
def display(btn1, btn2, btn3):
    button_clicked = ctx.triggered_id
    return f'You last clicked button with ID {button_clicked}'

if __name__ == '__main__':
    app.run_server(debug=True)

