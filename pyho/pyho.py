# -*- coding: utf-8 -*-

import datetime


def laugh() -> str:
    return 'hohoho'


def yyyymmdd_to_dt(yyyymmdd: int) -> datetime.date:
    """
    Convert date integer into date object.
    eg, 20151225 -> date(2015, 12, 25)

    :param yyyymmdd: date in integer
    :return: datetime.date object
    """

    year = int(yyyymmdd / 10000)
    month = int((yyyymmdd % 10000) / 100)
    day = int(yyyymmdd % 100)

    return datetime.date(year, month, day)
