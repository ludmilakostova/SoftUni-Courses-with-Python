from project.pet_shop import PetShop

from unittest import TestCase, main


class TestPetShop(TestCase):
    def setUp(self):
        self.pet_shop = PetShop("Mila")

    def test_init_attributes(self):
        self.assertEqual("Mila", self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_method_with_zero_quantity(self):
        with self.assertRaises(ValueError) as ex:
            self.pet_shop.add_food("meat", 0.0)
        self.assertEqual("Quantity cannot be equal to or less than 0", str(ex.exception))

    def test_add_method_with_quantity_below_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.pet_shop.add_food("meat", -6)
        self.assertEqual("Quantity cannot be equal to or less than 0", str(ex.exception))

    def test_add_method_with_new_item(self):
        result = self.pet_shop.add_food("meat", 5.50)
        self.assertEqual({"meat": 5.50}, self.pet_shop.food)
        self.assertEqual(f'Successfully added 5.50 grams of meat.', result)

    def test_add_method_with_existing_item(self):
        self.pet_shop.food = {"meat": 5.20}
        result = self.pet_shop.add_food("meat", 4.80)
        self.assertEqual({"meat": 10.0}, self.pet_shop.food)
        self.assertEqual(f'Successfully added 4.80 grams of meat.', result)

    def test_add_new_pet(self):
        self.assertEqual([], self.pet_shop.pets)
        result = self.pet_shop.add_pet("Titi")
        self.assertEqual(["Titi"], self.pet_shop.pets)
        self.assertEqual("Successfully added Titi.", result)

    def test_add_pet_while_already_existing(self):
        self.pet_shop.pets = ["Kate", "Titi"]
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet("Titi")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_fed_pet_method_while_pet_not_in_the_shop(self):
        self.pet_shop.pets = ["Kate", "Titi"]
        self.pet_shop.food = {"meat": 5.20}
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet("meat", "Lulu")
        self.assertEqual('Please insert a valid pet name', str(ex.exception))

    def test_fed_method_with_food_not_available(self):
        self.pet_shop.pets = ["Kate", "Titi"]
        self.pet_shop.food = {"meat": 5.20}
        result = self.pet_shop.feed_pet("carrots", "Kate")
        self.assertEqual('You do not have carrots', result)

    def test_fed_method_with_quantity_below_100(self):
        self.pet_shop.food = {"meat": 5.20}
        self.pet_shop.pets = ["Kate", "Titi"]
        result = self.pet_shop.feed_pet('meat', "Kate")
        self.assertEqual({"meat": 1005.20}, self.pet_shop.food)
        self.assertEqual('Adding food...', result)

    def test_fed_method_with_quantity_above_100(self):
        self.pet_shop.food = {"meat": 500}
        self.pet_shop.pets = ["Kate", "Titi"]
        result = self.pet_shop.feed_pet('meat', "Kate")
        self.assertEqual({"meat": 400}, self.pet_shop.food)
        self.assertEqual('Kate was successfully fed', result)

    def test_fed_method_with_quantity_100(self):
        self.pet_shop.food = {"meat": 100}
        self.pet_shop.pets = ["Kate", "Titi"]
        result = self.pet_shop.feed_pet('meat', "Kate")
        self.assertEqual({"meat": 0}, self.pet_shop.food)
        self.assertEqual('Kate was successfully fed', result)

    def test_repr_with_no_pets(self):
        self.assertEqual(f'Shop Mila:\nPets: ', repr(self.pet_shop))

    def test_repr_with_pets(self):
        self.pet_shop.pets = ["Kate", "Lulu", "Titi"]
        self.assertEqual(f'Shop Mila:\nPets: Kate, Lulu, Titi', repr(self.pet_shop))


if __name__ == "__main__":
    main()
