from datetime import datetime
import pycron


class CronClient:
    def __init__(self):
        pass

    def is_today(self, period=None):
        # TODO: need to unmock
        tst = '2021-08-13'
        dt_obj = datetime.strptime(tst, '%Y-%m-%d')
        tst2 = '2021-08-14'
        dt_obj2 = datetime.strptime(tst2, '%Y-%m-%d')
        return pycron.has_been(period, dt_obj, dt_obj2)
