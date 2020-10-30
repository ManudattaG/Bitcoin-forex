import datetime
import pytest
from decimal import Decimal
from forex_python.bitcoin import (get_latest_price, get_previous_price_list, BtcConverter)

class TestBitCoinForceDecimal:
    """
    Test Perfect fit - get latest price with force_decimal flag
    """
    def test_bitcoin_with_force_decimal(self):
        btc_obj = BtcConverter(force_decimal=True)
        price = btc_obj.get_latest_price('USD')
        assert type(price) == Decimal

    def test_bitcoin_without_force_decimal(self):
        btc_obj = BtcConverter()
        price = btc_obj.get_latest_price('USD')
        assert type(price) == float

class TestBitcoinLatestRate:
    """
    Test Perfect fit - get latest price using currency code
    """
    @pytest.mark.parametrize(
        "currency, expected, exception",
        [
            ("USD", float, None),
            ("BTC", int, None),
            ("EUR", float, None)
        ]
    )
    def test_latest_price_valid_codes(self, currency, expected, exception):
        if exception:
            with pytest.raises(exception):
                result = get_latest_price(currency=currency)
        else:
            result = get_latest_price(currency=currency)
            assert type(result) == expected

    """
    Test edge(failure) cases - get latest price using currency code
    """
    @pytest.mark.parametrize(
        "currency, expected, exception",
        [
            ("XYZ", None, None),
            ("", None, None),
            (250, None, None),
            ("100", None, None),
            (["USD"], None, None)
        ]
    )
    def test_latest_price_invalid_codes(self, currency, expected, exception):
        if exception:
            with pytest.raises(exception):
                result = get_latest_price(currency=currency)
        else:
            result = get_latest_price(currency=currency)
            assert result is None

class TestBitcoinHistoricalRates:
    """
    Test Perfect fit - get historical price using currency code
    """
    @pytest.mark.parametrize(
        "startDate, endDate, currency, expected, exception",
        [
            (datetime.datetime.today() - datetime.timedelta(days=10), datetime.datetime.today(), "USD", dict, None),
            (datetime.datetime.today() - datetime.timedelta(days=5), datetime.datetime.today(), "BTC", dict, None),
            (datetime.datetime.today() - datetime.timedelta(days=6), datetime.datetime.today(), "EUR", dict, None),
            (datetime.datetime.today(), datetime.datetime.today(), "USD", dict, None),
            (datetime.datetime.today() - datetime.timedelta(days=int("10")), datetime.datetime.today(), "INR", dict, None)
        ]
    )
    def test_historical_price_valid_codes(self, startDate, endDate, currency, expected, exception):
        if exception:
            with pytest.raises(exception):
                result = get_previous_price_list(currency=currency, start_date=startDate, end_date=endDate)
        else:
            result = get_previous_price_list(currency=currency, start_date=startDate, end_date=endDate)
            assert type(result) == expected

    """
    Test edge(failure) cases - get historical price using currency code
    """
    @pytest.mark.parametrize(
        "startDate, endDate, currency, expected, exception",
        [
            ("2020-10-15", "2020-10-25", "USD", "", AttributeError),
            ("2020-10-20", "2020-10-25", "XYZ", "", AttributeError),
            ("2020-10-01", "2020-10-05", "INR", "", AttributeError),
            (datetime.datetime.today() - datetime.timedelta(days=10), datetime.datetime.today(), "XYZ", dict, None),
            (datetime.datetime.today() - datetime.timedelta(days=-2), datetime.datetime.today(), "USD", dict, None)
        ]
    )
    def test_historical_price_invalid_codes(self, startDate, endDate, currency, expected, exception):
        if exception:
            with pytest.raises(exception):
                result = get_previous_price_list(currency=currency, start_date=startDate, end_date=endDate)
        else:
            result = get_previous_price_list(currency=currency, start_date=startDate, end_date=endDate)
            assert type(result) == expected