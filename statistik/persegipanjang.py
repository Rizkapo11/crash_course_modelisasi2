from bangun_ruang import bangun_ruang


class PersegiPanjang(bangun_ruang):
    def __init__( self, p, l ):
        #fungsi yang pertama kali dipanggil saat objek diciptakan
        self.p = p
        self.l = l
    def info(self):
        return f'ini adalah objek dari persegi panjang, dengan panjang = {self.p} dan lebar = {self.l}'

    def hitung_luas(self):
        return self.p * self.l
