from city_scrapers.mixins.wichita_city_mixin import WichitaCityMixin


class WicksCityEDCMBSpider(WichitaCityMixin):
    name = "wicks_city_edcmb"
    agency = "Wichita City - Employees' Deferred Compensation Management Board"
    cid = "63"
