class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.reskiteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 2000

    def kiihdytys(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kuljettu(self, aika):
        self.matka += self.nopeus * aika

auto = Auto("ABC-123", 142)

print(f"Rekisteritunnus: {auto.reskiteritunnus}")
print(f"Huippunopeus: {auto.huippunopeus} km/h")
print(f"Nopeus: {auto.nopeus} kmh/h")
print(f"Kuljettu matka: {auto.matka} km")

auto.kiihdytys(30)
auto.kiihdytys(70)
auto.kiihdytys(50)

print(f"Tämän hetkinen nopeus: {auto.nopeus} km/h")

auto.kiihdytys(-200)
print(f"Auton nopeus hätäjarrutuksen jälkeen: {auto.nopeus} km/h")

auto.kiihdytys(60)
auto.kuljettu(1.5)
print(f"Kuljettu matka: {auto.matka} km")