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

kilpailu = True
while kilpailu:
    for auto in autot:
        auto.kiihdytys(random.randint(-10,15))
        auto.kuljettu(1)


        if auto.matka >= 10000:
            kilpailu = False
            break

print(f"{'Rekisteri':<10}{'Huippunopeus':<15}{'Nopeus':<10}{'Matka':<10}")
print("-" * 45)
for auto in autot:
    print(f"{auto.rekisteritunnus:<10}{auto.huippunopeus:<15}{auto.nopeus:<10}{auto.matka:<10.1f}")