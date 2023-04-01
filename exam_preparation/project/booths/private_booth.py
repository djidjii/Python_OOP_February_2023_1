from project.booths.booth import Booth


class PrivateBooth(Booth):

    @property
    def get_price_for_one_person(self):
        return 3.50

    def reserve(self, number_of_people: int) -> None:
        self.price_for_reservation = number_of_people * self.get_price_for_one_person
        self.is_reserved = True
