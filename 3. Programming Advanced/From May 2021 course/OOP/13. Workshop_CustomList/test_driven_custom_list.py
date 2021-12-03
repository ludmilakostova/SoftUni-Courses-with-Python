from unittest import TestCase, main

from custom_list import CustomList


class TestCustomList(TestCase):
    def setUp(self):
        self.custom_list = CustomList(1, 2, 3)

    def test_init_attributes(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)

    def test_append_add_element_at_the_end(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        self.custom_list.append(5)
        self.assertEqual([1, 2, 3, 5], self.custom_list._CustomList__values)
        self.assertEqual(5, self.custom_list._CustomList__values[-1])

    def test_append_without_value_raises(self):
        with self.assertRaises(TypeError) as ex:
            self.custom_list.append()
        self.assertIn("append()", str(ex.exception))

    def test_append_if_empty_list(self):
        cl = CustomList()
        self.assertEqual([], cl._CustomList__values)
        cl.append(5)
        self.assertEqual([5], cl._CustomList__values)

    def test_append_does_not_return_a_value(self):
        res = self.custom_list.append(5)
        self.assertIsNone(res)

    def test_remove_element_at_index(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        self.assertEqual(1, self.custom_list._CustomList__values[0])
        self.custom_list.remove(0)
        self.assertEqual([2, 3], self.custom_list._CustomList__values)
        self.assertEqual(2, self.custom_list._CustomList__values[0])

    def test_remove_index_not_existing_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.custom_list.remove(10)
        self.assertEqual("Invalid index", str(ex.exception))

    def test_remove_return(self):
        el = self.custom_list.remove(0)
        self.assertIsNotNone(el)
        self.assertEqual(1, el)

    def test_get_returns_element(self):
        el = self.custom_list.get(0)
        self.assertIsNotNone(el)
        self.assertEqual(1, el)

    def test_get_invalid_index(self):
        with self.assertRaises(IndexError) as ex:
            self.custom_list.get(100)
        self.assertEqual("Invalid index", str(ex.exception))

    def test_extend_with_iterable_values(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        self.custom_list.extend([4, 5])
        self.assertEqual([1, 2, 3, 4, 5], self.custom_list._CustomList__values)
        self.custom_list.extend((100, 200))
        self.assertEqual([1, 2, 3, 4, 5, 100, 200], self.custom_list._CustomList__values)
        self.custom_list.extend({100, 200})
        self.assertEqual([1, 2, 3, 4, 5, 100, 200, 200, 100], self.custom_list._CustomList__values)

    def test_extend_with_empty_list(self):
        cl = CustomList()
        self.assertEqual([], cl._CustomList__values)
        cl.extend([1, 2])
        self.assertEqual([1, 2], cl._CustomList__values)

    def test_extend_and_return_new_list(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        res = self.custom_list.extend([4, 5])
        self.assertEqual([1, 2, 3, 4, 5], self.custom_list._CustomList__values)
        self.assertEqual([1, 2, 3, 4, 5], res)
        self.assertNotEqual(id(self.custom_list._CustomList__values), id(res))

    def test_extend_with_non_iterable(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        self.custom_list.extend(4)
        self.assertEqual([1, 2, 3, 4], self.custom_list._CustomList__values)

    def test_insert_value_at_valid_index_and_shift_right(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        self.assertEqual(1, self.custom_list._CustomList__values[0])
        self.custom_list.insert(0, 5)
        self.assertEqual([5, 1, 2, 3], self.custom_list._CustomList__values)
        self.assertEqual(5, self.custom_list._CustomList__values[0])
        self.assertEqual(1, self.custom_list._CustomList__values[1])

    def test_insert_value_at_invalid_index(self):
        with self.assertRaises(IndexError) as ex:
            self.custom_list.insert(6, 100)
        self.assertEqual("Invalid index", str(ex.exception))

    def test_pop_remove_last_el_and_return_it(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        self.assertEqual(3, self.custom_list._CustomList__values[-1])
        res = self.custom_list.pop()
        self.assertEqual([1, 2], self.custom_list._CustomList__values)
        self.assertEqual(3, res)

    def test_pop_with_empty_value_raises(self):
        cl = CustomList()
        with self.assertRaises(IndexError) as ex:
            cl.pop()
        self.assertEqual("Empty List", str(ex.exception))

    def test_clear_all_values(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        self.custom_list.clear()
        self.assertEqual([], self.custom_list._CustomList__values)

    def test_index_return_value(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        self.assertEqual(1, self.custom_list._CustomList__values[0])
        res = self.custom_list.index(1)
        self.assertIsNotNone(res)
        self.assertEqual(0, res)

    def test_index_with_non_existing_value_raises(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        self.assertNotIn(100, self.custom_list._CustomList__values)
        with self.assertRaises(ValueError) as ex:
            self.custom_list.index(100)
        self.assertEqual("Nonexistent value", str(ex.exception))

    def test_reverse_the_value(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        res = self.custom_list.reverse()
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        self.assertEqual([3, 2, 1], res)

    def test_copy_same_elements_different_id(self):
        res = self.custom_list.copy()
        self.assertEqual(res, self.custom_list._CustomList__values)
        self.assertNotEqual(id(res), id(self.custom_list))

    def test_size_list(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        res = self.custom_list.size()
        self.assertEqual(3, res)

    def test_size_if_empty_list(self):
        cl = CustomList()
        self.assertEqual([], cl._CustomList__values)
        res = cl.size()
        self.assertEqual(0, res)

    def test_add_first_value(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        self.assertEqual(1, self.custom_list._CustomList__values[0])
        res = self.custom_list.add_first(10)
        self.assertEqual(10, self.custom_list._CustomList__values[0])

    def test_dictionize(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        res = self.custom_list.dictionize()
        self.assertEqual({1: 2, 3: " "}, res)

    def test_dictionize_with_even_length_list(self):
        cl = CustomList(1, 2, 3, 4)
        self.assertEqual([1, 2, 3, 4], cl._CustomList__values)
        res = cl.dictionize()
        self.assertEqual({1: 2, 3: 4}, res)

    def test_move_amount(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        res = self.custom_list.move(2)
        self.assertEqual([3, 1, 2], res)

    def test_move_amount_with_bigger_length_than_list(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        res = self.custom_list.move(7)
        self.assertEqual("Amount to big - list unchanged", res)

    def test_sum_with_int(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__values)
        res = self.custom_list.sum()
        self.assertEqual(6, res)

    def test_sum_with_int_and_string(self):
        self.custom_list._CustomList__values = [1, 2, 3, "mila"]
        res = self.custom_list.sum()
        self.assertEqual(10, res)


if __name__ == "__main__":
    main()
