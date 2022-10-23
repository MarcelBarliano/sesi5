class Product:
    # _init_ => Merupakan Method Konstruktor
    # Method untuk Setter
    def _init_(self,ID_Produk,Nama_Produk,Harga,Jumlah):
        self.IDProduk = ID_Produk 
        self.Nama_Produk = Nama_Produk
        self.Harga = Harga
        self.Jumlah = Jumlah 

# Isi data dalam method Setter
a = Product(0,"teh Botol",1323,445)

# Method untuk Getter
print("Id_Produk : {}\nNama_Produk : {}\nHarga : {}\nJumlah : {} "
.format( a.IDProduk, a.Nama_Produk, a.Harga, a.Jumlah))