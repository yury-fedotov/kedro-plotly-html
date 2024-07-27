"""
This is a boilerplate pipeline 'visualization'
generated using Kedro 0.19.6
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import create_plotly_chart


def create_pipeline() -> Pipeline:
    return pipeline([
        node(
            create_plotly_chart,
            inputs=None,
            outputs="time_series_chart",
        ),
    ])
