#Nama : Aisyah Shinta Balqis
#Nim : D0219305

class Orang:

  def __init__ (self, nama, asal):
    self.nama = nama
    self.asal = asal

  def perkenalan (self):
    print(f'Perkenalkan nama saya {self.nama} dari {self.asal}')

Aisyah = Orang('Aisyah', 'Polewali Mandar')
Aisyah.perkenalan()
