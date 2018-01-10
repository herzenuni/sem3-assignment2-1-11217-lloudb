import pytest

import nod

def factory(a, b, c):
	def test():
		assert nod.nod(a, b) == c
	return test


test1 = factory(1, 11, 1)
test2 = factory(5, 55, 5)
test3 = factory(12345, 123, 3)
