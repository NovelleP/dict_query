import pytest
from dict_query import DictQuery


def test_get_ok():
    data = {
        'a': {
            'a1': ['1', '2'],
            'a2': {'a21': '1'}
        },
        'b': 2,
        'c': {
            'c1': 3,
            'c2': 4
        },
        'd': {
            'd1': {
                'flag': 'Si',
                'flag2': '1',
                'd12': 'as'
            },
            'd2': {
                'flag': 'a',
                'flag2': '2',
                'd22': 'as'
            },
            'd3': {
                'flag': 'No',
                'flag2': '3',
                'd32': 'as'
            },
            'd4': {
                'flag': 'Si',
                'flag2': '4',
                'd42': 'as'
            }

        }
    }
    dict_query = DictQuery(data,
                           path_separator='/',
                           filterpath_separator='.',
                           currentval_name='@')
    query_result = dict_query.get('d[@.flag>=Si]/d4')
    assert query_result == {
        'flag': 'Si',
        'flag2': '4',
        'd42': 'as'
    }

def test_get_ok():
    data = {
        'a': {
            'a1': ['1', '2'],
            'a2': {'a21': '1'}
        },
        'b': 2,
        'c': {
            'c1': 3,
            'c2': 4
        },
        'd': {
            'd1': {
                'flag': 'Si',
                'flag2': '1',
                'd12': 'as'
            },
            'd2': {
                'flag': 'a',
                'flag2': '2',
                'd22': 'as'
            },
            'd3': {
                'flag': 'No',
                'flag2': '3',
                'd32': 'as'
            },
            'd4': {
                'flag': 'Si',
                'flag2': '4',
                'd42': 'as'
            }

        }
    }
    dict_query = DictQuery(data,
                           path_separator='/',
                           filterpath_separator='.',
                           currentval_name='@')
    with pytest.raises(KeyError):
        dict_query.get('d[@.flag>=Si]/d5')
