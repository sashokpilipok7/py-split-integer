from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    res = split_integer(11, 5)

    assert sum(res) == 11
    assert res == [2, 2, 2, 2, 3]


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    res = split_integer(20, 5)
    for number in res:
        assert 20 // 5 == number, "parrts not equal"
    assert res == [4, 4, 4, 4, 4]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    res = split_integer(10, 1)

    assert res[0] == 10
    assert res == [10]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    res = split_integer(20, 3)

    assert res == sorted(res)
    assert res == [6, 7, 7]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    res = split_integer(10, 15)

    assert res.count(0) == 5
