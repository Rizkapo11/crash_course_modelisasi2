from bangun_ruang import bangun_ruang
from segitiga_2 import segitiga
from statistik.persegipanjang import PersegiPanjang

print ('menggungkan OOP')
p1 = PersegiPanjang(8, 3)
print (p1.info())
print (p1.hitung_luas())

s1 = segitiga (10, 4)
print (s1.info())
print (s1.hitung_luas())

print ('\n mencoba membuat objek dari kelas bangun_ruang')
b1 = bangun_ruang ()
print (b1.info())
print (b1.hitung_luas())

#polymorphism : kemampuan objek untuk merspon berbeda, terhadap pemanggil method yang sama
daftar_bangun_ruang = []
daftar_bangun_ruang.append (p1)
daftar_bangun_ruang.append (s1)

print ('\n polymorphism ')
for bangun_ruang in daftar_bangun_ruang:
    print (bangun_ruang.info())
