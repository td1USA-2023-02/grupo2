import h3
import folium

# Obtén las coordenadas del centro de Colombia (por ejemplo, Bogotá)
colombia_center = (4.6097, -74.0817)

# Configura el mapa de Folium
map_colombia = folium.Map(location=colombia_center, zoom_start=6)

# Define la resolución de los hexágonos (ajusta según sea necesario)
resolution = 7

# Genera hexágonos para un área alrededor del centro de Colombia
hexagons = h3.k_ring(h3.geo_to_h3(*colombia_center, resolution), 10)

# Dibuja los hexágonos en el mapa
for hex_id in hexagons:
    vertices = h3.h3_to_geo_boundary(hex_id)
    folium.Polygon(locations=vertices, color='blue', fill=True, fill_color='blue', fill_opacity=0.4).add_to(map_colombia)

# Guarda el mapa en un archivo HTML o visualízalo directamente
map_colombia.save('colombia_hexagons.html')
