#Nama : Aisyah Shinta Balqis
#Nim : D0219305

class S:
   def __init__(diri, nama, nim):
      diri.nama = nama       # public
      diri.__nim = nim  # private

   def who(diri):
      print('Nama  : ', diri.nama)
      print('Nim : ', diri.__nim)
