import datetime
import calendar
from datetime import timedelta
import pycron


class CalendarClient:
    def __init__(self):
        pass

    def days_in_month(self) -> int:
        y, m, d = self.today_ymd()
        rng = calendar.monthrange(y, m)
        return rng[1] - d

    def month_range(self) -> tuple:
        y, m, d = self.today_ymd()
        rng = calendar.monthrange(y, m)
        # '+1' - it since the right border is not taken
        return (d, rng[1]+1)

    def today_ymd(self) -> list:
        today = datetime.date.today()
        return [int(x) for x in today.strftime("%Y-%m-%d").split('-')]

    def rest_of_month(self) -> list:
        rest_of_month = []
        cal_range = self.month_range()
        y, m, d = self.today_ymd()
        for i in range(*cal_range):
            date_str = f'{y}-{m}-{i}'
            date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
            rest_of_month.append(date_obj)
        return rest_of_month

    def is_cron_date(self, period: str, start: datetime, end: datetime = None) -> bool:
        if end is None:
            end = start + timedelta(days=1)
        return pycron.has_been(period, start, end)

    def is_date(self, period: str, start: datetime, end: datetime = None) -> bool:
        if end is None:
            end = start + timedelta(days=1)
        date_obj = datetime.datetime.strptime(period, '%Y-%m-%d')
        return start <= date_obj and date_obj <= end
