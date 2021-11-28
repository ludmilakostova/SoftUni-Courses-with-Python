from unittest import TestCase, main

from project.train.train import Train


class TestTrain(TestCase):
    def setUp(self):
        self.train = Train("Mila", 300)

    def test_init_attributes(self):
        self.assertEqual("Mila", self.train.name)
        self.assertEqual(300, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_class_attributes(self):
        self.assertEqual("Train is full", Train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", Train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", Train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", Train.PASSENGER_ADD)
        self.assertEqual("Removed {}", Train.PASSENGER_REMOVED)
        self.assertEqual(0, Train.ZERO_CAPACITY)

    def test_add_passenger_while_train_is_full(self):
        self.train.passengers = ["Mila", "Julie", "Peter"]
        self.train.capacity = 3
        with self.assertRaises(ValueError) as ex:
            self.train.add("Marie")
        self.assertEqual("Train is full", str(ex.exception))

    def test_add_passenger_with_already_the_same_name(self):
        self.train.passengers = ["Mila", "Julie", "Peter"]
        self.train.capacity = 50
        with self.assertRaises(ValueError) as ex:
            self.train.add("Julie")
        self.assertEqual("Passenger Julie Exists", str(ex.exception))

    def test_add_passenger_with_new_name_and_enough_capacity(self):
        self.train.passengers = ["Mila", "Julie", "Peter"]
        self.assertEqual(300, self.train.capacity)
        result = self.train.add("Rod")
        self.assertEqual(["Mila", "Julie", "Peter", "Rod"], self.train.passengers)
        self.assertEqual("Added passenger Rod", result)

    def test_remove_not_existing_passenger(self):
        self.train.passengers = ["Mila", "Julie", "Peter"]
        with self.assertRaises(ValueError) as ex:
            self.train.remove("Lucia")
        self.assertEqual("Passenger Not Found", str(ex.exception))

    def test_remove_existing_passenger(self):
        self.train.passengers = ["Mila", "Julie", "Peter"]
        result = self.train.remove("Julie")
        self.assertEqual("Removed Julie", result)


if __name__ == "__main__":
    main()