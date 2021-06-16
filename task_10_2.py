class ClothClothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def coat_main(self):
        return f'Пальто - {self.size/6.5 + 0.5}'

    def costume_main(self):
        return f'Костюм - {2*self.height + 0.3}'

    @property
    def full_cloth(self):
        return str(f'Всего ткани \n'
                   f' {(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(ClothClothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.cloth_coat = round(self.size / 6.5 + 0.5)

    def __str__(self):
        return f'Ткани на пальто {self.cloth_coat}'


class Costume(ClothClothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.cloth_costume = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Ткани на костюм {self.cloth_costume}'


coat = Coat(3, 5)
costume = Costume(2, 4)
print(coat)
print(costume)
print(coat.full_cloth)
print(coat.coat_main())
print(costume.full_cloth)
print(costume.costume_main())
