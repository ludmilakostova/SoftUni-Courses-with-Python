import unittest

from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def test_init_attributes(self):
        car = Vehicle(50.5, 140.0)
        default_fuel_consumption = 1.25
        self.assertEqual(50.5, car.fuel)
        self.assertEqual(140.0, car.horse_power)
        self.assertEqual(50.5, car.capacity)
        self.assertEqual(default_fuel_consumption, car.fuel_consumption)

    def test_drive_with_enough_fuel(self):
        car = Vehicle(50.5, 140.0)
        self.assertEqual(50.5, car.fuel)
        car.drive(10)
        self.assertEqual(38, car.fuel)

    def test_drive_with_no_fuel(self):
        car = Vehicle(0, 140.0)
        with self.assertRaises(Exception) as ex:
            car.drive(10)
        self.assertEqual('Not enough fuel', str(ex.exception))

    def test_drive_without_enough_fuel(self):
        car = Vehicle(50.5, 140.0)
        with self.assertRaises(Exception) as ex:
            car.drive(100)
        self.assertEqual('Not enough fuel', str(ex.exception))

    def test_refuel_in_capacity(self):
        car = Vehicle(50.5, 140.0)
        self.assertEqual(50.5, car.fuel)
        self.assertEqual(50.5, car.capacity)
        car.drive(10)
        car.refuel(10)
        self.assertEqual(48, car.fuel)

    def test_refuel_with_more_than_capacity(self):
        car = Vehicle(50.5, 140.0)
        self.assertEqual(50.5, car.fuel)
        self.assertEqual(50.5, car.capacity)
        with self.assertRaises(Exception) as ex:
            car.refuel(10)
        self.assertEqual('Too much fuel', str(ex.exception))

    def test_str_representation(self):
        car = Vehicle(50.5, 140.0)
        self.assertEqual('The vehicle has 140.0 horse power with 50.5 fuel left and 1.25 fuel consumption', car.__str__())



if __name__ == '__main__':
    unittest.main()