import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium

pnumber = phonenumbers.parse("+27796778695")
def check_country():
    return geocoder.description_for_number(pnumber, "en")
def service_provider():
    return carrier.name_for_number(pnumber, "en")

# ------------------------------ Check Coordinates ------------------------------
def read_oc_key():
    with open("api_key.txt", "r") as oc_key:
        return oc_key.read()
    
loc_geocoder = OpenCageGeocode(read_oc_key())
results = loc_geocoder.geocode(str(check_country()))
def coordination():
    return results[0]['geometry']

def Create_Map():
    lat = coordination()['lat']
    lng = coordination()['lng']
    create_map = folium.Map(location = [lat, lng], zoom_start = 10)
    create_marker = folium.Marker([lat, lng], popup=check_country).add_to(create_map)
    create_map.save('curr_location.html') 