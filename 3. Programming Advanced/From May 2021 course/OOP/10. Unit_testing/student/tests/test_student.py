from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("Mila", {"Math": [1, 2], "History": ["Europe", "France"]})

    def test_init_attributes_with_courses(self):
        self.assertEqual("Mila", self.student.name)
        self.assertEqual({"Math": [1, 2], "History": ["Europe", "France"]}, self.student.courses)

    def test_init_with_none_courses(self):
        student = Student("Ivo")
        self.assertEqual("Ivo", student.name)
        self.assertEqual({}, student.courses)

    def test_init_with_course_none(self):
        student = Student("Ivo", None)
        self.assertEqual("Ivo", student.name)
        self.assertEqual({}, student.courses)

    def test_enroll_adding_new_notes_to_existing_course(self):
        result = self.student.enroll("Math", [10, 20, 30])
        self.assertEqual([1, 2, 10, 20, 30], self.student.courses["Math"])
        self.assertEqual('Course already added. Notes have been updated.', result)

    def test_enroll_adding_a_new_course_with_notes(self):
        result = self.student.enroll("Geo", ['I have learned new material'])
        self.assertEqual(["I have learned new material"], self.student.courses["Geo"])
        self.assertEqual('Course and course notes have been added.', result)

    def test_enroll_adding_a_new_course_without_notes(self):
        result = self.student.enroll("Psychology", ['note_1'], "N")
        self.assertEqual([], self.student.courses["Psychology"])
        self.assertEqual('Course has been added.', result)

    def test_enroll_adding_a_new_course_with_notes_Y(self):
        result = self.student.enroll("Psychology", ['note_1'], "Y")
        self.assertEqual(['note_1'], self.student.courses["Psychology"])
        self.assertEqual('Course and course notes have been added.', result)

    def test_add_notes_to_current_course(self):
        result = self.student.add_notes("Math", 15)
        self.assertEqual([1, 2, 15], self.student.courses["Math"])
        self.assertEqual('Notes have been updated', result)

    def test_add_notes_to_not_enrolled_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Bio", "ajkdfhd")
        self.assertEqual('Cannot add notes. Course not found.', str(ex.exception))

    def test_leave_course_to_enroll_one(self):
        self.assertEqual({"Math": [1, 2], "History": ["Europe", "France"]}, self.student.courses)
        result = self.student.leave_course("Math")
        self.assertEqual({"History": ["Europe", "France"]}, self.student.courses)
        self.assertEqual('Course has been removed', result)

    def test_leave_course_to_non_enrolled_one(self):
        self.assertEqual({"Math": [1, 2], "History": ["Europe", "France"]}, self.student.courses)
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Bio")
        self.assertEqual('Cannot remove course. Course not found.', str(ex.exception))


if __name__ == "__main__":
    main()
