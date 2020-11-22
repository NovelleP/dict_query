from dict_query import FilterParser


def test_contains_filter_ok():
    filter_parser = FilterParser(currentval_name='@')
    filter = filter_parser.contains_filter('path1[@.item1>=15]')
    assert filter == '[@.item1>=15]'


def test_contains_filter_ko():
    filter_parser = FilterParser(currentval_name='@')
    filter = filter_parser.contains_filter('path1')
    assert filter is None

def test_parse():
    filter_parser = FilterParser(currentval_name='@')
    parsed_filter = filter_parser.parse('[@.item>=1]')
    assert parsed_filter == {
        'filter_path': '@.item',
        'filter_sign': '>=',
        'filter_value': '1'
    }
