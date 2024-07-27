import plotly.graph_objects as go
import plotly.express as px


def create_plotly_chart() -> go.Figure:
    df = px.data.gapminder().query("continent=='Oceania'")
    fig = px.line(df, x="year", y="lifeExp", color='country')
    return fig
