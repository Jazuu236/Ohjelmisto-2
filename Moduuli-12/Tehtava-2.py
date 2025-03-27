import requests

def saa(paikkakunta):
    API_KEY = "Tässä oli avain"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={API_KEY}&lang=en"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        lampotilaK = data["main"]["temp"]
        lampotilaC = lampotilaK - 273.15
        saakuvaus = data["weather"][0]["description"]

        print(f"Sää {paikkakunta}: {saakuvaus.capitalize()}, {lampotilaC:.1f}°C")
    except requests.exceptions.RequestException as e:
        print("Virhe haettaessa säätietoja:", e)
    except KeyError:
        print("Virhe: Tarkista paikkakunnan nimi tai API-avain.")

if __name__ == "__main__":
    kaupunki = input("Anna paikkakunta: ")
    saa(kaupunki)