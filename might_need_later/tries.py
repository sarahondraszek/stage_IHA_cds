import geocoder
g = geocoder.geonames(6094817, method='details', geoNamesUsername="sarahondraszek", key="sarahondraszek")
print(g.lat, g.lng)