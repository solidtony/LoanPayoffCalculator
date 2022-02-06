"""Pay schedule."""
from abc import ABC, abstractmethod

from typing import List

from datetime import date as Date

class PaySchedule(ABC):
    """Pay schedule abstract class."""
    def __init__(self, base_date:Date, *base_dates:List[Date]):
        self.base_dates = [base_date]+list(base_dates)

    @property
    def base_dates(self) -> List[Date]:
        return self._base_dates

    @base_dates.setter
    def base_dates(self, base_dates:List[Date]):
        self._base_dates = base_dates

    @staticmethod
    @abstractmethod
    def are_dates_valid(check_dates:List[Date]) -> bool:
        pass



class DummyPaySchedule(PaySchedule):
    @staticmethod
    def are_dates_valid(check_dates:List[Date]) -> bool:
        """All dates are on the same day of the month, and the dates must be less than 28."""
        return True
