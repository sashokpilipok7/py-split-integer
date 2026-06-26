from app.split_integer import split_integer

def test_base_logic_for_each_split() -> None:
    value = 20
    parts = 3
    result = split_integer(value, parts)

    assert sum(result) == value
    assert len(result) == parts
    assert max(result) - min(result) <= 1
    assert sorted(result) == result


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 11
    parts = 5
    res = split_integer(value, parts)


    assert sum(res) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 20
    parts = 5
    res = split_integer(value, parts)

    for n in res:
        assert value // parts == n, "parrts not equal"




def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    res = split_integer(10,1)

    assert res[0] == 10


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    res = split_integer(20,3)
    expected = sorted(res)

    assert res == expected
    assert res == [6,7,7]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 10
    parts = 15
    res = split_integer(value,parts)
    difference = parts - value

    assert res.count(0) == difference
    # start_idx = len(res) - difference
    # assert res[start_idx:] == [0]*difference

