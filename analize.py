import pickle


arr = []
file = open('databin.dat','rb')
num = pickle.load(file)

while True:
    print("Введите номер операции")
    print("1 - сортирока по номеру комнат")
    print("2 - вывод работников по номеру комнаты")
    print("3 - вывод работников по номеру телефона")
    print("4 - выводит номер телефона по номеру комнаты")
    print("5 - по фамилии выводит номер телефона и номер комнаты")
    k = int(input())
    if k == 1:
        pass
    elif k == 2:
        pass
    elif k == 3:
        pass
    elif k == 4:
        pass
    elif k == 5:
        pass