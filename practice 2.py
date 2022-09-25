#1
import math
a = int(input("Enter a: "))
b = int(input("Enter b: "))
h = int(input("Enter h: "))
S = ((math.pow(a,2)+b)*h) / ((2*(a-b))+4)
print ('1 exercise  answer : ' + str("S={0:.2f}".format(S)))
#2
x = int(input("Enter x: "))
y = int(input("Enter y: "))
a = math.sqrt(math.cos(2*y)+math.sin(4*y) + math.sqrt(math.pow(math.e,x) + math.pow(math.e,(-x))))
b = math.pow(((math.pow(math.e,(-x))) + math.pow(math.e,x)),3) * math.pow((math.sin(4*y) + math.cos(2*y) - 2), 2)
H = a/b
print ('2 exercise answer: ' + str("H={0:.2f}".format(H)))
#1
x=2
y=1
z = math.pow(math.pow(x,y),x) + math.pow(x,math.pow(x,y)) - math.pow(x,4)
print('3(1) exercise exercise is: ' + str("z={0:.2f}".format(z)))
#2
x=1
y=4
z=3
f = math.pow(((1/math.tan(y))+6), 1/3) + math.sqrt((math.pow((x+1),3))/4*y-2*z)
print('3(2) exercise exercise is: ' + str("f={0:.2f}".format(f)))

#3
x = 3
y = 0.2
z = 5*x*y / math.pow(x,3) + math.exp(math.pow(x,2)) + math.sqrt(math.pow(1/math.sin(y),2) - math.pow(y,2))
print('3(3) exercise answer is: ' + str("z={0:.2f}".format(z)))

#4
x=3
y=5
z= math.sqrt(math.fabs(y))+(math.pow(math.atan(math.log(x)),3) / math.pow(x,y) - y +1 )
print('3(4) exercise answer is: ' + str("z={0:.2f}".format(z)))

#5
x=3
y=1
z=2
f = math.pow(4,(x*y)) - math.pow(x,(x*y)) + math.pow((x*y),z)
print('3(5) exercise answer is: ' + str("f={0:.2f}".format(f)))

#6
x=2
y=2
z=1
f =( 4*math.fabs(x) - x*y*math.pow(z,2) )/( x+math.exp(y*x)-2*y*z)
print('3(6) exercise answer is: ' + str("f={0:.2f}".format(f)))
#7
x=0.8
y=0.1
z=4
f = math.pow((1-x + (1/math.atan(x-7*y)))/(4*x*z-math.pow(math.log(y),2)),1/5)
print('3(7) exercise answer is: ' + str("f={0:.2f}".format(f)))
#8
x=3
y=1
z=3
f= 2*3*4/(math.pow(math.sin(x),3) + math.pow(math.tan(y),3)) - math.sqrt(math.pow(z,(x-y)))
print('3(8) exercise answer is: ' + str("f={0:.2f}".format(f)))
#9
x=4
f= math.pow(math.log(x-3),4)+math.pow(2,x)*math.pow(math.sin(3*x),2)
print('3(9) exercise answer is: ' + str("f={0:.2f}".format(f)))
#10
x=2
y=2
z=1
f = math.sqrt(0.6*x*y*z)+math.pow(math.pow(y,x),2) - math.exp(math.sin(2*math.pow(x,2)))
#11
x=0.5
y=2
f = (math.asin(math.pow(x,3)) - 6) / (8*(math.cos(4*y)-math.sin(4*x)))
print('3(11) exercise answer is: ' + str("f={0:.2f}".format(f)))
#12
x=2
y=1
z=3
f = ((math.fabs(math.log(math.pow(x,3))) + math.exp(2*x)) / (x+3.4)) - (math.pow((1/math.tan(3/x*y*z)),3))
print('3(12) exercise answer is: ' + str("f={0:.2f}".format(f)))