# program array

contacts = [['Budi','081235648951']]
backtoMenu = 'y'

def showContacts(contacts):
    for person in contacts:
        print()
        print('<<<<<<<<<< Daftar Kontak >>>>>>>>>>')
        print('Nama :'+person[0])
        print('No Telepon : '+person[1])
        print('<<<<<<<<<<<<<<<<<->>>>>>>>>>>>>>>>>')
        print()

    return input('kembali ke menu (y/n) ? ')


def addContacts(name,phoneNumber):
    contacts.append([name,phoneNumber])
    print('Kontak berhasil ditambahkan')
    print()

    return input('kembali ke menu (y/n) ? ')


def menu():
    print()
    print('----- Menu -----')
    print('1. Daftar Kontak')
    print('2. Tambah Kontak')
    print('3. Keluar')
    print('----------------')

while(True):
    if (backtoMenu == 'y' or backtoMenu == 'Y'):
        menu()
        pilih = input('pilihan anda: ')
    else :
        pilih = '3'

    if (pilih == '1'):
        backtoMenu = showContacts(contacts)
    elif (pilih == '2'):
        backtoMenu = addContacts(input('Nama : '),input('No Telepon : '))
    elif (pilih == '3'):
        print('Program selesai, sampai jumpa!')
        break
    else:
        print('Menu tidak tersedia')
        break

