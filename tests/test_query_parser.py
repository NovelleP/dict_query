from dict_query import QueryParser


def test_parse():
    query_parser = QueryParser(path_separator='/',
                               currentval_name='@')
    parsed_query = query_parser.parse('a/a1[@.filter>=2]')
    assert parsed_query == [
        {'type': 'path',
          'content': 'a'},
        {'type': 'path',
         'content': 'a1'},
        {'type': 'filter',
         'content': {'filter_path': '@.filter',
                     'filter_sign': '>=',
                     'filter_value': '2'}
        }
    ]
