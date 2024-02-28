# Membuka file Me.txt untuk menulis
with open('Me.txt', 'w') as file:
    # Menulis baris-baris yang diinginkan ke dalam file
    file.write('Nama : Bonipacius Immanuel Sinaga\n')
    file.write('NIM : 122140032\n')
    file.write('Resolusi Saya di Tahun ini : ingin berbakti kepada nusa dan bangsa\n')

print("File 'Me.txt' berhasil dibuat dan diisi dengan data.")
