from typing import Any, Union
from .query_parser import QueryParser


class DictQuery:

    def __init__(self, data: dict, path_separator: str = '/', filterpath_separator: str = '.', currentval_name: str = '@'):
        if path_separator == filterpath_separator:
            raise Exception()
        self.path_separator = path_separator
        self.filterpath_separator = filterpath_separator
        self.tmp_filterpath_separator = None
        self.currentval_name = currentval_name
        self.type_to_function = {
            'path': self.__get_by_path,
            'filter': self.__apply_filter
        }
        self.signfilter_to_function = {
            '<': self.__lt,
            '>': self.__gt,
            '=': self.__eq,
            '<=': self.__le,
            '>=': self.__ge
        }
        self.data = data

    def get(self, query: str, data: dict = None, path_separator: str = None, filterpath_separator: str = None, currentval_name: str = None) -> Any:
        self.tmp_filterpath_separator = filterpath_separator
        path_separator = path_separator if path_separator else self.path_separator
        currentval_name = currentval_name if currentval_name else self.currentval_name
        query_parser = QueryParser(path_separator=path_separator,
                                   currentval_name=currentval_name)
        current_data = data if data else self.data
        for query_element in query_parser.parse(query):
            function = self.type_to_function[query_element['type']]
            current_data = function(query_element['content'], current_data, currentval_name)
        return current_data

    def __get_by_filterpath(self, query: str, data: dict = None, currentval_name: str = None) -> Any:
        filterpath_separator = self.tmp_filterpath_separator if self.tmp_filterpath_separator else self.filterpath_separator
        currentval_name = currentval_name if currentval_name else self.currentval_name
        query_parser = QueryParser(path_separator=filterpath_separator,
                                   currentval_name=currentval_name)
        current_data = data if data else self.data
        for query_element in query_parser.parse(query):
            function = self.type_to_function[query_element['type']]
            current_data = function(query_element['content'], current_data, currentval_name)
        return current_data

    def __get_by_path(self, path: str, data: Union[dict, list], currentval_name: str) -> Any:
        if path == currentval_name:
            return data
        if type(data) is dict:
            return data[path]
        elif type(data) is list:
            return data[int(path)]

    def __apply_filter(self, filter: dict, data: Union[dict, list], currentval_name: str):
        ans = {} if type(data) is dict else []
        for subdata in data:
            value = self.__get_by_filterpath(filter['filter_path'],
                                             data=subdata if type(data) is list else data[subdata],
                                             currentval_name=currentval_name)
            function = self.signfilter_to_function[filter['filter_sign']]
            if function(value, filter['filter_value']):
                if type(ans) is dict:
                    ans[subdata] = data[subdata]
                else:
                    ans.append(subdata)
        return ans

    def __lt(self, data: Any, comparison_value: Any):
        return data < comparison_value

    def __gt(self, data: Any, comparison_value: Any):
        return data > comparison_value

    def __eq(self, data: Any, comparison_value: Any):
        return data == comparison_value

    def __le(self, data: Any, comparison_value: Any):
        return data <= comparison_value

    def __ge(self, data: Any, comparison_value: Any):
        return data >= comparison_value
