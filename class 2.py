class Kopi():
    def __init__(self, inputJenis, inputDaerah):
        self.jenis = inputJenis
        self.daerah = inputDaerah
       

kopi1 = Kopi("Robusta","Mandar")
kopi2 = Kopi("Arabika","Mamasa")



print(kopi1.__dict__)
print(kopi1.daerah)
