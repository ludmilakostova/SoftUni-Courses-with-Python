from project.student_report_card import StudentReportCard
from unittest import TestCase, main


class TestStudentReportCard(TestCase):
    def setUp(self):
        self.student_card = StudentReportCard("Mila", 12)

    def test_all_init_attributes(self):
        self.assertEqual("Mila", self.student_card.student_name)
        self.assertEqual(12, self.student_card.school_year)
        self.assertEqual({}, self.student_card.grades_by_subject)

    def test_student_name_property_with_no_name(self):
        with self.assertRaises(ValueError) as ex:
            self.student_card.student_name = ''
        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))

    def test_student_name_property(self):
        self.student_card.student_name = "Ludmila"
        self.assertEqual("Ludmila", self.student_card.student_name)

    def test_school_year_property_with_negative_value(self):
        with self.assertRaises(ValueError) as ex:
            self.student_card.school_year = -2
        self.assertEqual('School Year must be between 1 and 12!', str(ex.exception))

    def test_school_year_property_with_greater_value(self):
        with self.assertRaises(ValueError) as ex:
            self.student_card.school_year = 13
        self.assertEqual('School Year must be between 1 and 12!', str(ex.exception))

    def test_school_year_property_with_year_in_range(self):
        self.student_card.school_year = 9
        self.assertEqual(9, self.student_card.school_year)

    def test_add_new_subject_with_grade(self):
        self.student_card.add_grade("Math", 5.5)
        result = self.student_card.grades_by_subject
        self.assertEqual({"Math": [5.5]}, result)

    def test_add_grade_to_existing_subject(self):
        self.student_card.add_grade("Math", 5.5)
        self.student_card.add_grade("Math", 6.5)
        result = self.student_card.grades_by_subject
        self.assertEqual({"Math": [5.5, 6.5]}, result)

    def test_average_grade_with_none_subject(self):
        self.assertEqual('', self.student_card.average_grade_by_subject())

    def test_average_grade_by_subject_with_1(self):
        self.student_card.grades_by_subject = {"Math": [5.5]}
        result = self.student_card.average_grade_by_subject()
        self.assertEqual('Math: 5.50', result)

    def test_average_grade_with_one_subject_and_different_grades(self):
        self.student_card.grades_by_subject = {"Math": [5.5, 6.5]}
        result = self.student_card.average_grade_by_subject()
        self.assertEqual('Math: 6.00', result)

    def test_average_grade_with_2_subjects(self):
        self.student_card.grades_by_subject = {"Math": [5.5, 6.5], "French": [6.0, 5.0]}
        result = self.student_card.average_grade_by_subject()
        self.assertEqual('Math: 6.00\nFrench: 5.50', result)

    def test_average_grade_for_all_subjects_2_in_total(self):
        self.student_card.grades_by_subject = {"Math": [5.5, 6.5], "French": [6.0, 5.0]}
        result = self.student_card.average_grade_for_all_subjects()
        self.assertEqual('Average Grade: 5.75', result)

    def test_average_grade_for_all_subjects_with_one_subject(self):
        self.student_card.grades_by_subject = {"Math": [5.5, 6.5]}
        result = self.student_card.average_grade_for_all_subjects()
        self.assertEqual('Average Grade: 6.00', result)

    def test_average_grade_for_all_subjects_with_none_subject(self):
        self.assertEqual({}, self.student_card.grades_by_subject)
        with self.assertRaises(ZeroDivisionError) as ex:
            self.student_card.average_grade_for_all_subjects()
        self.assertEqual('division by zero', str(ex.exception))

    def test_representation_student_card(self):
        self.student_card.grades_by_subject = {"Math": [5.5, 6.5], "French": [6.0, 5.0]}
        result = f"Name: Mila\n" \
                 f"Year: 12\n" \
                 f"----------\n" \
                 f"Math: 6.00\nFrench: 5.50\n" \
                 f"----------\n" \
                 f"Average Grade: 5.75"
        self.assertEqual(result, repr(self.student_card))


if __name__ == "__main__":
    main()
