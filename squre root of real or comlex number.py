# square root of real or complex numbers using cmath module
import cmath
a=float(input("ENTER THE REAL PART OF COMPLEX NUMBER:"))
print('IF IMAGINARI NUMBER NOT AVILABLE PUT=0')
bj=float(input("ENTER THE IMAGINARY PART OF COMPLEX NUMBER:"))
number = a+bj

number_sqrt = cmath.sqrt(number)
# decimal upto 2 place
print('THE SQUARE ROOT OF NUMBER {0} IS {1:0.2f}+{2:0.2f}j'.format(number ,number_sqrt.real,number_sqrt.imag))
#thanks akhlakansari94@gmail.com