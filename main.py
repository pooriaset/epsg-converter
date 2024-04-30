import geopandas as gpd

# Read GeoDataFrame from GeoJSON file
gdf = gpd.read_file("data/data.geojson")

# Define EPSG codes for UTM and WGS84
utm_epsg = 32639 
wgs84_epsg = 4326

# Convert GeoDataFrame to WGS84
gdf_wgs84 = gdf.to_crs(epsg=wgs84_epsg)

# Save GeoDataFrame to a new GeoJSON file in WGS84
gdf_wgs84.to_file("data/data-wgs84.geojson", driver="GeoJSON")