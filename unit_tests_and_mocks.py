import mock_supporting_module
from unittest.mock import patch


@patch('mock_supporting_module.ClassName2')
@patch('mock_supporting_module.ClassName1')
def test_mocking(mockclass1, mockclass2):
    m1 = mock_supporting_module.ClassName1()
    m2 = mock_supporting_module.ClassName2()
    assert mockclass1 is mock_supporting_module.ClassName1
    assert mockclass2 is mock_supporting_module.ClassName2
    assert mockclass1.called
    assert mockclass2.called
    print(m1.__dict__)


@patch('mock_supporting_module.ClassName1')
@patch('mock_supporting_module.ClassName2')
def test_mocking_reversed1(mockclass1, mockclass2):
    m1 = mock_supporting_module.ClassName1()
    m2 = mock_supporting_module.ClassName2()
    assert mockclass1 is mock_supporting_module.ClassName2
    assert mockclass2 is mock_supporting_module.ClassName1
    assert mockclass1.called
    assert mockclass2.called
    print(m1.__dict__)


@patch('mock_supporting_module.ClassName2')
@patch('mock_supporting_module.ClassName1')
def test_mocking_reversed2(mockclass2, mockclass1):
    m1 = mock_supporting_module.ClassName1()
    m2 = mock_supporting_module.ClassName2()
    assert mockclass2 is mock_supporting_module.ClassName1
    assert mockclass1 is mock_supporting_module.ClassName2
    assert mockclass1.called
    assert mockclass2.called
    print(m1.__dict__)


test_mocking()
test_mocking_reversed1()
test_mocking_reversed2()


