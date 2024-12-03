import unittest

from A2 import Group, Student, query


class A2Test(unittest.TestCase):
    def test_sum(self):
        groups = [Group(0, "G1"), Group(1, "G2")]
        students = [
            Student(0, "S1", 1, 5),
            Student(1, "S2", 0, 3),
            Student(2, "S3", 1, 4),
        ]
        result = query(groups, students)

        self.assertEqual(result, [("G1", 3), ("G2", 9)])

    def test_reverse(self):
        groups = [Group(0, "G1"), Group(1, "G2")]
        students = [
            Student(0, "S1", 0, 5),
            Student(1, "S2", 1, 3),
            Student(2, "S3", 0, 4),
        ]
        result = query(groups, students)

        self.assertEqual(result, [("G2", 3), ("G1", 9)])

    def test_no_students(self):
        groups = [Group(0, "G1"), Group(1, "G2")]
        students = []
        result = query(groups, students)

        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
