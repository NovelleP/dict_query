# dict_query
Queries in Python dicts

#### Paths
```
data = {
  'a': {
    'a1': 1
  }
}
dict_query = DictQuery(data)
dict_query.get('a/a1')
>>> 1  # the same results that data['a']['a1']
```

#### Filters
```
data = {
  'a': {
    'a1': ['1', '2', '3', '4']
  }
}
dict_query = DictQuery(data)
dict_query.get('a/a1[@>2]')
>>> ['3', '4']
```

```
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
dict_query.get('a[@.flag=Yes]')
>>> {'a2': {'flag': 'Yes', 'a12': '12'}}
```

>'@' is a special char: then name for the current value
>* This char can be changed in the call to DictQuery constructor
>```
>DictQuery(data, currentval_name='@')
>```
>* It also can be changed in the call to 'get' method for a specific query
>```
>DictQuery(data).get(query, currentval_name='this')
>```

>By default '/' is the path separator out of filters and '.' is the filter path separator
>* This path separators can be changed in the call to DictQuery constructor (both path separators cannot be the same)
>```
>DictQuery(data, path_separator='#', filterpath_separator='?')
>```
>
>* The separator also can be changed in the call to 'get' method for a specific query
>```
>DictQuery(data).get(query, path_separator='#', filterpath_separator='?')
>```
