import unittest
from dicesimulator import die_face_generator


class TestDieFaceGenerator(unittest.TestCase):
    def test_face(self):
        # check outputs of function against expected die faces.
        face_dict = {1: "-----------\n"
                        "|         |\n"
                        "|    o    |\n"
                        "|         |\n"
                        "-----------",
                     2: "-----------\n"
                        "|         |\n"
                        "|  o   o  |\n"
                        "|         |\n"
                        "-----------",
                     3: "-----------\n"
                        "|    o    |\n"
                        "|    o    |\n"
                        "|    o    |\n"
                        "-----------",
                     4: "-----------\n"
                        "|  o   o  |\n"
                        "|         |\n"
                        "|  o   o  |\n"
                        "-----------",
                     5: "-----------\n"
                        "|  o   o  |\n"
                        "|    o    |\n"
                        "|  o   o  |\n"
                        "-----------",
                     6: "-----------\n"
                        "|  o   o  |\n"
                        "|  o   o  |\n"
                        "|  o   o  |\n"
                        "-----------",
                     }
        self.assertEqual(die_face_generator(1), face_dict[1])
        self.assertEqual(die_face_generator(2), face_dict[2])
        self.assertEqual(die_face_generator(3), face_dict[3])
        self.assertEqual(die_face_generator(4), face_dict[4])
        self.assertEqual(die_face_generator(5), face_dict[5])
        self.assertEqual(die_face_generator(6), face_dict[6])
        self.assertEqual(die_face_generator(False), "This number doesn't exist on a regular die..?")
        self.assertEqual(die_face_generator(2.4), "This number doesn't exist on a regular die..?")
        self.assertEqual(die_face_generator("Hello"), "This number doesn't exist on a regular die..?")
