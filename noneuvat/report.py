import calendar
import datetime

from tabler import Tabler as Table
from stclocal import PyLinnworks


class NonEUVATReport:

    eu_countries = [
        'Netherlands', 'Germany', 'Malta', 'Croatia', 'Italy',
        'Bulgaria', 'Romania', 'Estonia', 'Portugal', 'Czech Republic',
        'Cyprus', 'Poland', 'Lithuania', 'Latvia', 'Slovakia', 'Ireland',
        'United Kingdom', 'Slovenia', 'Luxembourg', 'France', 'Sweden',
        'Austria', 'Greece', 'Finland', 'Belgium', 'Denmark', 'Spain',
        'Hungary']

    def __init__(self, year, quarter):
        self.year = year
        self.quarter = quarter
        self.get_dates()
        self.get_order_table()
        self.report = self.generate_report()

    def get_dates(self):
        quarters = {1: [1, 3], 2: [4, 6], 3: [7, 9], 4: [10, 12]}
        year = self.year
        start_month, end_month = quarters[self.quarter]
        self.start_date = datetime.datetime(
            year=year, month=start_month, day=1)
        self.end_date = datetime.datetime(
            year=year, month=end_month, day=calendar.monthrange(
                year, end_month)[1])

    def get_order_table(self):
        export = PyLinnworks.Export()
        self.order_table = export.get_orders_between_dates(
            self.start_date, self.end_date)

    def generate_report(self):
        non_EU_vat_table = Table()
        non_EU_vat_table.header = ['Country', 'Sales']
        country_total_lookup = {}
        for row in self.order_table:
            if row['status'] == 'PAID' and row['Source'] != 'EPOS':
                if row['Country'] not in country_total_lookup:
                    country_total_lookup[row['Country']] = 0.0
                country_total_lookup[row['Country']] += float(row['Total'])
        for key in country_total_lookup:
            if key not in self.eu_countries:
                non_EU_vat_table.append(
                    [key, round(country_total_lookup[key], 2)])
        non_EU_vat_table.sort('Country')
        return non_EU_vat_table

    def get_save_name(self, extension=None):
        return 'Non EU Vat - {} Q{}.{}'.format(
            self.year, self.quarter, extension)
