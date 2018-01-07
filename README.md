# !V'X

An esoteric Pʹʹ-like language.

!V'X is a minimalist language, designed to be hard. It was inspired by brainfuck.

# The Language

These are the instructions:

	[: A label. When a GOTO is encountered, it will go to the last label encountered.
	]: A GOTO.
	&: Print the value in the accumulator.
	!: On the next print, print the value as if it were a character.
	#: Skip the next instruction if the accumulator equals the following value.
	+: Increment the value in the accumulator.
	-: Decrement the value in the accumulator.
	_: Halt the program.

A byte in !V'X is represented by an array of dots (1) and whitespace/lines (0).

There are four possible digits: {|,.,; and :}.

The actual byte array:

	[7][6][5][4]
	[3][2][1][0]

# A simple incrementer program:
	
	[&+#::::]
