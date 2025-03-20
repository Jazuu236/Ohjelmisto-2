class Hissi:
    def __init__(self, alas, ylos):
        self.alas = alas
        self.ylos = ylos
        self.uhissi = alas

    def kerros_ylös(self):
        if self.uhissi < self.ylos:
            self.uhissi += 1
        print(f"Hissi on nyt kerroksessa: {self.uhissi}")

    def kerros_alas(self):
        if self.uhissi > self.alas:
            self.uhissi -= 1
        print(f"Hissi on nyt kerroksessa: {self.uhissi}")

    def siirtymä(self, kohde):
        while self.uhissi < kohde:
            self.kerros_ylös()
        while self.uhissi > kohde:
            self.kerros_alas()

class Talo:
    def __init__(self, alas, ylos, maara):
        self.alas = alas
        self.ylos = ylos
        self.hissit = [Hissi(alas, ylos) for _ in range(maara)]

    def aja_hissiä(self, hissin_num, kohde):
        if 0 <= hissin_num < len(self.hissit):
            print(f"Ajetaan hissiä: {hissin_num} kerrokseen {kohde}")

talo = Talo(1,100,3)

talo.aja_hissiä(1, 3)
talo.aja_hissiä(0,87)
talo.aja_hissiä(2,17)
talo.aja_hissiä(0, 1)
