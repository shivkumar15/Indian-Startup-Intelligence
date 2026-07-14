

from __future__ import annotations

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from config import CHART_HEIGHT


class ChartFactory:
    """
    Generates all Plotly charts used
    throughout the application.
    """

    
    # Theme
    

    @staticmethod
    def _apply_theme(fig):

        fig.update_layout(

            template="plotly_white",

            height=CHART_HEIGHT,

            paper_bgcolor="rgba(0,0,0,0)",

            plot_bgcolor="rgba(0,0,0,0)",

            margin=dict(

                l=20,

                r=20,

                t=50,

                b=20

            ),

            legend_title_text="",

            title_x=0.02,

            font=dict(

                family="Segoe UI",

                size=13

            ),
            hovermode="x unified"
           
        )

        return fig

    
    # Line Chart
    

    @staticmethod
    def line(

        dataframe: pd.DataFrame,

        x: str,

        y: str,

        title: str

    ):

        fig = px.line(

            dataframe,

            x=x,

            y=y,

            markers=True,

            title=title

        )

        fig.update_traces(

            line_width=3,

            marker_size=8

        )

        return ChartFactory._apply_theme(fig)

    
    # Bar Chart
    

    @staticmethod
    def bar(

        dataframe: pd.DataFrame,

        x: str,

        y: str,

        title: str,

        horizontal: bool = False

    ):
        if dataframe.empty:

            return ChartFactory.empty()

        if horizontal:

            fig = px.bar(

                dataframe,

                x=x,

                y=y,

                orientation="h",

                text_auto=".2s",

                title=title

            )

        else:

            fig = px.bar(

                dataframe,

                x=x,

                y=y,

                text_auto=".2s",

                title=title

            )

        return ChartFactory._apply_theme(fig)

    
    # Pie Chart
    

    @staticmethod
    def pie(

        dataframe: pd.DataFrame,

        names: str,

        values: str,

        title: str,

        hole: float = 0.45

    ):
        if dataframe.empty:

              return ChartFactory.empty()
        fig = px.pie(

            dataframe,

            names=names,

            values=values,

            hole=hole,

            title=title

        )

        return ChartFactory._apply_theme(fig)

    
    # Area Chart
    

    @staticmethod
    def line(

        dataframe: pd.DataFrame,

        x: str,

        y: str,

        title: str

    ):

        if dataframe.empty:

            return ChartFactory.empty()

        fig = px.line(

            dataframe,

            x=x,

            y=y,

            markers=True,

            title=title

        )

        fig.update_traces(

            line_width=3,

            marker_size=8

        )

        return ChartFactory._apply_theme(fig)

    
    # Scatter Chart
    

    @staticmethod
    def scatter(

        dataframe: pd.DataFrame,

        x: str,

        y: str,

        title: str,

        color: str | None = None

    ):

        fig = px.scatter(

            dataframe,

            x=x,

            y=y,

            color=color,

            title=title

        )

        return ChartFactory._apply_theme(fig)

    
    # KPI Indicator
    

    @staticmethod
    def indicator(

        title: str,

        value

    ):

        fig = go.Figure(

            go.Indicator(

                mode="number",

                value=value,

                title={

                    "text": title

                }

            )

        )

        return ChartFactory._apply_theme(fig)

    
    # Empty Figure
    

    @staticmethod
    def empty(

        message="No data available."

    ):

        fig = go.Figure()

        fig.add_annotation(

            text=message,

            showarrow=False,

            font=dict(size=18)

        )

        fig.update_xaxes(visible=False)

        fig.update_yaxes(visible=False)

        return ChartFactory._apply_theme(fig)
    
    
# Horizontal Bar Chart


    @staticmethod
    def horizontal_bar(
        dataframe: pd.DataFrame,
        x: str,
        y: str,
        title: str
    ):

        return ChartFactory.bar(
            dataframe=dataframe,
            x=x,
            y=y,
            title=title,
            horizontal=True
        )
    

    
# Donut Chart


    @staticmethod
    def donut_chart(
        dataframe: pd.DataFrame,
        names: str,
        values: str,
        title: str
    ):

        return ChartFactory.pie(
            dataframe=dataframe,
            names=names,
            values=values,
            title=title,
            hole=0.55
        )
    

    
# Line Chart


    @staticmethod
    def line_chart(
        dataframe: pd.DataFrame,
        x: str,
        y: str,
        title: str
    ):

        return ChartFactory.line(
            dataframe=dataframe,
            x=x,
            y=y,
            title=title
        )