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

h = Hissi(1,100)
h.siirtymä(5)
h.siirtymä(1)
