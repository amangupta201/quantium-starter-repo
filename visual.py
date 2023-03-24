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


if __name__ == '__main__':
    app.run_server(debug=True)



