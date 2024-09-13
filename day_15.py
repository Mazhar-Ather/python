# good morning sir
import datetime
nw=datetime.datetime.now()
print(nw)
a=int(nw.strftime('%H'))
if a>=6 and a<=12:
    print("GOOD MORNING SIR")
if a>12 and a<=18:
    print("GOOD afternoon SIR")
if a>18 and a<=24:
    print("GOOD night SIR") 
if a>=1 and a<6:
    print("Closed")           