jumlah_siswa = int(input("Masukkan jumlah siswa: "))
nilai_siswa = {}

for i in range(jumlah_siswa):
    nama = input("Masukkan nama siswa {}: ".format(i+1))
    nilai = float(input("Masukkan nilai siswa {}: ".format(i+1)))

    nilai_siswa[nama] = nilai

print("\nNilai siswa : ")
for nama, nilai_angka in nilai_siswa.items():
    print(f"{nama} : {nilai_angka}")
