def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n - 1)

# Contoh penggunaan
n = int(input("Silahkan Masukkan angka:"))
hasil = faktorial(n)
print(f"Faktorial dari {n}! adalah {hasil}.")