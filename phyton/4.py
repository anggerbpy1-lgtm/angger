# input data 
n = int(input("Masukkan tinggi segitiga (n): "))

# proses data 
if n <= 0:
    print("Silakan masukkan tinggi segitiga yang lebih besar dari 0.")
else:
    print("\nHasil Pola Segitiga:")
    # Perulangan 
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end="")
        # Pindah baris baru setelah mencetak bintang 
        print() 