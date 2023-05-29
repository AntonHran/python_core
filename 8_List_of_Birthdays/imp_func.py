import datetime
import typing
from birthdays_list import users, week


def get_birthdays_per_week_2(lst: typing.List[dict]) -> typing.List[dict]:
    b_list: typing.List[dict] = []
    one_week_int: typing.List[datetime] = [datetime.datetime.now().date() +
                                           datetime.timedelta(days=day) for day in
                                           range(1, 8)]
    for user in lst:
        if user['birthday'].month in [m.month for m in one_week_int] and \
                user['birthday'].day in [d.day for d in one_week_int]:
            w_day: int = datetime.datetime(year=datetime.datetime.now().year,
                                           month=user['birthday'].month,
                                           day=user['birthday'].day).weekday()
            w_day = 0 if w_day in range(5, 7) else w_day
            b_list.append({week[w_day]: user['name']})
    return b_list


print(get_birthdays_per_week_2(users))
