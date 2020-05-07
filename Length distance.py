import geopandas as gpd
data = "./stasiun bandung-terminal dago.json"
df = gpd.read_file(data)

df = df.ix[0]

series = gpd.GeoSeries(df)

deg2km = 111
dis_route = series.geometry.length * deg2km
