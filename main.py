class Avto:
    def __init__(self, model, rang, korobka, narh, kilometer=0):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.kilometer = kilometer
    def get_info(self):
        return (f"Model: {self.model}, Rang: {self.rang}, "
                f"Korobka: {self.korobka}, Narh: {self.narh} so'm, "
                f"Kilometraj: {self.kilometer} km")

    def update_km(self, new_km):
        if new_km >= self.kilometer:
            self.kilometer = new_km
        else:
            print("Error")


class Avtosalon:
    def __init__(self, nomi, manzil):
        self.salon_nomi = nomi
        self.manzil = manzil
        self.sotuvdagi_avtomobillar = []

    def avtomobil_qoshish(self, avtomobil):
        self.sotuvdagi_avtomobillar.append(avtomobil)

    def avtomobillarni_korish(self):
        return [avto.get_info() for avto in self.sotuvdagi_avtomobillar]

    def salon_malumoti(self):
        return (f"Salon Nomi: {self.nomi}, "
                f"Manzil: {self.manzil}, "
                f"Sotuvdagi Avtomobillar: {len(self.sotuvdagi_avtomobillar)} ta")

avto1 = Avto("BYD Champion", "oq", "avtomat", 35000)
avto2 = Avto("BYD Chazor", "qora", "avtomat", 30000)

salon = Avtosalon("Avtosalon BYD", "Urganch, Darital yoni")

salon.avtomobil_qoshish(avto1)
salon.avtomobil_qoshish(avto2)

print(salon.salon_malumoti())
print(salon.avtomobillarni_korish())
avto1.update_km(155)
print(avto1.get_info())



