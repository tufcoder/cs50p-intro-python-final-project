import pytest
from project import (
    write_champions_file,
    exists,
    read_file,
    request_champions,
    check_picks,
    check_bans,
    check_valid_name,
    ordinal,
    get_round,
    side,
)


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_file("test/file.json")


def test_request_champions():
    champions = request_champions()
    assert len(champions) > 0


def test_write_champions_file():
    file = write_champions_file("test/test_champions.json")
    assert file != ""


def test_read_file():
    champions = read_file("test/test_champions.json")
    assert exists("test/test_champions.json")
    assert len(champions) > 0


def test_check_bans():
    with pytest.raises(ValueError):
        check_bans("a", ["a", "b", "c"])


def test_check_picks():
    with pytest.raises(ValueError):
        check_picks("a", ["a", "b", "c"])


def test_check_valid_name():
    with pytest.raises(ValueError):
        check_valid_name("a1!#4ç=")


def test_ordinal():
    assert ordinal(1) == "1st"
    assert ordinal(2) == "2nd"
    assert ordinal(3) == "3rd"
    assert ordinal(4) == "4th"


def test_get_round():
    assert get_round(1, "bans") == "\n### Bans 1st Round ###\n"
    assert get_round(2, "bans") == "\n### Bans 2nd Round ###\n"
    assert get_round(1, "picks") == "\n### Picks 1st Round ###\n"
    assert get_round(2, "picks") == "\n### Picks 2nd Round ###\n"


def test_side():
    assert side("blue", "pick") == "🔵 Blue side 🔵"
    assert side("blue", "ban") == "🟦 Blue side 🟦"
    assert side("red", "pick") == "🔴 Red side 🔴"
    assert side("red", "ban") == "🟥 Red side 🟥"
