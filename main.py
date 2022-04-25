from application import salary
from application.db import people
from datetime import datetime as dt


if __name__ == '__main__':
    print(dt.now())
    salary.calculate_salary()
    people.get_employees()


