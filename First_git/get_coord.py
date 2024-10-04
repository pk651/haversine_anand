import haversine
import requests
def get_coordinates(address:str) -> list:
    """ this function takes an address and return coordinates """

    URL = "https://api-adresse.data.gouv.fr/search/?q="
    r = requests.get(URL + address)
    coordinates= r.json()['features'][0]['geometry']['coordinates'][::-1]
    return coordinates