# !V'X

An esoteric Pʹʹ-like language.

!V'X is a minimalist language, designed to be hard. It was inspired by brainfuck.

These are the instructions:

\[: A label. When a GOTO is encountered, it will go to the last label encountered.
]: A GOTO.
&: Print the value in the accumulator.
!: On the next print, print the value as if it were a character.
#: Skip the next instruction if the accumulator equals the following value.
+: Increment the value in the accumulator.
-: Decrement the value in the accumulator.
\_: Halt the program.
