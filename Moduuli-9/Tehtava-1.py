class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.reskiteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

auto = Auto("ABC-123", 142)

print(f"Rekisteritunnus: {auto.reskiteritunnus}")
print(f"Huippunopeus: {auto.huippunopeus} km/h")
print(f"Nopeus: {auto.nopeus} kmh/h")
print(f"Kuljettu matka: {auto.matka} km")
