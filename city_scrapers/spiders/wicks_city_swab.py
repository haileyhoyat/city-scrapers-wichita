from city_scrapers.mixins.wichita_city import WichitaCityMixin


class WicksCitySWABSpider(WichitaCityMixin):
    name = "wicks_city_swab"
    agency = "Wichita City - Storm Water Advisory Board"
    cid = "57"
