import pickle
class Data:
    def __init__(self, number,people ,room_num):
        self.number: str = number
        self.people = people
        self.room_number:int =room_num
with open("", 'r', encoding="UTF8") as f:
    arr = f.readlines()
number_arr = []
for i in arr:
    num = i.split()[-1]
    names = i.split()[1:len(i)]
    room_names = i.split()[0]
    number_arr.append(Data(num, names, room_names))

with open("databin.dat", 'rb') as file:
    pickle.dump(number_arr, file)