# input data
angka = int(input("Masukkan bilangan : "))

# Proses data
if angka == 0:
    print("bilangan nol")
else:
    if angka % 2 != 0:
        jenis_angka = "ganjil"
    else:
        jenis_angka = "genap"
    if angka > 0:
        sifat_angka = "positif"
    else:
        sifat_angka = "negatif"

#output
print(f"bilangan {jenis_angka} dan {sifat_angka}")