# ML for Social Good Proj 1 

import numpy as np
import pandas as pd
import json
import math
import plotly.express as px
from area import area

# read the neighborhood population data into a DataFrame and load the GeoJSON data
nycmap = json.load(open("nyc_zip.geojson"))

filenames = ['2019_2020.csv', '2021_pre_final.csv', '2021_post_final.csv', '2022_FHEPS_final.csv', '2022_sec8_final.csv']

# Which of the files to display. Indexing starts at 0
file_num = 0

# The colorscheme to use for plotting, find full list here: https://plotly.com/python/builtin-colorscales/#builtin-sequential-color-scales
color_scale = "YlGnBu"

# Column name to nap based on (Claim, No Claim, etc.)
column_name = "Claim"

df = pd.read_csv(f'data/{filenames[file_num]}')

'''
d = {}
neighborhood = nycmap["features"]
for n in neighborhood:
    code = n["properties"]["ZIPCODE"]
    d[code] = n["properties"]["PO_NAME"]


zips = list(d.keys())
names = list(d.values())
zip_df = pd.DataFrame({'Zip': zips, 'Names': names})
densitys = np.random.rand(len(zips)) *10 
zip_df['density'] = densitys
'''

# call Plotly Express choropleth function to visualize data
fig = px.choropleth_mapbox(df,
                        geojson=nycmap,
                        locations="zip",
                        featureidkey="properties.ZIPCODE",
                        color=column_name,
                        color_continuous_scale=color_scale, #"viridis",
                        mapbox_style="carto-positron",
                        zoom=9, center={"lat": 40.7, "lon": -73.9},
                        opacity=0.7,
                        hover_name="zip"
                        )

fig.show()

    # black ice, pink dragonfruit