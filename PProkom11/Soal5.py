def hitung_volume_kerucut(jari_jari, tinggi):
    pi = 3.14159
    volume = (1/3) * pi * (jari_jari ** 2) * tinggi
    return volume

# Contoh penggunaan fungsi:
jari_jari_alas = int(input("Silahkan Masukkan jari-jari:"))
tinggi_kerucut = int(input("Silahkan Masukkan tinggi:"))
volume_kerucut = hitung_volume_kerucut(jari_jari_alas, tinggi_kerucut)
print(f"""Volume kerucut dengan jari-jari {jari_jari_alas}
dan tinggi {tinggi_kerucut} adalah {volume_kerucut}""")