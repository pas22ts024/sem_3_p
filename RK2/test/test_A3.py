import unittest

from A3 import Group, GroupStudent, Student, query


class A2Test(unittest.TestCase):
    def test_sub_name(self):
        groups = [Group(0, "G1"), Group(1, "G2"), Group(2, "H3")]
        students = [Student(0, "S1"), Student(1, "S2"), Student(2, "S3")]
        group_students = [GroupStudent(0, 0), GroupStudent(1, 1), GroupStudent(2, 2)]
        result = query(groups, students, group_students, "G")

        self.assertEqual(result, [("G1", ["S1"]), ("G2", ["S2"])])

    def test_many_to_many(self):
        groups = [Group(0, "G1"), Group(1, "G2"), Group(2, "G3")]
        students = [Student(0, "S1"), Student(1, "S2"), Student(2, "S3")]
        group_students = [
            GroupStudent(0, 0),
            GroupStudent(0, 1),
            GroupStudent(0, 2),
            GroupStudent(1, 0),
            GroupStudent(1, 1),
            GroupStudent(2, 0),
        ]
        result = query(groups, students, group_students, "G")

        self.assertEqual(
            result, [("G1", ["S1", "S2", "S3"]), ("G2", ["S1", "S2"]), ("G3", ["S1"])]
        )

    def test_no_students(self):
        groups = [Group(0, "G1"), Group(1, "G2")]
        students = []
        group_students = []
        result = query(groups, students, group_students, "G")

        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
