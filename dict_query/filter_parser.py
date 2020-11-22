import re
from typing import Optional, Dict


class FilterParser:

    def __init__(self, currentval_name: str = '@'):
        self.currentval_name = currentval_name
        self.valid_signs = ('<=', '>=', '<', '>', '=')
        self.validsigns_exp = '|'.join(self.valid_signs)
        self.sign_validator = re.compile(self.validsigns_exp)
        self.filter_validator = re.compile(f'(?<=\[){re.escape(currentval_name)}.*?(?:{self.validsigns_exp}).+(?=\])')

    def parse(self, filter: str) -> Dict[str, str]:
        if not (filter_match := self.filter_validator.search(filter)):
            raise Exception()  # TODO: define exception for this case

        filter_query = filter_match.group()
        filter_sign = max(self.sign_validator.findall(filter_query), key=len)
        filter_path, filter_value = filter_query.split(filter_sign)
        return {
            'filter_path': filter_path,
            'filter_sign': filter_sign,
            'filter_value': filter_value  # TODO: casting filter value to specific type
        }

    def contains_filter(self, subquery: str) -> Optional[str]:
        if (filter_match := self.filter_validator.search(subquery)):
            return f'[{filter_match.group()}]'
        else:
            return None

