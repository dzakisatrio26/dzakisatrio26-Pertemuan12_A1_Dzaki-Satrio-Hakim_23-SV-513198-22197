#Mencetak Menu 
from persegi import luas_persegi 
from lingkaran import luas_lingkaran
from segitiga import luas_segitiga

def main_menu(): 
    print ("Pilih Bentuk 2D")
    print() 
    print ("1. Persegi Panjang")
    print ("2. Lingkaran")
    print ("3. Segitiga")
    print ("4. Keluar")
    opsi = input("Masukkan opsi bangun datar = ")
    if opsi == "1":
        lp()
    elif opsi == "2":
        luas_lingkaran()
    elif opsi == "3":
        luas_segitiga()
    elif opsi == "4":
        exit()
    else:
        print("Opsi yang anda masukkan tidak tersedia")

if __name__ == "__main__":
    while True:
        main_menu()