from dash import Dash, html, dash_table
import pandas as pd

df = pd.read_csv('flights.csv')
df['DepDelay'] = df['DepDelay'].where(df['DepDelay'] < 15, other='Delayed')

app = Dash()
app.layout = [
    html.Div(children='My first App with Data in Dash'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10)
]

if __name__ == '__main__':
    app.run(debug=True)