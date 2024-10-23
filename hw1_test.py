import data
import hw1
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    class TestCases(unittest.TestCase):
        def test_vowel_count(self):
            self.assertEqual(hw1.vowel_count("hello"), 2)
            self.assertEqual(hw1.vowel_count("sky"), 0)

    # Part 2
    def test_short_lists(self):
        self.assertEqual(hw1.short_lists([[1, 2], [3], [4, 5, 6], [7, 8]]), [[1, 2], [7, 8]])
        self.assertEqual(hw1.short_lists([[1, 2], [3, 4], [5]]), [[1, 2], [3, 4]])

    # Part 3
    def test_ascending_pairs(self):
        self.assertEqual(hw1.ascending_pairs([[3, 2], [1, 4], [5]]), [[2, 3], [1, 4], [5]])
        self.assertEqual(hw1.ascending_pairs([[5, 1], [2], [7, 8]]), [[1, 5], [2], [7, 8]])
    # Part 4
    def test_add_prices(self):
        price1 = hw1.Price(5, 50)
        price2 = hw1.Price(3, 75)
        self.assertEqual(hw1.add_prices(price1, price2), hw1.Price(9, 25))
        price3 = hw1.Price(2, 80)
        price4 = hw1.Price(4, 30)
        self.assertEqual(hw1.add_prices(price3, price4), hw1.Price(7, 10))

    # Part 5
    def test_rectangle_area(self):
        rect1 = hw1.Rectangle(0, 0, 5, 5)
        self.assertEqual(hw1.rectangle_area(rect1), 25)  # Area = 5 * 5
        rect2 = hw1.Rectangle(1, 1, 4, 3)
        self.assertEqual(hw1.rectangle_area(rect2), 6)


    # Part 6
    def test_books_by_author(self):
        book1 = hw1.Book("Book A", "Author X")
        book2 = hw1.Book("Book B", "Author Y")
        books = [book1, book2]
        self.assertEqual(hw1.books_by_author("Author X", books), [book1])
        self.assertEqual(hw1.books_by_author("Author Z", books), [])


     # Part 7
    def test_circle_bound(self):
        rect = hw1.Rectangle(0, 0, 4, 4)
        bounding_circle = hw1.circle_bound(rect)
        self.assertEqual(bounding_circle.radius, 2.8284271247461903)
        self.assertEqual(bounding_circle.center_x, 2)
        self.assertEqual(bounding_circle.center_y, 2)

    # Part 8
    def test_below_pay_average(self):
        emp1 = hw1.Employee("Alice", 50000)
        emp2 = hw1.Employee("Bob", 60000)
        emp3 = hw1.Employee("Charlie", 70000)
        employees = [emp1, emp2, emp3]
        self.assertEqual(hw1.below_pay_average(employees), ["Alice"])
        emp4 = hw1.Employee("David", 30000)
        employees.append(emp4)
        self.assertEqual(hw1.below_pay_average(employees), ["Alice", "David"])




if __name__ == '__main__':
    unittest.main()
