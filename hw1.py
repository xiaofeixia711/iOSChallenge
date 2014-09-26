# hw1.py
# Luyao Hou + lhou + A

######################################################################
# Place your non-autograded solutions below here!
######################################################################
#
"""
Be sure to include all your non-autograded responses within this
triple-quoted text, which Python will basically ignore.
Also be sure to show your work.  Provide some simple explanation
as to how you derived your solution.  Don't be too detailed, just
enough so we can follow your logic.


1)
For funtion f,
denote z by x following all operations.

After executing z=x and z+=3,
z=x+3;

After z*=10,
z becomes 10x+30;

After z**=2,
z=(10x+3)**2=100x**2 + 60x + 9;

After z-=x, z=100x**2 + 59x +9;

let y=9-104046120906035084020967429491109643279
then 100x**2 + 59x + y=0
By implementing method isqrt(x),
the first root = (-59+isqrt(59**2-4*100*y))/(2*100)=1020030004000054323
the second root = (-59-isqrt(59**2-4*100*y))/(2*100)=-1020030004000054325

Therefore,x=1020030004000054323 and x=-1020030004000054325 are augument values that make the function return True




2)
For function g,
In the first place, x should be of int type

Express y in x:
x%x*x**x=0*(x**x)=0 as Python first computes ** and then % and * in order, x%x=0, 0 times anyting is 0
x**2%x/x=0 as Python computes x**2 first and then % and / in order. (x**2)%x gives 0, 0/x=0
x/x*x/2=1*x/2=x/2 as Python computes / and * in order.

Therefore, y=0+0+x/2
However, as x is of int type, there is truncation and y is not exactly x/2 when x is an odd number
x=2*y+1 if x is odd

Also, x cannot be zero as the program crashes when a number is divided by 0

Therefore,
for (2*y != x) to be True, x should be an odd number

For (x+y) == 1501:
x=2*y+1
2*y+1+y=1500
y=500
x=2*y+1=1001

Therefore, argument value of 1001 makes the function return True




3)
First look at statements that relats to d or relates d to x
(int(round(d) == x)) suggests that (x-0.5)<=d<(x+0.5)
Also, (x > d > 25), so 25 < (x-0.5) <= d < x and that d must have decimals

(d * 100 % 1 == 0) suggests that there is no decimal place for d*100
Therefore, the number of decimal places of d is greater than 0 and less than 3
Therefore, (d % 1) * 100) has its decimal part equal to 0 and e=int(round((d % 1) * 100))=int((d%1)*100)

Then look at the relationship between e and x
As 25 < (x-0.5) <= d < x and x is an integer, e must be greater or equal to 50

For ((x%10) == (e/10)):
the last digit of x equals to the first digit of e

For ((x/10) == (e%10)):
x must be less than 100 so that (x/10) and (e%10) are both one-digit numbers and can equal to each other
the first digit of x equals to the last digit of e
In order to achieve e>=50, the last digit of x be greater or equal to 5

Therefore, x should be any two-digit number that is greater than 25 and has last digit greater than 5
d should have an integer part of x-1 and its decimal part is the reverse of two digits of x

Therefore, one input that makes the funtion return True is h(87,86.78)

"""

######################################################################
# Place your autograded solutions below here
######################################################################

import math

def maximumHeartRate(age, gender):
	# You may assume that age is a positive integer and
	# gender a string and is either "male" or "female".
	# Given these values, use the formulas on this page to
	# compute and and return the maximum heart rate:
	#   http://www.aqua-calc.com/calculate/maximum-heart-rate
	# Actually, one difference: here you should return the
	# nearest int value to what the formula computes.
	# Remember that you may not use conditionals this week, so you
	# may have to use some boolean arithmetic on this problem (sigh).
	gen=bool(gender=='male')
	exactMhr=(190.2+gen*13.5)/(1+math.e**((0.0453-gen*0.0123)*(age-107.5+3.2*gen)))
	integerMhr=int(round(exactMhr))
	return integerMhr

def sphereVolumeFromSurfaceArea(surfaceArea):
	# Return the volume of a sphere given its surface area, which you may assume
	# is a float.  You may need to look up the formulas for the surface area
	# and volume of a sphere.
	radius=(surfaceArea/(4*math.pi))**0.5
	volume=radius**3*4/3*math.pi
	return volume

def isDivisible(x, y):
	# returns True if x and y are both integer types and x is divisible by y,
	# and False otherwise
	return bool(y!=0 and type(x)==int and type(y)==int and (float(x)/y)%1==0)

def pascalsTriangleValue(row, col):
	# Given int values row and col, this function
	# returns the value in the given row and column of Pascal's Triangle
	# where the triangle starts at row 0, and each row starts at column 0.
	# If row and col are not legal values, returns False, instead of crashing.
	# Hint: math.factorial may be helpful!
	testLegal=bool(type(row)==int and type(col)==int and row>=0 and col>=0 and row>=col)
	return (testLegal and math.factorial(row)/(math.factorial(col)*math.factorial(row-col)))

def nearestOdd(x):
	# Return the nearest odd integer to x, which may be a float.
	even=bool(x%2==0)
	isNegative=bool(x<0 and (x%2!=0))
	nearestOdd=(int(x)*even)+int(x/2)*2*(not even)+1-2*isNegative
	return nearestOdd

def rectanglesOverlap(left1, top1, width1, height1,
	                  left2, top2, width2, height2):
	# A rectangle can be described by its left, top, width, and height.
	# This function takes two rectangles described this way, and
	# returns True if the rectangles overlap at all (even if just at a point),
	# and False otherwise.
	bottomHigher=bool(((top1<top2) and (top1+height1)<top2) or ((top2<top1) and (top2+height2)<top1))
	widthLefter=bool(((left1<left2) and (left1+width1)<left2) or ((left1>left2) and (left2+width2)<left1))
	doesNotOverlap=bool(bottomHigher or widthLefter)
	doesOverlap=not doesNotOverlap
	return doesOverlap

def cosineZerosCount(r):
	# r is a float, and this function returns the integer
	# number of zeros of cosine(x) for r radians where 0 <= x <= r.
	# You may need to Google about the shape of the graph of cosine,
	# if you don't know where its zeros are (where it crosses the x axis).
	# For example, pi/2 is one such zero.  You can also look at the
	# test function below (as you should!) to see some others!
	num=int((r/(math.pi)+0.5))*(r>=0)
	return num

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

def almostEqual(d1, d2, epsilon=10**-3):
	return abs(d1 - d2) < epsilon

def testMaximumHeartRate():
	print "Testing maximumHeartRate()...",
	assert(maximumHeartRate(30, "male") == 188)
	assert(maximumHeartRate(30, "female") == 185)
	assert(maximumHeartRate(1, "male") == 197)
	assert(maximumHeartRate(1, "female") == 189)
	assert(maximumHeartRate(100, "male") == 109)
	assert(maximumHeartRate(100, "female") == 111)
	print "Passed!"


def testSphereVolumeFromSurfaceArea():
	print "Testing sphereVolumeFromSurfaceArea()...",
	# From http://www.aqua-calc.com/calculate/volume-sphere, with r=3, we see:
	assert(almostEqual(sphereVolumeFromSurfaceArea(452.38934),  904.77868) == True) # r=6
	assert(almostEqual(sphereVolumeFromSurfaceArea(113.09734), 113.09734) == True) # r=3
	assert(almostEqual(sphereVolumeFromSurfaceArea(452.38934),  904) == False) # r=6
	assert(almostEqual(sphereVolumeFromSurfaceArea(452.38934),  905) == False) # r=6
	assert(almostEqual(sphereVolumeFromSurfaceArea(113.09734), 113) == False) # r=3
	assert(almostEqual(sphereVolumeFromSurfaceArea(113.09734), 113.1) == False) # r=3
	print "Passed!"

def testIsDivisible():
	print "Testing isDivisible()...",
	assert(type(isDivisible(4, 2)) == bool)
	assert(isDivisible(4,2) == True)
	assert(isDivisible(2,4) == False)
	assert(isDivisible(2,2) == True)
	assert(isDivisible(2,0) == False)
	assert(isDivisible(0,2) == True)
	assert(isDivisible(3.4, 1.7) == False) # not integers
	assert(isDivisible(3.0, 2) == False) # not integers
	print "Passed!"

def testPascalsTriangleValue():
	print "Testing pascalsTriangleValue()...",
	assert(type(pascalsTriangleValue(0,0)) == int)
	assert(pascalsTriangleValue(0,0) == 1)
	assert(pascalsTriangleValue(1,0) == 1)
	assert(pascalsTriangleValue(1,1) == 1)
	assert(pascalsTriangleValue(2,0) == 1)
	assert(pascalsTriangleValue(2,1) == 2)
	assert(pascalsTriangleValue(2,2) == 1)
	assert(pascalsTriangleValue(3,0) == 1)
	assert(pascalsTriangleValue(3,1) == 3)
	assert(pascalsTriangleValue(3,2) == 3)
	assert(pascalsTriangleValue(3,3) == 1)
	assert(pascalsTriangleValue(8,3) == 56)
	assert(pascalsTriangleValue(3,3.5) == False) # 3.5 is not an int
	assert(pascalsTriangleValue(3,3.0) == False) # 3.0 is not an int
	assert(pascalsTriangleValue(3,-1) == False) # col -1 is out of range
	assert(pascalsTriangleValue(3,4) == False)  # col 4 is out of range for row 3
	assert(pascalsTriangleValue("dog", "cat") == False)  # ridiculous
	print "Passed!"

def testNearestOdd():
	print "Testing nearestOdd()...",
	assert(type(nearestOdd(3.0)) == int)
	assert(nearestOdd(0) == 1)
	assert(nearestOdd(0.75) == 1)
	assert(nearestOdd(1.0) == 1)
	assert(nearestOdd(1.9999) == 1)
	assert(nearestOdd(2.0) == 3)
	assert(nearestOdd(3) == 3)
	assert(nearestOdd(3.9999) == 3)
	assert(nearestOdd(4) == 5)
	assert(nearestOdd(-2.001) == -3)
	assert(nearestOdd(-2) == -1)
	assert(nearestOdd(-0.0001) == -1)
	print "Passed!"

def testRectanglesOverlap():
	print "Testing rectanglesOverlap()...",
	assert(type(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 2)) == bool)
	assert(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 2) == True)
	assert(rectanglesOverlap(1, 1, 2, 2, -2, -2, 6, 6) == True)
	assert(rectanglesOverlap(1, 1, 2, 2, 3, 3, 1, 1) == True)
	assert(rectanglesOverlap(1, 1, 2, 2, 3.1, 3, 1, 1) == False)
	assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 1.9) == False)
	assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 2) == True)
	print "Passed!"

def testCosineZerosCount():
	print "Testing cosineZerosCount()...",
	assert(type(cosineZerosCount(0)) == int)
	assert(cosineZerosCount(0) == 0)
	assert(cosineZerosCount(math.pi/2 - 0.0001) == 0)
	assert(cosineZerosCount(math.pi/2 + 0.0001) == 1)
	assert(cosineZerosCount(3*math.pi/2 - 0.0001) == 1)
	assert(cosineZerosCount(3*math.pi/2 + 0.0001) == 2)
	assert(cosineZerosCount(5*math.pi/2 - 0.0001) == 2)
	assert(cosineZerosCount(5*math.pi/2 + 0.0001) == 3)
	assert(cosineZerosCount(-math.pi/2 - 0.0001) == 0)
	assert(cosineZerosCount(-math.pi/2 + 0.0001) == 0)
	print "passed!"

def testAll():
	testMaximumHeartRate()
	testSphereVolumeFromSurfaceArea()
	testIsDivisible()
	testPascalsTriangleValue()
	testNearestOdd()
	testRectanglesOverlap()
	testCosineZerosCount()

if __name__ == "__main__":
    testAll()
