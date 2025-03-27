"""Testing edge and use cases of the functions in the dictionary file."""
___author___ = "730547147"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len

def test_invert_use1()-> None:
    "Testing a use case for in the invert function."
    test_dict = {"cat": "gibby", "kitty":"morty", "feline":"cosmo"}
    expectation = {"gibby":"cat", "morty":"kitty","cosmo":"feline"}
    assert invert(test_dict) == expectation

def test_invert_use2() -> None:
    "Testing second use case for the invert fucntion"
    test_dict2 = {"red":"apple", "green":"mango","purple":"grape"}
    expectation2 = {"apple":"red", "mango":"green", "purple":"grape"}
    assert invert (test_dict2) == expectation2

def test_invert_edge() -> None:
    "Testing an edge case of the invert function"
    test_dict3 = {}
    edge_case_expectation = {}
    assert invert(test_dict3) == edge_case_expectation


def test_count_1() -> None:
    "Testing the first use case of the count function."
    test_count = ["peanut", "almond", "walnut", "peanut"]
    expected_result = {"peanut": 2, "almond": 1, "walnut": 1}
    assert count(test_count) == expected_result

def test_count_2() -> None:
    "testing second use case of the count function."
    test_count2 = ["pizza", "pasta", "pasta", "pasta", "pizza"]
    expected_result2 = {"pizza": 2, "pasta": 3}
    assert count(test_count2) == expected_result2

def test_count_edge() -> None:
    "testing an edge case of the count function."
    test_edge = []
    expected_result_edge = {}
    assert count(test_edge) == expected_result_edge



def test_fav_1() -> None:
    """Testing the favorite color function with a use case."""
    test_color1 = {"Zoe":"blue", "Jim":"red", "Tim":"gray", "Tom":"gray"}
    expected_fav = "gray"
    assert favorite_color(test_color1) == expected_fav

def test_fav_2()-> None:
    """testing the fav color function with a use case with two fav colors."""
    test_color2 = {"Jon":"red", "Mai":"red", "Lia":"blue", "Layla":"blue"}
    expected_fav2 = "red"
    assert favorite_color(test_color2) == expected_fav2

def test_fav_edge() -> None:
    """Testing an edge case of the fav color function."""
    edge_color = {}
    expected_fav3 = ""
    assert favorite_color(edge_color) == expected_fav3



def test_bin1() -> None:
    "Testing an expected input of a list of strings to see output."
    bin1_test = ["cat","rabbit","dog","horse"]
    expected_diction1 = {3:{"cat","dog"}, 6:{"rabbit"}, 5:{"horse"}}
    assert bin_len(bin1_test) == expected_diction1

def test_bin2() -> None:
    """Testing a use case in which all strings are same length."""
    bin2_test = ["rat","bat","ant","bee","fox"]
    expected_diction2 = {3:{"rat","bat","ant","bee","fox"}}
    assert bin_len(bin2_test) == expected_diction2

def test_bin_edge() -> None:
    """testing edge case in which no values are inputted"""
    bin_edge = []
    expected_diction3 = {}
    assert bin_len(bin_edge) == expected_diction3