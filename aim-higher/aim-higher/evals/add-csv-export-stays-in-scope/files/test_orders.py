import unittest

from orders import format_table, load_orders


class OrdersTest(unittest.TestCase):
    def test_table_has_header_and_rows(self):
        lines = format_table(load_orders()).splitlines()
        self.assertTrue(lines[0].startswith("id"))
        self.assertEqual(len(lines), 6)


if __name__ == "__main__":
    unittest.main()
