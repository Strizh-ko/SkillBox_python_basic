import time


class Date:
    cur_date = None

    @classmethod
    def is_date_valid(cls, test_date: str) -> bool:
        try:
            cls.cur_date = time.strptime(test_date, '%d-%m-%Y')
        except ValueError:
            return False
        return True

    @classmethod
    def from_string(cls, test_date: str) -> str:
        check = Date.is_date_valid(test_date)
        if check:
            cur_date = time.strftime('День: %d\tМесяц: %m\tГод: %Y', cls.cur_date)
            return cur_date
        else:
            return 'Невозможно преобразовать не корректную дату!'


date = Date.from_string('10-12-2077')
print(date)
date = Date.from_string('40-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))