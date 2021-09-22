"""Exploring the datawrapper python package for easier use of DataWrapper API.

https://blog.datawrapper.de/datawrapper-python-package/
"""

import os

from datawrapper import Datawrapper
import pandas as pd


data = pd.read_csv('organic_share.csv')

dw = Datawrapper(access_token=os.getenv('DATAWRAPPER_ACCESS_TOKEN'))

chart_info = dw.create_chart(
    title='Organic farms in Europe',
    chart_type='d3-maps-choropleth',
    data=data,
)

properties = {
    "axes": {
        "keys": "geo",
        "values": "organic_share",
        "labels": "organic_share",
    },
    "visualize": {
        "basemap": "europe",
        "map-key-attr": "ISO_A2",
        "colorscale": {
            'colors': [
                {'color': '#fefaca', 'position': 0},
                {'color': '#008b15', 'position': 1},
            ],
        },
        "map-label-format": "0.0%",
        "labels": {"enabled": True, "type": "column"},
        "legend": {"labelFormat": "0.0%"},
        "tooltip": {
            "body": '{{ organic_share }}%',
            'title': '%REGION_NAME%',
            'enabled': True,
        },
    },
}

description = {
    "source_name": "Eurostat",
    "source_url": "https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Organic_farming_statistics",
    "intro": "Share of organic farms area in total utilised agricultural area in 2019",
}

dw.update_metadata(chart_info['id'], properties)
dw.update_description(chart_info['id'], **description)
dw.publish_chart(chart_id=chart_info['id'])
