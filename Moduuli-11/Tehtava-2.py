class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.matka = 0
        self.nopeus = nopeus

    def aja(self, tunti):
        self.matka += self.nopeus * tunti

    def tulosta_tiedot(self):
        print(f"Rekisteritunnus: {self.rekisteritunnus}")
        print(f"Huippunopeus: {self.huippunopeus} km/h")
        print(f"Ajettu matka: {self.matka} km")


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, kapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.kapasiteetti = kapasiteetti

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Akunkapasiteetti: {self.kapasiteetti} kWh")


class Polttomoottori(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankki = tankki

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Polttoainetankin tilavuus: {self.tankki} l")


def main():
    sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
    polttomoottori = Polttomoottori("ACD-123", 165, 32.3)

    sahkoauto.Nopeus = 153
    sahkoauto.aja(3)

    polttomoottori.Nopeus = 147
    polttomoottori.aja(3)

    print("Sähköauto tiedot:")
    sahkoauto.tulosta_tiedot()
    print("Polttomoottori auton tiedot:")
    polttomoottori.tulosta_tiedot()


if __name__ == "__main__":
    main()
