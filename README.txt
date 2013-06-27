OpenPyCalc

Author: Ravi Malik

Copyright (C) 2011-2013  Ravi Malik

INTRODUCTION:

This project is basically a calculator program implemented completely in Python. All the algorithms for calculating the expressions are also coded in Python. 

Why this project was made?

This project was initially made with the purpose of learning. I was interested in how a calculator and other tools used to evaluate expressions to generate results out of them. Some of those other tools were the Python interpreter and many such programming languages. Exploring how it was done, I came across the concepts of Infix to Postfix Conversion and Postfix Evaluation and decided to implement them on my own to have a better understanding of them. Initially only the arithmetic expressions were supported and with further improvements it grew into a calculator that could support trignometric functions too. And with the inclusion of a GUI it stepped into the realms of user friendliness.

Some of the features of this Project:
1. Support for arithmetic expressions like addition, subtraction, multiplication, division.
2. Support for trignometric functions like sine(), cosine().
3. And some other functions like abs(), fact(), sqrt(). 

SOME OF THE ALGORITHMS USED IN THIS PROJECT:
1. Infix to Postfix conversion
2. Postfix Evaluation

A little description of the files of the project:
1. calc.py :
	This python file contains the core of the calculator, i.e. all the logics which perform calculations are present here. It is intended as a module on top of which interfaces could be built.

2. run.py :
	This is the interface to the calc.py file, which is built using the Python Tkinter GUI module.
