# !V'X

An esoteric Pʹʹ-like language.

!V'X is a minimalist language, designed to be hard. It was inspired by brainfuck.

# The Language

These are the instructions:

	[: A label. When a GOTO is encountered, it will go to the last label encountered.
	]: A GOTO.
	#: Skip the next instruction if the accumulator equals the following value.
	&: Print the value in the accumulator.
		- If the memory pointer points to the last place in memory, print it as a character.
	>: Go to the register specified by the following byte.
	+: Increment the value in the accumulator.
	-: Decrement the value in the accumulator.
	!: Move the value in the register to the next register with a 0.
		- If you use the ! operator when you're at the last place in memory, it will go to memory location #0.

A byte in !V'X is represented by an array of dots (1) and whitespace/lines (0).

There are four possible digits: {|,.,; and :}.

The actual byte array:

	[7][6][5][4]
	[3][2][1][0]

# A simple incrementer program:
	
	[&+#::::]
