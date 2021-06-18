#!/usr/bin/python3


class fizzbuzz:
    """
    Simple iterator which implements fizz-buzz exercise usualy seen on job interviews.
    There are two arguments:
    - start -- first element to start our iteration
    - stop -- last element which should stop our iteration
    """

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.index = start

    def __iter__(self):
        return self

    def __next__(self):
        result = ''
        if self.index <= self.end:
            idx = self.index
            if not (idx % 3):
                result += 'fizz'
            if not (idx % 5):
                result = 'buzz'
            self.index = + 1
            return result or idx
        else:
            raise StopIteration()

    def __repr__(self):
        return 'fizzbuzz({}, {})'.format(self.start, end)


if __name__ == '__main__':
    assert list(fizzbuzz(3, 5)) == ['fizz', 4, 'buzz']
    assert list(fizzbuzz(12, 15)) == ['fizz', 13, 14, 'fizzbuzz']
