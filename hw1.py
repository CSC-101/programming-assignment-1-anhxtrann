import data

# Write your functions for each part in the space below.

# Part 1
def vowel_count(s:str) -> int:
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

# Part 2
def short_lists(lst: list[list[int]]) -> list[list[int]]:
    return [sublist for sublist in lst if len(sublist) == 2]
# Part 3
def ascending_pairs(lst: list[list[int]]) -> list[list[int]]:
    return [sorted(sublist) if len(sublist) == 2 else sublist for sublist in lst]


# Part 4
class Price:
    def __init__(self, dollars: int, cents: int):
        self.dollars = dollars
        self.cents = cents

    def __repr__(self):
        return "Price(dollars={}, cents={})".format(self.dollars, self.cents)

    def __eq__(self, other):
        return self.dollars == other.dollars and self.cents == other.cents

def add_prices(price1: Price, price2: Price) -> Price:
    total_dollars = price1.dollars + price2.dollars
    total_cents = price1.cents + price2.cents

    if total_cents >= 100:
        total_dollars += 1
        total_cents -= 100

    return Price(total_dollars, total_cents)



# Part 5
class Rectangle:
    def __init__(self, top_left_x: int, top_left_y: int, bottom_right_x: int, bottom_right_y: int):
        self.top_left_x = top_left_x
        self.top_left_y = top_left_y
        self.bottom_right_x = bottom_right_x
        self.bottom_right_y = bottom_right_y

    def __repr__(self):
        return "Rectangle(top_left_x={}, top_left_y={}, bottom_right_x={}, bottom_right_y={})".format(
            self.top_left_x, self.top_left_y, self.bottom_right_x, self.bottom_right_y
        )

def rectangle_area(rect: Rectangle) -> int:
    width = rect.bottom_right_x - rect.top_left_x
    height = rect.bottom_right_y - rect.top_left_y

    if width < 0 or height < 0:
        return 0

    return width * height


# Part 6
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author


def books_by_author(author: str, books: list[Book]) -> list[Book]:
    return [book for book in books if book.author == author]

# Part 7
class Circle:
    def __init__(self, center_x: float, center_y: float, radius: float):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def __repr__(self):
        return "Circle(center_x={}, center_y={}, radius={})".format(self.center_x, self.center_y, self.radius)

def circle_bound(rect: Rectangle) -> Circle:
    center_x = (rect.top_left_x + rect.bottom_right_x) / 2
    center_y = (rect.top_left_y + rect.bottom_right_y) / 2

    radius = ((rect.top_left_x - center_x) ** 2 + (rect.top_left_y - center_y) ** 2) ** 0.5

    return Circle(center_x, center_y, radius)

# Part 8
class Employee:
    def __init__(self, name: str, pay: float):
        self.name = name
        self.pay = pay


def below_pay_average(employees: list[Employee]) -> list[str]:
    if not employees:
        return []

    average_pay = sum(employee.pay for employee in employees) / len(employees)
    return [employee.name for employee in employees if employee.pay < average_pay]


