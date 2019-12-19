Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def new_line():
	print('.')

	
>>> def three_lines():
	new_line()
	new_line()
	new_line()

	
>>> def nine_lines():
	three_lines()
	three_lines()
	three_lines()

	
>>> def clear_screen():
	nine_lines()
	nine_lines()
	three_lines()
	three_lines()
	new_line()

	
>>> print("Printing nine lines...")
Printing nine lines...
>>> nine_lines()
.
.
.
.
.
.
.
.
.
>>> print("Calling clear_screen() function...")
Calling clear_screen() function...
>>> clear_screen()
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
>>> 
