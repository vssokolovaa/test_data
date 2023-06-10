import pytz
from datetime import datetime
import datetime


class DateData:
    def get_time_now_string(self) -> str:
        now = datetime.datetime.now()
        return now.isoformat()

    def get_time_now_string_utc(self) -> str:
        utc_date = datetime.datetime.now(pytz.timezone("UTC"))
        return utc_date.isoformat()

