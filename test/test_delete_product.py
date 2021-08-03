from source.products_menu.delete_product import delete_product
from unittest.mock import patch, Mock

@patch('builtins.input')
def test_delete_product(mock_input):
    mock_list = [{'name': 'test'}]
    mock_input.return_value = '0'
    delete_product(mock_list)
    assert mock_list == []

@patch('builtins.input')
@patch('builtins.print')
def test_delete_product_print(mock_print, mock_input):
    mock_list = [{'name': 'test'}]
    mock_input.return_value = '0'
    delete_product(mock_list)
    mock_print.assert_called_with("product test was deleted.")


@patch("builtins.input")
def test_delete_product_C(mock_input):
    mock_input.return_value = 'C'
    mock_list = [{'name': 'test'}]
    expected = delete_product(mock_list)
    assert expected == None


@patch('builtins.input', side_effect = ['fail', '0'])
@patch('builtins.print')
def test_delete_product_error(mock_print, mock_input):
    mock_list = [{'name': 'test'}]
    mock_input.return_value
    delete_product(mock_list)
    #expecting 4 prints as function runs twice,
    #fails once and succeeds the second time
    assert mock_print.call_count == 4

