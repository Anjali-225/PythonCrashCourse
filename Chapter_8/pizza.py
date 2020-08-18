
def make_pizza(size, *toppings):
	"""Summarize the pizza we are about to make."""
	print(f"\nMaking a {size}-inch pizza with the following toppings:")
	for topping in toppings:
		print(f"- {topping}")

#from module_name import function_name
#from module_name import function_0, function_1, function_2
'''
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

from module_name import function_name as fn


import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

import module_name as mn

from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from module_name import *

def function_name(parameter_0, parameter_1='default value')

function_name(value_0, parameter_1='value')

def function_name(
parameter_0, parameter_1, parameter_2,
parameter_3, parameter_4, parameter_5):
function body...





