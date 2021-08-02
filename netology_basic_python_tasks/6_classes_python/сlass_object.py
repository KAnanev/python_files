class Animals:
    satiety = 0
    name_ref = []

    def __init__(self, name, weight):
        self.sound_animal = None
        self.name = name
        self.weight = weight
        Animals.name_ref.append(self)

    def feed(self, value):
        self.satiety += value

    def sound(self):
        print(self.sound_animal)


class Bird(Animals):
    def pick_eggs(self):
        print(f" У {self.name} собраны яйца")


class Goose(Bird):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.sound_animal = 'Kryaaaa'


class Duck(Goose):
    pass


class Chicken(Bird):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.sound_animal = 'Koko'


class Mammal(Animals):
    def milk(self):
        print(self.name + " подоена")


class Cow(Mammal):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.sound_animal = 'Muuuuu'


class Goat(Mammal):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.sound_animal = 'Beeeee'


class Sheep(Goat):
    def cut(self):
        print(f"{self.name} подстрижен")


my_goose_grey = Goose("Серый", 7)
my_goose_white = Goose("Белый", 10)
my_cow = Cow("Манька", 300)
my_sheep_lamb = Sheep("Барашек", 53)
my_sheep_curly = Sheep("Кудрявый", 53)
my_chicken_coco = Chicken("Коко", 3)
my_chicken_kukareku = Chicken("Кукареку", 2)
my_goat_horns = Goat("Рога", 45)
my_goat_hoof = Goat("Копыто", 45)
my_duck = Duck("Кряква", 8)

list_name = [x.name for x in Animals.name_ref]
list_weight = [x.weight for x in Animals.name_ref]
max_index = list_weight.index(max(list_weight))
print(f"Общий вес всех животных {sum(list_weight)}, имя самого тяжелого животного {list_name[max_index]}.")
