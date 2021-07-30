# Regular Expression Programming Interface


DIGIT       = r'\d'
WORDCHAR    = r'\w'
WHITESPACE  = r'\s'
WORDBOUNDRY = r'\b'

NOT_DIGIT       = r'\D'
NOT_WORDCHAR    = r'\W'
NOT_WHITESPACE  = r'\S'
NOT_WORDBOUNDRY = r'\B'



class Expression(object):
	def __init__(self, exp: str):
		self._exp = exp

	def __getitem__(self, index):
		return self._exp[index]

	def __repr__(self): 
		return self.exp

	def __add__(self, other):
		def remove_sides(exp: str):
			first = (exp[0] == "'")
			last = (exp[-1] == "'")

			if first and last:
				return exp[1:-1]
			elif first:
				return exp[1:]
			elif last:
				return exp[:-1]
			return exp

		return Expression(f'{remove_sides(self.exp)}{remove_sides(other.exp)}')

	@property
	def exp(self): 
		return self._exp

	def times(self, n: int):
		assert n > 1 and isinstance(n, int), 'change "n" to be greater than +1 and an integer!'
		return Expression(f'{self.exp}{{{n}}}')

	def until(self):
		pass

	def beginswith(self): 
		return Expression(f'^{self.exp}')

	def endswith(self): 
		return Expression(f'{self.exp}$')



class Range(Expression):
	def __init__(self, start, end):
		self._start = start
		self._end = end

		self.__is_valid(self._start, self._end)

	def __repr__(self):
		return self.exp.exp

	@property
	def exp(self):
		a, b = self.start, self.end
		return Expression(r'\d' if a == 0 and b == 9 else f'[{a}-{b}]')
	
	@property
	def start(self):
		return self._start

	@start.setter
	def start(self, value):
		self.__is_valid(self._start, self._end)
		self._start = value

	@property
	def end(self):
		return self._end 
		
	@end.setter
	def end(self, value):
		self.__is_valid(self._start, self._end)
		self._end = value

	def __is_valid(self, start, end):		
		if isinstance(start, int) and isinstance(end, int):
			assert (0 <= start <= 9) and (0 <= end <= 9) and (start <= end), 'set the range with numbers between 0 and 9, and "start" should be bigger or equal to "end"!'
			return

		from string import ascii_lowercase as ascii_L, ascii_uppercase as ascii_U

		magnitude_check = (start.islower() and end.islower()) or (start.isupper() and end.isupper())
		position_check = (ascii_L.index(start) <= ascii_L.index(end)) or (ascii_U.index(start) <= ascii_U.index(end))

		assert position_check, '"start" and "end" should be Capitalized or exactly the opposite!'



class OR(Expression):
	# OR(Range(0,4), Range('a', 'z')
	# OR('a', 'z')
	# OR(1, 3)
	pass



def add(*exps):
	return ''.join(xp.exp for xp in exps)
