# _*_ encoding: utf-8 _*_

import unittest
import datetime
import astropy.time


from gpsweekconverter.converter import Converter


class TestConverter(unittest.TestCase):

    def setUp(self) -> None:
        self.converter = Converter()

    def test_given_correct_parameter_convert_julian_date_to_gps_week(self) -> None:
        julian_date = astropy.time.Time(datetime.datetime(year=2021, month=3, day=10)).jd1

        result = self.converter.convert_julian_date_to_gps_week(julian_date=julian_date)

        self.assertEqual(first=2148, second=result, msg='Conversion failed. Wrong gps week calculated.')

    def test_given_correct_parameter_convert_gps_week_to_julian_date(self) -> None:
        gps_week = 2148
        day_of_week = 3
        result: float = self.converter.convert_gps_week_to_julian_date(gps_week=gps_week, day_of_week=day_of_week)

        self.assertEqual(first=2459284.0, second=result, msg='Conversion failed. Julian date is different from expected.')

    def test_given_incorrect_parameter_value_for_day_of_week_raise_exception_for_conversion_gps_week_to_julian_date(self):
        gps_week = 2148
        day_of_week = -1
        with self.assertRaises(ValueError):
            self.converter.convert_gps_week_to_julian_date(gps_week=gps_week, day_of_week=day_of_week)

    def test_given_incorrect_parameter_value_for_gps_week_raise_exception_for_conversion_gps_week_to_julian_date(self):
        gps_week = 0
        day_of_week = -1
        with self.assertRaises(ValueError):
            self.converter.convert_gps_week_to_julian_date(gps_week=gps_week, day_of_week=day_of_week)

