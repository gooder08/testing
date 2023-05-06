from ya_disk.ya import ya_disk_create_folder
from ya_disk.ya import ya_auth
from ya_disk.ya import delete_folder
import unittest



class api_ya(unittest.TestCase):
    # Проверка на существование папки на диске
    def test_exist_folder(self):
        result = ya_disk_create_folder()
        self.assertEqual(result, 201)
    # Проверка на код ответа 200
    def test_auth(self):
        result = ya_auth()
        self.assertEqual(result, 200)

    # Проверка на удаление папки, если папка не найдена, то тест - успешен
    @unittest.expectedFailure
    def test_delete_folder(self):
        result = delete_folder()
        self.assertEqual(result, 204)
        





if __name__ == "__main__":
    unittest.main()