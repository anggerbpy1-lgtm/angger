batas_bawah = int(input(" batas bawah : "))
batas_atas = int(input(" batas atas : "))

bilangan_prima = []
jumlah_prima = 0

print(f"\nHasil rentang {batas_bawah} sampai {batas_atas}:")

for angka in range(batas_bawah, batas_atas + 1):
    
    if angka > 1:
        adalah_prima = True
        
        for i in range(2, int(angka ** 0.5) + 1):
            if angka % i == 0:
                adalah_prima = False
                break
        
        if adalah_prima:
            bilangan_prima.append(str(angka))
            jumlah_prima += 1

if jumlah_prima > 0:
    print(f" #Bilangan prima : {', '.join(bilangan_prima)}")
    print(f" #Jumlah bilangan prima: {jumlah_prima} bilangan")
else:
    print(" Tidak ada bilangan prima yang ditemukan dalam rentang tersebut.")
