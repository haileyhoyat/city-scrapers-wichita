from city_scrapers.mixins.wichita_city_mixin import WichitaCityMixin


class WicksCityWCRBSpider(WichitaCityMixin):
    name = "wicks_city_wcrb"
    agency = "Wichita Citizens Review Board"
    cid = "61"
