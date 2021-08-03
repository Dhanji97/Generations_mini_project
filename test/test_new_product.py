from source.products_menu.new_product import create_new_product
from unittest.mock import patch, Mock

@patch("builtins.input", side_effect=["new", '1.00'])
def test_new_product(mock_input):
    mock_input.return_value
    mock_list = Mock()
    mock_list.return_value = []
    create_new_product(mock_list)
    mock_list.append.assert_called_with({'name': 'new', 'price': '£1.00'})

@patch("builtins.input", side_effect=["new", '1.00'])
@patch("builtins.print")
def test_new_product_print(mock_print, mock_input):
    mock_input.return_value
    mock_list = Mock()
    mock_list.return_value = []
    create_new_product(mock_list)
    mock_print.assert_called_with("{'name': 'new', 'price': '£1.00'} added to list of couriers")

@patch("builtins.input")
def test_new_product_first_C(mock_input):
    mock_input.return_value = 'C'
    mock_list = Mock()
    mock_list.return_value = []
    expected = create_new_product(mock_list)
    assert expected == None

@patch("builtins.input", side_effect=["new", 'C'])
def test_new_product_second_C(mock_input):
    mock_input.return_value
    mock_list = Mock()
    mock_list.return_value = []
    expected = create_new_product(mock_list)
    assert expected == None
