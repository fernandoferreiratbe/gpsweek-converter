# _*_ encoding: utf-8 _*_


class Converter:

    # noinspection PyMethodMayBeStatic
    def convert_julian_date_to_gps_week(self, julian_date: float):
        gps_week = ((julian_date - 2444245) // 7)

        return int(gps_week)

    # noinspection PyMethodMayBeStatic
    def convert_gps_week_to_julian_date(self, gps_week: int, day_of_week: int):
        if day_of_week not in range(0, 7):
            raise ValueError('Day of week out of range 0-6.')

        julian_day = (7.0 * gps_week + 2444245.0 + day_of_week)

        return julian_day
