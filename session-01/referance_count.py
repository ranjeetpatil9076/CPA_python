Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> n = 327698658
>>> print(n)
327698658
>>> id(n)
2921647010032
>>> type(n)
<class 'int'>
>>> import sys
>>> sys.getrefcount(n)
2
>>> 
>>> #here we are having reference count of variable n is two
>>> #why this referance count is two insted of one coz object have attached only one name but it has to be getting referance count is two
>>> #getrefcount is one of the algoritham and this alogorithm needed input and it will give the desired output .!
>>> #so gaterefcount will take n input to giive the referance count .
>>> help (sys.getrefcount)
Help on built-in function getrefcount in module sys:

getrefcount(object, /)
    Return the reference count of object.

    The count returned is generally one higher than you might expect,
    because it includes the (temporary) reference as an argument to
    getrefcount().

