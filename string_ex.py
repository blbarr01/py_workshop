pi = 3.14159
e = 2.71 
mol = 42 
g = 9.8 
cx = 3+1j 
h = 0xAf12
htd = h.__int__()

#using the .format() method
#make a multiline statement 
s = "eulor's number is {} and the gravitational \
constant is {}".format(e, g) 

# you can specify the index in the bracket
t = "eulor's number is {1} and the gravitational constant is {0}".format(g,e)

#order matters 
print("the meaning of life is %d \
and the value of pi is %.2f \
and a hex digit is %x"%( mol, pi, h))

#newest print format 
p = f"the value of pi is {pi}"

#how to print a complex 
i = "print my complex number %s" % cx.__str__()
print(i)
print(p)
print(s)
print(t)