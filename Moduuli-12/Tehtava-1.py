import requests

def norris_vitsi():
    url = "https://api.chucknorris.io/jokes/random"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(data["value"])
    except requests.exceptions.RequestException as e:
        print("Virhe!", e)

if __name__ == "__main__":
    norris_vitsi()
