# Nama Teman
list = ['Aisyah', 'Nuri', 'Anna', 'Mayyah', 'Dhilla', 'Risma', 'Ryan', 'Dita', 'Fifi', 'Windi']

# Menampilkan isi list indeks nomor 4,6,7
print("list[4,6,7]: ", list[4], list[6], list[7])

# Mengganti nama pada list nomor 3,5,9
print("Nama_3,5,9: ", list[3], list[5], list[9])
list[3] = 'Soraya'
list[5] = 'Retno'
list[9] = 'Ani'
print("Nama_3,5,9_diganti: ", list[3], list[5], list[9])

# Menambah 2 nama teman
list.append('Muti')
list.append('Syerli')
print(list)

# Menampilkan nama dengan perulangan
print(list * 2)

# Menampilkan panjang list
print(len(list))
