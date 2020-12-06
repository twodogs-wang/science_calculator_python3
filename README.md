# science_calculator_python3
A science calculator developed with python3

This project is a science calculator:
it has two features, "define" and "test"
	
	define: this feature supports user to define its own functions. command is like:
define f a b = (+ a ( sin b))

This command defines function f = a + sin b, f is a function name and the rest is its 
expression.

	test: this feature supports user to test and assigns values to its pre-defined functions.
let's say a function f = a + sin b has been pre-defined. A command may be like this:
	
	test f 1 2
	This command means ask the program to calculate 1 + sin(2), also commands like test + 1 2
or test log 3 are also supported.

How the program works? RUN  main file