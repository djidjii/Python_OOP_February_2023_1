from project.animal.animal import Bird
from project.food import Meat, Fruit, Vegetable, Seed


class Owl(Bird):

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    @property
    def gained_weight(self):
        return 0.25

    @property
    def food_that_eats(self):
        return [Meat] # if food in self.food_that_eats


class Hen(Bird):

    @staticmethod
    def make_sound():
        return "Cluck"

    @property
    def gained_weight(self):
        return 0.35

    @property
    def food_that_eats(self):
        return [Meat, Fruit, Vegetable, Seed]
