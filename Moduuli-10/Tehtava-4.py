import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytys(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kuljettu(self, aika):
        self.matka += self.nopeus * aika

autot = [Auto(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def aika(self):
        for auto in self.autot:
            auto.kiihdytys(random.randint(-10,15))
            auto.kuljettu(1)

    def tilanne(self):
        print(f"Kilpailu: {self.nimi}")
        print(f"{'Rek num':<10}{'Huippunopeus':<15}{'Nopeus':<10}{'Matka':<10}")
        print("_" * 50)
        for auto in autot:
            print(f"{auto.rekisteritunnus:<10}{auto.huippunopeus:<15}{auto.nopeus:<10}{auto.matka:<10}")

    def kilpailu_ohi(self):
        return any(auto.matka >= self.pituus for auto in self.autot)


autot = [Auto(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]  # 10 autoa

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunti = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.aika()
    tunti += 1
    if tunti % 10 == 0:
        kilpailu.tilanne()


print("Kilpailu on päättynyt!")
kilpailu.tilanne()
