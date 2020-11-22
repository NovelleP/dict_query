from dict_query import DictQuery


if __name__ == '__main__':
    d = {
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
    dict_query = DictQuery(d)
    print(dict_query.get('a/a1[@>1]'))
    print(dict_query.get('a/a1'))
    print(dict_query.get('b'))
    print(dict_query.get('@/a/a2'))
    print(dict_query.get('d[@.flag=Si]'))
    print(dict_query.get('d[@.flag>=Si]/d4'))
    print(dict_query.get('d[this#flag>=Si]$d4', path_separator='$', filterpath_separator='#', currentval_name='this'))

    data = {
        'a': {
            'a1': {
                'flag': 'no',
                'a12': '11'
            },
            'a2': {
                'flag': 'Yes',
                'a12': '12'
            }
        }
    }
    dict_query = DictQuery(data)
    print(dict_query.get('a[@.flag=Yes]'))