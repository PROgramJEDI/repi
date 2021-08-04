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
	def __init__(self, exp: str):
		self._exp = exp

	def __getitem__(self, index: int):
		return self.exp[index]

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

		first = self.exp if self.__is_close() else self.exp.exp
		second = other.exp if other.__is_close() else other.exp.exp

		return Expression(f'{remove_sides(first)}{remove_sides(second)}')

	def __is_close(self):
		return type(self) is Expression

	@property
	def exp(self): 
		return self._exp

	def times(self, n: int):
		assert n > 1 and isinstance(n, int), 'change "n" to be an integer greater than +1!'
		return Expression(f'{self.exp if self.__is_close() else self.exp.exp}{{{n}}}')

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

	def __is_valid(self, start, end):		
		if isinstance(start, int) and isinstance(end, int):
			assert (0 <= start <= 9) and (0 <= end <= 9) and (start <= end), 'set the range with numbers between 0 and 9, and "start" should be bigger or equal to "end"!'
			return

		from string import ascii_lowercase as ascii_L, ascii_uppercase as ascii_U
		
		are_lower = start.islower() and end.islower()
		position_check = ascii_L.index(start) <= ascii_L.index(end) if are_lower else ascii_U.index(start) <= ascii_U.index(end)
		assert position_check, '"start" and "end" should be Capitalized or exactly the opposite!'
	
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
