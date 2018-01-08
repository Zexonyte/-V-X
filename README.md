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
	!: Move the value in the current register to the next register.
		- If you use the ! operator when you're at the last register, it will assign the byte to register #0.

A byte in !V'X is represented by an array of dots (1) and whitespace/lines (0).

There are four possible digits: {|,.,; and :}.

The actual byte array:

	[7][6][5][4]
	[3][2][1][0]

# A simple incrementer program:
	
	[+&#::::]

# A not-so simple "Hello world!" program:
	
	>::::[+#.;||]&[+#|:;.]&+++++++&&+++&[-#..;|]&[-#||;|]&[+#|:.:]&[+#.::.]&+++&------&--------&[+#||;.]&
