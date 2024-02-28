import pytest
import mock
import builtins
import os
from project import (
    read_file,
    request_champions,
    write_champions_file,
    exists,
    check_bans,
    check_picks,
    check_valid_name,
    ordinal,
    get_round,
    side,
    get_lower_names,
    check_lower_names,
    list_options,
    check_names,
    sinput,
    first_round_bans,
    second_round_bans,
    first_round_picks,
    second_round_picks,
    mkdir,
    write_file,
    append_table_bans,
    append_table_picks,
    append_draf,
    final_table_bans,
    final_table_picks,
    final_draf,
    get_champions,
    write_draft_csv,
    tabulate,
)


champions = {
    "data": {
        "Aatrox": { "id": "Aatrox" },
        "Ahri": { "id": "Ahri" },
        "AurelionSol": { "id": "AurelionSol" },
    }
}
bans_first = ["lucian", "nami", "milio", "ashe", "jax", "poppy"]
picks_first = ["varus", "azir", "jhin", "aatrox", "orianna", "xinzhao"]
bans = ["lucian", "nami", "milio", "ashe", "jax", "poppy", "renata", "jayce", "rell", "renekton"]
picks = ["varus", "azir", "jhin", "aatrox", "orianna", "xinzhao", "gwen", "leesin", "rakan", "bard"]


def test_tabulate():
    with pytest.raises(TypeError):
        print(tabulate())


def test_write_draft_csv():
    path = "test/temp_draft"
    write_draft_csv(path, ["column1","column2","column3"], ["abc", "def"])
    assert exists(path)


def test_get_champions():
    path = "test/test_champions.json"
    get_champions(path)
    assert exists(path)


def test_final_draf():
    fpicks = [[1,2],[4,3],[5,6],[8,7],[9,10]]
    fbans = [[1,2],[3,4],[5,6],[8,7],[10,9]]
    ft = [[1,2,1,2],[4,3,3,4],[5,6,5,6]]
    assert final_draf(fpicks, fbans, ft) == [
        [1,2,1,2],
        [4,3,3,4],
        [5,6,5,6],
        [8,7,8,7],
        [9,10,10,9]
    ]


def test_final_table_picks():
    table = [[1,2],[4,3],[5,6]]
    assert final_table_picks([1,2,3,4,5,6,7,8,9,10], [1,4,5], [2,3,6], table) == [
        [1,2],[4,3],[5,6],[8,7],[9,10]
    ]


def test_final_table_bans():
    table = [[1,2],[3,4],[5,6]]
    assert final_table_bans([1,2,3,4,5,6,7,8,9,10], [1,3,5], [2,4,6], table) == [
        [1,2],[3,4],[5,6],[8,7],[10,9]
    ]


def test_append_draf():
    assert append_draf([[1,2],[4,3],[5,6]], [[1,2],[3,4],[5,6]], []) == [
        [1,2,1,2],
        [4,3,3,4],
        [5,6,5,6]
    ]


def test_append_table_picks():
    assert append_table_picks([1,2,3,4,5,6], [], [], []) == [
        [1,2],
        [4,3],
        [5,6]
    ]


def test_append_table_bans():
    assert append_table_bans([1,2,3,4,5,6], [], [], []) == [
        [1,2],
        [3,4],
        [5,6]
    ]


def test_write_file():
    filename = "test/temp_draft/test.txt"
    data = "abcd"
    write_file(filename, data)
    assert exists(filename)


def test_mkdir():
    path = "test/temp_draft/test-dir"
    mkdir(path)
    assert os.path.exists(path)


def test_second_round_picks():
    with mock.patch.object(builtins, "input", lambda _: "renata"):
        pickeds = second_round_picks(1, 1, bans, picks)
        assert pickeds == picks


def test_first_round_picks():
    with mock.patch.object(builtins, "input", lambda _: "varus"):
        pickeds = first_round_picks(1, 1, bans_first, picks_first)
        assert pickeds == picks_first


def test_second_round_bans():
    with mock.patch.object(builtins, "input", lambda _: "renata"):
        banneds = second_round_bans(1, 1, bans, picks)
        assert banneds == bans


def test_first_round_bans():
    with mock.patch.object(builtins, "input", lambda _: "lucian"):
        banneds = first_round_bans(1, 1, bans_first, picks_first)
        assert banneds == bans_first


def test_sinput():
    with mock.patch.object(builtins, "input", lambda _: "ahri"):
        path = "test/test_champions.json"
        assert sinput("1st pick: ", bans, picks, path) == "Ahri"


def test_check_names():
    path = "test/test_champions.json"
    assert check_names("ahri", bans, picks, path) == "Ahri"
    assert check_names("AHRI", bans, picks, path) == "Ahri"
    assert check_names("AhRi", bans, picks, path) == "Ahri"
    with pytest.raises(ValueError):
        check_names("ahhhhri", bans, picks, path)


def test_list_options():
    o = list_options(champions, "ah")
    assert o == ["Are you are trying to choose: Ahri ?"]


def test_check_lower_names():
    l = check_lower_names(champions, "ahri", bans, picks)
    assert l == "Ahri"


def test_get_lower_names():
    assert get_lower_names(champions) == [
        {"name": "Aatrox", "lower": "aatrox"},
        {"name": "Ahri", "lower": "ahri"},
        {"name": "AurelionSol", "lower": "aurelionsol"},
    ]


def test_read_file_not_found():
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

def test_exists():
    path = "test/test_champions.json"
    assert exists(path)
