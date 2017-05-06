from decimal import Decimal
from requests import get

TRANSACTIONS_BASE_URL = 'http://resttest.bench.co/transactions'
ZERO = Decimal('0.00')


def get_page(page_number):
    url = '{}/{}.json'.format(TRANSACTIONS_BASE_URL, page_number)
    response = get(url)
    code = response.status_code

    if code == 404:
        return None

    if code == 200:
        return response.json()

    raise Exception('Unexpected response code {} from {}'.format(code, url))


def sum_daily_balances(transactions):
    daily_balances = {}

    for txn in transactions:

        date = txn['Date']
        amount = txn['Amount']

        if date not in daily_balances:
            daily_balances[date] = ZERO

        daily_balances[date] += Decimal(amount)

    return daily_balances


def combine_daily_balances(balances1, balances2):
    daily_balances = {}
    for date in set(balances1.keys()).union(set(balances2.keys())):
        daily_balances[date] = (balances1.get(date, ZERO) +
                                balances2.get(date, ZERO))
    return daily_balances


def all_daily_balances():
    page_number = 1
    daily_balances = {}

    # Since no guarantees on page size, cannot assume number of pages
    while True:
        page = get_page(page_number)
        if not page:
            return daily_balances

        page_daily_balances = sum_daily_balances(page['transactions'])
        daily_balances = combine_daily_balances(daily_balances,
                                                page_daily_balances)
        page_number += 1


def grand_total(daily_balances):
    return sum(daily_balances.values())
