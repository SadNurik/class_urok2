class Zoo:
    def __init__(self, animal_1, animal_2, animal_3):
        self.animal_1 = animal_1
        self.animal_2 = animal_2
        self.animal_3 = animal_3

a = Zoo("Тигр", "Бегемот", "Жираф")
print(a.animal_1, a.animal_2, a.animal_3)
a.animal_1 = "Лев"
print(a.animal_1)
a.animal_4 = [a.animal_2, a.animal_3]
print(a.animal_4)
a.animal_3 = "Змея"
print(a.animal_3)