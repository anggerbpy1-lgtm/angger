# input data
nilai = int(input("Masukkan nilai = "))

# Menentukan Grade
if nilai < 0 or nilai > 100 :
    print("nilai tidak valid")
elif nilai >= 85: 
    print("grade: a")
elif nilai >= 70: 
    print("grade: b")
elif nilai >= 55: 
    print("grade: c")
elif nilai >= 40: 
    print("grade: d")
else:
    print ("grade: e")