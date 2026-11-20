n = int(input("masukkan n: "))

deret = []
jumlah_semua = 0
jumlah_genap = 0

for i in range(1, n + 1):
    deret.append(str(i))
    jumlah_semua += i
    if i % 2 == 0:
        jumlah_genap += i

print("deret:" + " ".join(deret))
print("jumlah semua:", jumlah_semua)
print("jumlah genap:", jumlah_genap)