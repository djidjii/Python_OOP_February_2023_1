from project.booths.private_booth import Booth


class OpenBooth(Booth):

    @property
    def get_price_pre_person(self):
        return 2.50

    def reserved(self, number_of_people: int) -> None:
        self.price_for_reservation= number_of_people * self.get_price_pre_person
        self.is_reserved = True
