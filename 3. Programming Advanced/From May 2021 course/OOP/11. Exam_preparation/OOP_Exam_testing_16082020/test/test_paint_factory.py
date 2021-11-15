from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    def setUp(self):
        self.paint_factory = PaintFactory("Lala", 100)

    def test_init_attributes(self):
        self.assertEqual("Lala", self.paint_factory.name)
        self.assertEqual(100, self.paint_factory.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.paint_factory.valid_ingredients)
        self.assertEqual({}, self.paint_factory.ingredients)

    def test_add_ingredients_not_in_the_valid_range(self):
        with self.assertRaises(TypeError) as ex:
            self.paint_factory.add_ingredient("purple", 50)
        self.assertEqual("Ingredient of type purple not allowed in PaintFactory", str(ex.exception))

    def test_add_ingredients_in_range_and_enough_capacity_with_new_item(self):
        self.assertEqual({}, self.paint_factory.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.paint_factory.valid_ingredients)
        self.paint_factory.add_ingredient("white", 50)
        self.assertEqual({'white': 50}, self.paint_factory.ingredients)

    def test_add_ingredients_in_range_with_existing_item_and_enough_capacity(self):
        self.paint_factory.ingredients = {"white": 20}
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.paint_factory.valid_ingredients)
        self.paint_factory.add_ingredient("white", 50)
        self.assertEqual({'white': 70}, self.paint_factory.ingredients)

    def test_add_ingredients_in_range_without_capacity(self):
        self.assertEqual(100, self.paint_factory.capacity)
        self.assertEqual({}, self.paint_factory.ingredients)
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.add_ingredient('white', 150)
        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_remove_ingredients_not_in_the_attribute_ingredients(self):
        self.paint_factory.ingredients = {'white': 20, 'red': 50}
        with self.assertRaises(KeyError) as ex:
            self.paint_factory.remove_ingredient('yellow', 10)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))

    def test_remove_ingredients_in_the_attribute_letting_enough_quantity(self):
        self.paint_factory.ingredients = {'white': 20, 'red': 50}
        self.paint_factory.remove_ingredient('white', 10)
        self.assertEqual({"white": 10, 'red': 50}, self.paint_factory.ingredients)

    def test_remove_ingredients_in_the_attribute_without_enough_quantity(self):
        self.paint_factory.ingredients = {'white': 20, 'red': 50}
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.remove_ingredient('white', 30)
        self.assertEqual('Ingredients quantity cannot be less than zero', str(ex.exception))

    def test_prop_products(self):
        self.assertEqual({}, self.paint_factory.ingredients)
        self.assertEqual({}, self.paint_factory.products)

    def test_repr_method(self):
        self.paint_factory.ingredients = {'white': 20, 'red': 50}
        result = ''
        result += 'Factory name: Lala with capacity 100.\n'
        result += 'white: 20\nred: 50\n'
        self.assertEqual(result, repr(self.paint_factory))


if __name__ == "__main__":
    main()
