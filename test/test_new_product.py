import builtins
from source.products_menu.new_product import create_new_product
from unittest.mock import patch, Mock

@patch("builtins.input", side_effect=["new", 1.00])
def test_new_product(mock_input):
    mock_input.return_value
    mock_list = Mock()
    mock_list.return_value = []
    create_new_product(mock_list)
    mock_list.append.assert_called_with({'name': 'new', 'price': 1.00})

