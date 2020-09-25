from prettytable import PrettyTable
tbl = PrettyTable()
tbl.field_names = ['Makanan / Minuman', 'Harga']

f = open('dapur.txt', 'r')
konten = f.readlines()

for s in konten:
    list_konten = s.split('#')
    angka = int(list_konten[1])
    angka = '{:20,.2f}'.format(angka)
    tbl.add_row(list_konten)
f.close()


print(tbl)
