from lecture_4.task_1 import get_country
from lecture_4.task_2 import get_geo
from lecture_4.task_3 import max_value
import unittest


class test_lecture4(unittest.TestCase):
    def test_task1(self):
        result = get_country()
        self.assertEqual(
            result,
            [
                {"visit1": ["Москва", "Россия"]},
                {"visit3": ["Владимир", "Россия"]},
                {"visit7": ["Тула", "Россия"]},
                {"visit8": ["Тула", "Россия"]},
                {"visit9": ["Курск", "Россия"]},
                {"visit10": ["Архангельск", "Россия"]},
            ],
        )

    def test_task2(self):
        result = get_geo()
        self.assertEqual(result, [98, 35, 213, 54, 119, 15])

    def test_task3(self):
        result = max_value()
        self.assertEqual(result, "Канал с максимальным обьемом продаж: yandex")


if __name__ == "__main__":
    unittest.main()
