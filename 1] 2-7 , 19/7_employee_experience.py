# w.a.p to take years of experience and display employee position ; 0&1-fresher 1&2-senior , 2&3 - teamlead
s=float(input('Enter employee experience : '))     #to input experience
if s>=0 and s<1:            #first condition
    print('fresher')
elif s>=1 and s<2:          #second condition
    print('senior')
elif s>=2 and s<3:          #third condition
    print('teamlead')
else:                       #if experience is greater than 3 or negative
    print('Enter valid experience')