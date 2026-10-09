while True:
    buyruq1 = input('Loginni kiriting: ')
    if buyruq1 == "Abdurazzoq":
        while True:
            yosh = int(input('Parolni kiriting: '))
            if yosh == 5078:
                print("Xush kelibsiz!")
                break
            else:
                davom = input("Noto'g'ri parol kiritildi. Parolni qayta kiriting. ")
                if davom.lower() == "stop":
                    break
        break
    else:
        davom = input("Noto'g'ri login kiritildi. Loginni qayta kiriting. ")
        if davom.lower() == "stop":
            break
