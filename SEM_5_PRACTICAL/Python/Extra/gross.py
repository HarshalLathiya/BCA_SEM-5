from employee import *
#calculate gross salary of employee by taking basic
basic=float(input("enter basic salary: "))
#calculate gross salary
gross=basic+da(basic)+hra(basic)
print("YOur gross salary :{:10.2f}".format(gross))
#calculate net salary
net=gross-pf(basic)-itax(gross)
print("Your net salary : {:10.2f}".format(net))