# Regular Expression Programming Interface

DIGIT      		= r'\d'
WORDCHAR    	= r'\w'
WHITESPACE 		= r'\s'
WORDBOUNDRY 	= r'\b'

NOT_DIGIT       = r'\D'
NOT_WORDCHAR    = r'\W'
NOT_WHITESPACE  = r'\S'
NOT_WORDBOUNDRY = r'\B'



class Expression(object):
	def __init__(self, string: str):
		self._string = string

	def __getitem__(self, index: int):
		return self.string[index]

	def __add__(self, other):
		def remove_sides(string: str):
			first = (string[0] == "'")
			last = (string[-1] == "'")

			if first and last:
				return string[1:-1]
			elif first:
				return string[1:]
			elif last:
				return string[:-1]
			return string

		self.string = f'{remove_sides(self.string)}{remove_sides(other.string)}'
		return self

	@property
	def string(self): 
		return self._string

	@string.setter
	def string(self, value):
		self._string = value

	def times(self, n: int):
		assert n > 1 and isinstance(n, int), 'change "n" to be an integer greater than +1!'
		self.string = f'{self.string}{{{n}}}'
		return self

	def until(self):
		pass

	def beginswith(self): 
		self.string = f'^{self.string}'
		return self

	def endswith(self): 
		self.string = f'{self.string}$'
		return self

	def OR(self, exp):
		# convert the expression to Expression, if it's not in that type.
		exp = Expression(exp) if type(exp) in (int, str, float) else exp
		# check and convert to all types being Expression objects.
		exp, self = list(map(lambda x: x if type(x) is Expression else x.exp, (exp, self)))
		self.string = f'({self.string}|{exp.string})'
		return self



class Range(Expression):
	def __init__(self, start, end):
		self._start = start
		self._end = end

		self.__is_valid(self._start, self._end)

	def __is_valid(self, start, end):		
		if isinstance(start, int) and isinstance(end, int):
			assert (0 <= start <= 9) and (0 <= end <= 9) and (start <= end), 'set the range with numbers between 0 and 9, and "start" should be bigger or equal to "end"!'
			return None

		from string import ascii_lowercase as ascii_L, ascii_uppercase as ascii_U
		
		are_lower = start.islower() and end.islower()
		position_check = ascii_L.index(start) <= ascii_L.index(end) if are_lower else ascii_U.index(start) <= ascii_U.index(end)
		assert position_check, '"start" and "end" should be following letters with the same shape (capitalized/non-capitalized)!'
	
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
