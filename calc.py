import re

def add(numbers: str) -> int:
    result = 0
    if not numbers:
        return result
    
    delimeter = None
    if numbers.startswith('//'):
        delimeter = re.split(r'//|\n',numbers)[1]
        numbers = re.split(r'//|\n',numbers)[2]
        if not delimeter:
            delimeter = ';'

    if not delimeter:
        delimeter = "[,\n]"

    numbers_ = re.split(delimeter,numbers)
    print(numbers_)
    for n in numbers_:
        if not n:
            raise NotImplementedError("Empty number not supported")
        result += int(n)

    return result