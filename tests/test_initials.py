def test_lists():
    assert [1, 2, 3] == [1, 2, 3]


def test_lists_ok():
    assert [3, 3, 3] != [1, 2, 3]

def test_lists_neOK():
    assert [3, 3, 3] != [1, 2, 3]