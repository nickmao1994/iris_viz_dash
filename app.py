import altair as alt
from dash import Dash, html, dcc, Input, Output
from vega_datasets import data

# read global data
iris = data.iris()

# setup app and layout
app = Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server

app.layout = html.Div([
        html.Iframe(
            # srcDoc=plot_altair(),
            id = 'scatter',
            style={'border-width': '0', 'width': '100%', 'height': '400px'}),
        dcc.Dropdown(
            id = 'xcol-widget',
            value = 'sepalLength',
            options = [{'label': col, 'value': col} for col in iris.columns]) 
        ])


# setup call back
@app.callback(
    Output('scatter', 'srcDoc'),
    Input('xcol-widget', 'value'))

def plot_altair(xcol):
    chart = alt.Chart(iris).mark_point().encode(
        alt.X(xcol, scale=alt.Scale(zero=False)),
        alt.Y('sepalWidth', scale=alt.Scale(zero=False)), 
        color = 'species'
        )
    return chart.to_html()

if __name__ == '__main__':
    app.run_server(debug=True)