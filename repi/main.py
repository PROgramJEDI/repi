# Regular Expression Programming Interface


class Expression(object):
	def times(self, n: int):
		return f'{self.__repr__()}{{{n}}}'

	def until(self):
		pass

	def beginswith(self):
		return f'^{self.__repr__()}'

	def endswith(self):
		return f'{self.__repr__()}$'

	def __add__(self, other):
		def remove_sides(string):
			first = string[0] == "'"
			last = string[-1] == "'"

			if first and last:
				return string[1:-1]
			elif first:
				return string[1:]
			return string[:-1]

		return f'{remove_sides(self.__repr__())}{remove_sides(other.__repr__())}'



class Range(Expression):
	def __init__(self, start: int = 0, end: int = 9):
		self._start = start
		self._end = end

		self.is_valid(self._start, self._end)
	

	def __repr__(self):
		self.is_valid(self._start, self._end)
		return r'\d' if self._start == 0 and self._end == 9 else f'[{self.start}-{self.end}]'
	
	def is_valid(self, start: int = 0, end: int = 9):
		assert (0 <= start <= 9) and (0 <= end <= 9) and (start <= end), 'set the range with numbers between 0 and 9\nand "start" should be bigger or equal to "end"!'

	@property
	def start(self):
		self.is_valid(self._start)
		return self._start

	@start.setter
	def start(self, value: int):
		self.is_valid(self._start)
		self._start = value

	@property
	def end(self):
		self.is_valid(end=self._end)
		return self._end 
		
	@end.setter
	def end(self, value):
		self.is_valid(end=self._end)
		self._end = value


def add(*exps):
	return ''.join(xp.__repr__() for xp in exps)