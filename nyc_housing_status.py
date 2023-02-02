# 

import numpy as np
import pandas as pd
import json
import math
import plotly.express as px
from area import area

# read the neighborhood population data into a DataFrame and load the GeoJSON data
nycmap = json.load(open("nyc_zip.geojson"))
#df = pd.read_csv('2019_2020_FINAL.csv')
df = pd.read_csv('house_claim_counts_by_zip.csv')

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

# call Plotly Express choropleth function to visualize data
fig = px.choropleth_mapbox(df,
                        geojson=nycmap,
                        locations="zip",
                        featureidkey="properties.ZIPCODE",
                        color="Claim",
                        color_continuous_scale="YlGnBu", #"viridis",
                        mapbox_style="carto-positron",
                        zoom=9, center={"lat": 40.7, "lon": -73.9},
                        opacity=0.7,
                        hover_name="zip"
                        )

fig.show()

    # black ice, pink dragonfruit