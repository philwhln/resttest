from decimal import Decimal

import pytest
import responses

from resttest.transactions import (TRANSACTIONS_BASE_URL,
                                   all_daily_balances,
                                   combine_daily_balances, get_page,
                                   grand_total, sum_daily_balances)


TRANSACTIONS_FIXTURE_DIR = 'tests/fixtures/transactions'


@pytest.fixture
def mock_transaction_pages():
    for page_number in [1, 2, 3, 4]:
        body = open('{}/{}.json'.format(TRANSACTIONS_FIXTURE_DIR,
                                        page_number), 'r').read(),
        responses.add(responses.GET,
                      '{}/{}.json'.format(TRANSACTIONS_BASE_URL, page_number),
                      body=body, status=200, content_type='application/json')

    responses.add(responses.GET,
                  '{}/{}.json'.format(TRANSACTIONS_BASE_URL, 5),
                  body=body, status=404)


def test_get_page(mock_transaction_pages):
    for page_number in [1, 2, 3, 4]:
        page = get_page(page_number)
        assert page
        assert 'transactions' in page

    assert not get_page(5)


def test_sum_daily_balances(mock_transaction_pages):
    page = get_page(4)
    expect = {
        '2013-12-13': Decimal('-6156.83'),
        '2013-12-20': Decimal('-1874.75'),
        '2013-12-12': Decimal('-227.35')
    }
    assert sum_daily_balances(page['transactions']) == expect


def test_combine_daily_balances():
    balances1 = {
        '2013-12-01': Decimal('1.11'),
        '2013-12-02': Decimal('-2.22'),
        '2013-12-03': Decimal('-3.33')
    }
    balances2 = {
        '2013-12-02': Decimal('-20.00'),
        '2013-12-03': Decimal('-30.00'),
        '2013-12-04': Decimal('-40.00')
    }
    assert combine_daily_balances(balances1, balances2) == {
        '2013-12-01': Decimal('1.11'),
        '2013-12-02': Decimal('-22.22'),
        '2013-12-03': Decimal('-33.33'),
        '2013-12-04': Decimal('-40.00')
    }


total_daily_balances = {
    '2013-12-12': Decimal('-227.35'),
    '2013-12-13': Decimal('-1229.58'),
    '2013-12-15': Decimal('-5.39'),
    '2013-12-16': Decimal('-4575.53'),
    '2013-12-17': Decimal('10686.28'),
    '2013-12-18': Decimal('-1841.29'),
    '2013-12-19': Decimal('19753.31'),
    '2013-12-20': Decimal('-4054.60'),
    '2013-12-21': Decimal('-17.98'),
    '2013-12-22': Decimal('-110.71')
}


def test_all_daily_balances(mock_transaction_pages):
    assert all_daily_balances() == total_daily_balances


def test_grand_total(mock_transaction_pages):
    assert grand_total(total_daily_balances) == Decimal('18377.16')
