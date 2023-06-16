# Script for generating MemeAssembly code for a given output


import random
import sys
from typing import List, Tuple


def value_str(val: int) -> str:
    # printable ascii, but not whitespace
	if val > 32 and val <= 126:
		return str(chr(val))
	return str(val)

def simple_strategy(current_reg_value: int, reg_name: str, target: int) -> Tuple[List[str], int | None]:
	return ([
		"what can I say except " + value_str(target),
	], None)

def add_strategy(current_reg_value: int, reg_name: str, target: int) -> Tuple[List[str], int | None]:
	if current_reg_value == target:
		return ([
			"what can I say except " + reg_name,
		], current_reg_value)
	else:
		diff_val = target - current_reg_value
		if diff_val < 0:
			diff_val += 256

		return ([
			f"{reg_name} units are ready, with {diff_val} more well on the way",
			"what can I say except " + reg_name,
		], target)



possible_registers = [
	"al", "ah", "bl", "bh", "cl", "ch", "dl", "dh"
]

# a strategy gets the current value of a register, its name and the target value we want to get
# It returns an array of MemeAssembly commands and the new value of the register. If the register is not used, return None
strategies = [
	simple_strategy,
	add_strategy,
]

def convert_memeasm(target: str) -> str:
	output = []
	register_state = {}

	for i in range(len(target)):
		register = random.choice(possible_registers)

		is_new_register = register not in register_state
		register_val = random.randint(0, 255) if is_new_register else register_state[register]

		new_output, new_reg_val = random.choice(strategies)(register_val, register, ord(target[i]))
		if new_reg_val is not None:
			register_state[register] = new_reg_val

			if is_new_register:
				output.append(register + " is brilliant, but I like " + str(register_val))

		output.extend(new_output)

	return "\n\t".join(output)



joined_args = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Hello, World!"

print("I like to have fun, fun, fun, fun, fun, fun, fun, fun, fun, fun main\n\t" + convert_memeasm(joined_args) + "\n\tI see this as an absolute win")
