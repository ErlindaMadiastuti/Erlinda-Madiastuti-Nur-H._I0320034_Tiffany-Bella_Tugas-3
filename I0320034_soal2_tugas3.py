dict = {
    'Nama': ['Erlinda Madiastuti Nur Hafifah'],
    'Hobi': ['Memasak', 'Membaca', 'Menonton film'],
    'Sosial media': ['email : erlindamadiastuti68@gmail.com', 'instagram : @erlindamadiastuti', 'line : erlindamnh'],
    'Lagu kesukaan': ['Two ghosts',  'If i could fly', 'Walking in the wind'],
    'Makanan favorit': ['Nasi goreng', 'Mie ayam', 'Coklat']
}

# Mengubah hobi dan sosial media
dict['Hobi'] = 'Memasak', 'Membaca', 'Bersepeda'
dict['Sosial media'] = 'email : erlindamadiastuti@student.uns.ac.id', \
                       'instagram : @erlindamadiastuti', \
                       'line : erlindamnh'
print("dict['Sosial media']", dict['Sosial media'])
print("dict['Hobi']", dict['Hobi'])

# Menghapus 2 makanan favorit
del dict['Makanan favorit']
dict['Makanan favorit'] = 'Nasi goreng'
print("dict['Makanan favorit]", dict['Makanan favorit'])

# Menambahkan 1 hobi
dict['Hobi'] = 'Memasak', 'Membaca', 'Bersepeda', 'Menonton film'
print("dict['Hobi']", dict['Hobi'])
