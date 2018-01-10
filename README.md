# !V'X

An esoteric Pʹʹ-like language.

!V'X is a minimalist language, designed to be hard. It was inspired by brainfuck.

# The Language

These are the instructions:

	[: A while statement. When a ] is encountered, it will go to the while that it's on the same layer as.
	]: Go to the while layer the symbol is on.
	#: Skip the next instruction if the current register equals the following value.
	&: Print the value in the current register.
		- If the memory pointer points to the last register, print it as a character.
	>: Go to the register specified by the following byte.
	+: Increment the value in the current register.
	-: Decrement the value in the current register.
	!: Overwrite the current register with the current command line argument.

A byte in !V'X is represented by an array of dots (1) and whitespace/lines (0).

There are four possible digits: {|,.,; and :}.

The actual byte array:

	[7][6][5][4]
	[3][2][1][0]
	
In !V'X, errors are _silently_ ignored. So if you made a mistake in your program, you would have to find it yourself.

# A simple incrementer program:
	
	[+&#::::]

# A not-so simple "Hello world!" program:
	
	>::::[+#.;||]&[+#|:;.]&+++++++&&+++&[-#..;|]&[-#||;|]&[+#|:.:]&[+#.::.]&+++&------&--------&[+#||;.]&
