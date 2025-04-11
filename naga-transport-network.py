import osmnx as ox
import folium

# Load the graph of Naga, Philippines
place = "Naga, Philippines"
graph = ox.graph_from_place(place, network_type='drive') 

# Get graph nodes and edges as GeoDataFrames
gdf_nodes, gdf_edges = ox.graph_to_gdfs(graph)

# Create folium map centered on the mean node location
center_lat = gdf_nodes.geometry.y.mean()
center_lon = gdf_nodes.geometry.x.mean()
m = folium.Map(location=[center_lat, center_lon], zoom_start=14)

# Add edges (roads)
folium.GeoJson(gdf_edges[['geometry']]).add_to(m)

# Add nodes with labels (can be node ID or anything else)
for node_id, node_data in gdf_nodes.iterrows():
    lat = node_data.geometry.y
    lon = node_data.geometry.x

    folium.CircleMarker(
        location=[lat, lon],
        radius=3,
        color='blue',
        fill=True,
        fill_opacity=0.7,
        popup=folium.Popup(f"Node ID: {node_id}", max_width=200),
        tooltip=f"{node_id}"
    ).add_to(m)

# Save or display the map
m.save("graph_with_nodes_urban-network_naga.html")
