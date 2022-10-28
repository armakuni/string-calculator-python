import re
from typing import List

NEGATIVE_NUMBER_MESSAGE = "negatives not allowed:"

def add(numbers: str) -> int:  
    if not numbers:
        return 0
    
    delimeter = get_delimeter(numbers)
    numbers = remove_delimeter(numbers)
    numbers_ = get_number_list(numbers, delimeter)
    result = add_numbers(numbers_)
    return result

def get_delimeter(numbers: str) -> str:
    delimeter = None
    if numbers.startswith('//'):
        delimeter = re.split(r'//|\n',numbers)[1]
        if not delimeter:
            delimeter = ';'

    if not delimeter:
        delimeter = "[,\n]"

    return delimeter

def remove_delimeter(numbers: str) -> str:
    if numbers.startswith('//'):
        return re.split(r'//|\n',numbers)[2]
    return numbers

def get_number_list(numbers: str, delimeter: str) -> list:
    str_numbers = re.split(delimeter,numbers)
    number_list = []
    negative_numbers = []

    for s in str_numbers:
        if not s:
            raise NotImplementedError("Empty number not supported")
        n = int(s)
        if n < 0:
            negative_numbers.append(n)
            continue
        number_list.append(n)

    if len(negative_numbers) > 0:
        raise NotImplementedError(NEGATIVE_NUMBER_MESSAGE + ','.join(str(n) for n in negative_numbers))

    return number_list

def add_numbers(numbers: List[int]) -> int:
    return sum(numbers)