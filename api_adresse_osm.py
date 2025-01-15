import requests

def API_address(Lat, Lng):
  url = f"https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat={Lat}&lon={Lng}&limit=1"
  headers = {
    'User-Agent': 'Mon application'
  }
  r = requests.get(url, headers=headers)

  # extraire les données JSON

  r = r.json()

  point = [r['lat'], r['lon']]

  return point