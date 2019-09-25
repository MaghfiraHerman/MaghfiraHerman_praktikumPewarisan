class sepatu(object):
    def __init__(self, merk, ukran):
        self.merk = merk
        self.ukuran = ukuran

    def cetakdata(self):
        print("merk\t: ", self.merk)
        print("ukuran\t: ", self.ukuran)


#mendefinisikan kelas turunan (subclass)
class sepatuanak(sepatu):
    def __init__(self, merk, ukuran, warna):
        self.merk = merk
        self.ukuran = ukuran
        self.warna = warna

    def cetakData(self):
        print("merk\t: ", self.merk)
        print("ukuran\t: ", self.ukuran)
        print("warna\t: ", self.warna)
       

def main():
   # membuat objek KotakWarna
   sepatuanak1 = sepatuanak("adidas", 38, "merah")

   # menggunakan objek
   sepatuanak1.cetakData()
   

if __name__ == "__main__":
    main()
