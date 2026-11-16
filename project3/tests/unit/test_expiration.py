import pytest
from datetime import date, timedelta
from app import create_app
from app.models import Fruit, FruitMetrics, db


@pytest.fixture
def test_app():
    # Fresh app and empty in-memory database for every test
    app = create_app()
    ctx = app.app_context()
    ctx.push()
    db.create_all()

    yield app

    db.session.remove()
    ctx.pop()


def test_createFruit_withExpirationDate_storesDate():
    """
    A Fruit can be created with an expiration date and keeps it.
    """
    expires = date(2030, 1, 1)
    fruit = Fruit(name="Apple", quantity=10, expiration_date=expires)
    assert fruit.expiration_date == expires


def test_isExpired_withPastDate_returnsTrue():
    """
    A fruit whose expiration date is before today is expired.
    """
    fruit = Fruit(name="Apple", quantity=10, expiration_date=date.today() - timedelta(days=1))
    assert fruit.is_expired() is True


def test_isExpired_withFutureDate_returnsFalse():
    """
    A fruit whose expiration date is after today is not expired.
    """
    fruit = Fruit(name="Apple", quantity=10, expiration_date=date.today() + timedelta(days=1))
    assert fruit.is_expired() is False


def test_isExpired_withTodayDate_returnsFalse():
    """
    A fruit that expires today is not yet expired (boundary case).
    """
    fruit = Fruit(name="Apple", quantity=10, expiration_date=date.today())
    assert fruit.is_expired() is False


def test_isExpired_withNoExpirationDate_returnsFalse():
    """
    A fruit with no expiration date is never considered expired.
    """
    fruit = Fruit(name="Apple", quantity=10)
    assert fruit.is_expired() is False


def test_isExpired_withCustomToday_usesGivenDate():
    """
    is_expired accepts a custom 'today' so it can be tested with fixed dates.
    """
    fruit = Fruit(name="Apple", quantity=10, expiration_date=date(2025, 6, 1))
    assert fruit.is_expired(today=date(2025, 6, 2)) is True
    assert fruit.is_expired(today=date(2025, 5, 31)) is False


def test_serialize_withExpirationDate_returnsIsoString():
    """
    serialize() turns the date into a YYYY-MM-DD string so it can become JSON.
    """
    fruit = Fruit(name="Apple", quantity=10, expiration_date=date(2030, 1, 15))
    assert fruit.serialize()['expiration_date'] == '2030-01-15'


def test_getExpired_withMixedFruits_returnsOnlyExpiredFruits(test_app):
    """
    get_expired returns only fruits with a past date, ignoring future dates
    and fruits that have no date at all.
    """
    today = date.today()
    db.session.add_all([
        Fruit(name="Old Apple", quantity=1, expiration_date=today - timedelta(days=5)),
        Fruit(name="Fresh Banana", quantity=2, expiration_date=today + timedelta(days=5)),
        Fruit(name="Plain Pear", quantity=3),
    ])
    db.session.commit()

    results = Fruit.get_expired()
    assert [fruit.name for fruit in results] == ["Old Apple"]


def test_getExpired_withCustomToday_usesGivenDate(test_app):
    """
    get_expired accepts a custom 'today' to compare against.
    """
    db.session.add(Fruit(name="Apple", quantity=1, expiration_date=date(2025, 6, 1)))
    db.session.commit()

    assert len(Fruit.get_expired(today=date(2025, 7, 1))) == 1
    assert Fruit.get_expired(today=date(2025, 5, 1)) == []


def test_totalQuantity_withFruitsList_returnsSumOfQuantities():
    """
    total_quantity adds up the quantity of every fruit.
    """
    fruits = [Fruit(name="Apple", quantity=10), Fruit(name="Banana", quantity=5)]
    assert FruitMetrics.total_quantity(fruits) == 15


def test_totalQuantity_withEmptyList_returnsZero():
    """
    The total quantity of an empty inventory is 0.
    """
    assert FruitMetrics.total_quantity([]) == 0
