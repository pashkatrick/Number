from datetime import datetime, timedelta
import pycron


class CronClient:
    def __init__(self):
        pass

    def is_in(self, period: str, start: datetime, end: datetime = None) -> bool:
        if end is None:
            end = start + timedelta(days=1)
        return pycron.has_been(period, start, end)
