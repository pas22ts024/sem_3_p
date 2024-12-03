import unittest

from A1 import Group, Student, query


class A1Test(unittest.TestCase):
    def test_reverse(self):
        groups = [Group(0, "G1"), Group(1, "G2")]
        students = [Student(0, "S1", 1), Student(1, "S2", 0)]
        result = query(groups, students)

        self.assertEqual(result, [("G1", ["S2"]), ("G2", ["S1"])])

    def test_no_students_in_group(self):
        groups = [Group(0, "G1"), Group(1, "G2")]
        students = [Student(0, "S1", 0), Student(1, "S2", 0)]
        result = query(groups, students)

        self.assertEqual(result, [("G1", ["S1", "S2"])])

    def test_no_students(self):
        groups = [Group(0, "G1"), Group(1, "G2")]
        students = []
        result = query(groups, students)

        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
