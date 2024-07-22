class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self,new_floor: int):
        if new_floor > self.number_of_floors or new_floor < 1:
                print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

    def __eq__(self, new_floor):
        return self.number_of_floors == new_floor

    def __lt__(self, new_floor):
        return self.number_of_floors < new_floor

    def __le__(self, new_floor):
        return self.number_of_floors <= new_floor

    def __gt__(self, new_floor):
        return self.number_of_floors > new_floor

    def __ge__(self, new_floor):
        return self.number_of_floors >= new_floor

    def __ne__(self, new_floor):
        return self.number_of_floors != new_floor

    def __add__(self, value: int):
        self.number_of_floors += value
        return self

    def __radd__(self, value: int):
        return self.__add__(value)

    def __iadd__(self, value: int):
        return self.__add__(value)


#h1 = House('ЖК Горский', 18)
#h2 = House('Домик в деревне', 2)
#h1.go_to(5)
#h2.go_to(10)


#h1 = House('ЖК Эльбрус', 10)
#h2 = House('ЖК Акация', 20)

# __str__
#print(h1)
#print(h2)

# __len__
#print(len(h1))
#print(len(h2))


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__