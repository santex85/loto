from loto import Card
from pytest import fixture


@fixture
def instance_card() -> list:
    card = Card()
    card = card.get_card()
    return card


class TestCard:
    win_card = [
        ['-', '', '-', '', '-', '-', '', '-', '', ''],
        ['-', '-', '-', '-', '-', '', '', '', '', ''],
        ['', '', '-', '', '-', '', '-', '-', '-', '']
    ]

    def test_check_card(self, instance_card: list):
        result = Card.check_card(instance_card)
        assert result is None

    def test_check_win_card(self):
        result = Card.check_card(self.win_card)
        assert result is True
