phoneBook = {}  # DICT
optionList = ['Ekle', 'Sil', 'Ara', 'Listele']  # SECENEKLER


def displayMenu():  # MENU FONKSIYONU
    print('0. Cik')
    for i, option in enumerate(optionList, start=1):
        print(f'{i}. Kisi {option}')


def exitFunc():  # CIKIS FONKSIYONU
    print('Rehber Kapatiliyor.')


def addFunc():  # KISI EKLEME FONKSIYONU
    name = input('Isim Giriniz: ').lower()
    if not name.isalpha():
        print('Gecerli Bir Isim Giriniz.\n')
        return

    if name in phoneBook:
        print('Bu kisi zaten kayitli.\n')
        return

    phoneNumber = input('Telefon Numarasi Giriniz: ')
    if not phoneNumber.isdigit():
        print('Gecerli Bir Numara Giriniz.\n')
        return

    phoneBook[name.lower()] = phoneNumber
    print('Kisi basariyla eklendi.')
    print(f'Isim: {name.lower()} - Numara: {phoneNumber}\n')


def delFunc():  # KISI SILME FONKSIYONU
    name = input('Isim Giriniz: ').lower()
    if not name.isalpha() or name not in phoneBook:
        print('Gecerli Bir Isim Giriniz.\n')
        return
    del phoneBook[name]
    print('Kisi basariyla silindi.\n')


def searchFunc():  # ARAMA FONKSIYONU
    name = input('Isim Giriniz: ').lower()
    if not name.isalpha():
        print('Gecerli Bir Isim Giriniz.\n')
        return

    if name not in phoneBook:
        print('Aradiginiz kisi rehberde yok.\n')
        return

    phoneNumber = phoneBook.get(f'{name}')
    print('-Aranan Kisi-')
    print(f'Isim: {name.lower()} - Numara: {phoneNumber}\n')


def readFunc():  # LISTELEME FONKSIYONU
    if not phoneBook:
        print('Rehberde kişi yok.\n')
        return
    print('-Kisi Listesi-')

    for name, phoneNumber in phoneBook.items():
        print(f'Isim: {name.lower()} - Numara: {phoneNumber}\n')
