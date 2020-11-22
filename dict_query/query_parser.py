import re
from typing import List
from .filter_parser import FilterParser


class QueryParser:

    def __init__(self, path_separator: str = '/', currentval_name: str = '@'):
        self.path_separator = path_separator
        self.currentval_name = currentval_name
        self.query_splitter = re.compile(re.escape(self.path_separator))
        self.filter_parser = FilterParser(currentval_name=self.currentval_name)

    def parse(self, query: str) -> List[dict]:
        subqueries = []
        for subquery in self.query_splitter.split(query):
            if (filter := self.filter_parser.contains_filter(subquery)):
                subquery_without_filter = subquery.replace(filter, '')
                subqueries.extend(({'type': 'path',
                                    'content': subquery_without_filter},
                                   {'type': 'filter',
                                    'content': self.filter_parser.parse(filter)}))
            else:
                subqueries.append({'type': 'path',
                                   'content': subquery})
        return subqueries
