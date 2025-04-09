from flask import Flask, jsonify
import mariadb

app = Flask(__name__)

def hae_lenttokentta(icao):
    try:
        yhteys = mariadb.connect(
            host='localhost',
            user='root',
            password='Salasana',
            database='flight_game'
        )
        sql = "SELECT name, municipality FROM airport WHERE ident=%s"
        kursori = yhteys.cursor()
        kursori.execute(sql, (icao,))
        tulos = kursori.fetchone()
        kursori.close()
        yhteys.close()

        if tulos:
            return {
                "ICAO": icao,
                "Name": tulos[0],
                "Municipality": tulos[1]
            }
        else:
            return None

    except mariadb.Error as e:
        print(f"Database connection error: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

@app.route('/kenttä/<icao>', methods=['GET'])
def hae_tiedot(icao):
    tiedot = hae_lenttokentta(icao)
    if tiedot:
        return jsonify(tiedot)
    else:
        return jsonify({"error": "Lentokenttää ei löytynyt annetulla ICAO-koodilla."}), 404

if __name__ == '__main__':
    app.run(port=3000)
