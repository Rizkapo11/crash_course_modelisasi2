print('menghitung luas segetiga')

alas = 50
tinggi = 3
luas_segitiga = alas * tinggi / 2
print(f'segetiga dengan alas = {alas} tinggi = {tinggi} memiliki luas = {luas_segitiga}')

alas = 100
tinggi = 5
luas_segitiga = alas * tinggi / 2
print(f'segetiga dengan alas = {alas} tinggi = {tinggi} memiliki luas = {luas_segitiga}')

print('\nmenghitung luas segetiga dengan fungsi')


def hitung_luas_segitiga(alas: object, tinggi: object) -> object:
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

alas = 8
tinggi = 3
print (f'dengan fungi, segetiga dengan alas = {alas} tinggi = {tinggi} memiliki luas = {hitung_luas_segitiga (alas, tinggi)}')
print (f'menghitung luas segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga (10, 3)}')
print (f'dari data diatas berapakah luas segitiga tersebut = {hitung_luas_segitiga (8, 5)}')


