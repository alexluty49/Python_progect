from random import choice
import random
def password(stroka):
    res = len (stroka)
    while res <6:
        res = len(stroka)
        special = ["1", "2", "3", "4","5", "?", "#", "$"]
        s = choice(special)
        stroka = stroka + s
        print(stroka)
    a = stroka.replace("O", "0")
    b = a.replace("o", "0")
    char_list = []
    for i in b:
        char_list.append(i)
        random.shuffle(char_list)
        print(char_list)

password(input("Добавить слово:"))
