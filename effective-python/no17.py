def normalize(numbers):
    numbers = list(numbers)  # copy the iterator
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


def normalize_func(get_iter):
    """ this is the descritpion
    """
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percent = 100 * value / total
        result.append(percent)
    return result


class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


path = 'C:\\Users\\qxu8502\\workspace\\myspace\\python\\python-xuexi\\effective-python\\my_numbers.txt'
visits = read_visits(path)
#visits = [15,35,80]
# print(list(visits))
# print(list(visits))
percentages = normalize(visits)
print('normalize', percentages)

percentages2 = normalize_func(lambda: read_visits(path))
print('normalize 2', percentages2)

visits2 = ReadVisits(path)
percentages3 = normalize(visits2)
print('normalize 3', percentages3)
