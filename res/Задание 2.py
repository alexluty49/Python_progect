def slovo(stroka):
    res = len(stroka)
    if res <5:
        des = stroka.upper()
        print(des)
    elif res > 5:
        les = stroka[::-1]
        print (les)
    else:
        print("Замена")

slovo(input("Введите слово:"))
