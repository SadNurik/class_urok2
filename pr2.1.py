class Factory:
    def engine(self):
        return ("Двигатель создан")

    def bridge(self):
        return ("Ходовая часть создана")

class Toyota(Factory):
    def wheels(self):
        return ("Колёса готовы")

    def windows(self):
        return ("Стёкла готовы")

car = Toyota()
list = [car.wheels(), car.windows(), car.engine(), car.bridge()]
print(list)