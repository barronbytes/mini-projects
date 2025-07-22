import unittest
import os
from etl_load import Load


class TestLoad(unittest.TestCase):
    def setUp(self):
        self.cwd = os.path.dirname(os.path.relpath(__file__))
        self.file = "test_sleep_hours.json"
        self.days = ["Friday", "Saturday", "Sunday"]
        self.hours = [6, 8, 4]
        self.out_path = os.path.join(Load.DST_DIR, self.file.replace(".json", ".png"))


    def tearDown(self):
        if os.path.exists(self.out_path):
            os.remove(self.out_path)


    def test_cwd_in_code_dir(self):
        self.assertTrue(self.cwd in Load.SUBFOLDER_DIR)


    def test_visualization_saved(self):
        Load.create_bar_graph(file_name=self.file, data_labels=self.days, data_counts=self.hours)
        self.assertTrue(os.path.exists(self.out_path))


if __name__ == "__main__":
    unittest.main()
