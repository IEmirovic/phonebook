# with open("file1.txt", "r") as file1:
# read_content = file1.read()
# print(read_content)

from functions import displayMenu, addFunc, delFunc, searchFunc, readFunc, exitFunc


def main():
    while True:
        try:
            displayMenu()
            choice = input('\nSeciminizi Yapiniz: ')
            if choice == '0':
                exitFunc()
                break
            elif choice == '1':
                addFunc()
            elif choice == '2':
                delFunc()
            elif choice == '3':
                searchFunc()
            elif choice == '4':
                readFunc()
            else:
                print('Gecersiz Secim. Tekrar Deneyiniz.')

        except Exception as hata:
            # Exception sinifini "hata" degiskenine atadim
            print(f'Hata: {hata}')


if __name__ == "__main__":
    main()
