# definisi fungsi print_string
from os import system
def print_string(str):
    system('cls')
    print("""Menampilkan argumen string str ke layar""")
    print(str)
# Kita memanggil fungsi dengan kata kunci
print_string(str = "Hello Python")
