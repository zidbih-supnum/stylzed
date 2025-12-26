import json
import pandas as pd
import geopandas as gpd 
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource, LinearColorMapper, HoverTool, ColorBar
from bokeh.palettes import OrRd9


def get_interactive_map(gdf, df, candidate_name, year=2024):
    """
    Merges election data with geographic shapes and returns a Bokeh plot.
    """
    # 1. Filter results
    df_filtered = df[(df['year'] == year) & (df['candidate'] == candidate_name)].copy()
    
    # 2. Merge
    merged = gdf.merge(df_filtered, on="moughataa", how="left")
    merged['nb_votes'] = merged['nb_votes'].fillna(0)

    # --- FIX STARTS HERE ---
    # Convert all datetime columns to strings so they can be saved to JSON
    for col in merged.select_dtypes(include=['datetime64', 'datetimetz']).columns:
        merged[col] = merged[col].astype(str)
    # --- FIX ENDS HERE ---

    # 3. Convert to JSON
    merged_json = json.loads(merged.to_json())
    geosource = GeoJSONDataSource(geojson=json.dumps(merged_json))

    # ... (rest of your code remains the same)
    palette = OrRd9[::-1]
    color_mapper = LinearColorMapper(palette=palette, low=0, high=merged['nb_votes'].max())

    p = figure(title=f"Election Results: {candidate_name} ({year})", 
               height=600, width=500,
               tools="pan,wheel_zoom,reset,save")
    p.axis.visible = False
    p.grid.grid_line_color = None

    p.patches('xs', 'ys', source=geosource,
              fill_color={'field': 'nb_votes', 'transform': color_mapper},
              line_color='black', line_width=0.5, fill_alpha=0.8)

    hover = HoverTool(tooltips=[
        ("Moughataa", "@moughataa"),
        ("Votes", "@nb_votes{0,0}"),
        ("Candidate", "@candidate")
    ])
    p.add_tools(hover)

    return p