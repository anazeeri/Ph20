import math

import numpy

import matplotlib.pyplot as plt

import sys

#Hi mom

def frange(start,stop,step):

    while start<stop:

        yield start

        start += step



print("What is the initial x?")

Xi = float(sys.argv[1])
print(Xi)

print("What is the initial v?")

Vi = float(sys.argv[2])
print(Vi)

print("What value for h?")

h = float(sys.argv[3])
print(h)

print("What value for N?")

N = int(sys.argv[4])
print(N)

print("What figure to return?")

fig = int(sys.argv[5])
print(fig)


ExplEuler  = numpy.empty((3,N))



ExplEuler[0,0] = Xi

ExplEuler[1,0] = Vi

ExplEuler[2,0] = 0



for i in range(1,N):

    ExplEuler[0,i] = ExplEuler[0,i-1] + h*ExplEuler[1,i-1]

    ExplEuler[1,i] = ExplEuler[1,i-1] -h*ExplEuler[0,i-1]

    ExplEuler[2,i] = i*h





Xlist = []

Ylist = []

Nlist = []



Xlist = ExplEuler[0:1]

Vlist = ExplEuler[1:2]

Nlist = ExplEuler[2:3]



#print(Xlist)

#print(Vlist)

#print(Nlist)


if fig==1:
	plt.plot(Nlist,Xlist,'ro')

	plt.suptitle('X vs Steps')

	plt.xlabel('Steps')

	plt.ylabel('X')

	plt.savefig(sys.argv[6])


if fig==2:
	plt.plot(Nlist,Vlist,'ro')
	
	plt.suptitle('V vs Steps')
	
	plt.xlabel('Steps')
	
	plt.ylabel('V')
	
	plt.savefig(sys.argv[6])



#Error analysis

Anal = numpy.empty((3,N))

Anal[2:3] = ExplEuler[2:3]

Anal[0:1] = numpy.cos(Anal[2:3])

Anal[1:2] = -numpy.sin(Anal[2:3])



aXlist = Anal[0:1]

aVlist = Anal[1:2]

aNlist = Anal[2:3]


if fig==3:
	plt.plot(Nlist,aXlist,'ro')
	
	plt.suptitle('Analytically Solved X vs Time')
	
	plt.xlabel('Time')
	
	plt.ylabel('Position')
	
	plt.savefig(sys.argv[6])


if fig==4:
	plt.plot(Nlist,aVlist,'ro')
	
	plt.suptitle('Analytically Solved V vs Time')
	
	plt.xlabel('Time')
	
	plt.ylabel('Velocity')
	
	plt.savefig(sys.argv[6])



ErrComp = ExplEuler - Anal

ErrComp[2:3] = ExplEuler[2:3]





ErrXlist = ErrComp[0:1]

ErrVlist = ErrComp[1:2]

ErrNlist = ErrComp[2:3]


if fig==5:
	plt.plot(ErrNlist,ErrXlist,'ro')
	
	plt.suptitle('Error X vs Time')
	
	plt.xlabel('Time')
	
	plt.ylabel('Error X')
	
	plt.savefig(sys.argv[6])


if fig==6:
	plt.plot(ErrNlist,ErrVlist,'ro')
	
	plt.suptitle('Error V vs Time')
	
	plt.xlabel('Time')
	
	plt.ylabel('Error V')
	
	plt.savefig(sys.argv[6])


if fig==7:
	plt.plot([0.01,0.005,0.0025,0.00125,0.000625,0.0003125],[0.002833225,0.001409682,0.000703106,0.000351119,0.000175451,8.77E-05],'ro')
	
	plt.suptitle('Trunctation Error vs h')
	
	plt.xlabel('h')
	
	plt.ylabel('Max Error')
	
	plt.savefig(sys.argv[6])



#if ErrXlist.max()>ErrXlist.min():

#    print(ErrXlist.max())

#else:

#    print(ErrXlist.min())



#Energy Calculations

Elist = []

Elist = (ExplEuler[0:1]*ExplEuler[0:1])+(ExplEuler[1:2]*ExplEuler[1:2])


if fig==8:
	plt.plot(Nlist,Elist,'ro')
	
	plt.suptitle('Energy vs Time')
	
	plt.xlabel('Time')
	
	plt.ylabel('Energy')
	
	plt.savefig(sys.argv[6])



#Implicit Calculations

IplEuler  = numpy.empty((3,N))



IplEuler[0,0] = Xi

IplEuler[1,0] = Vi

IplEuler[2,0] = 0



for i in range(1,N):

    ht=(1+h**2)

    IplEuler[0,i] = (IplEuler[0,i-1] + h*IplEuler[1,i-1])

    IplEuler[0,i] = numpy.divide(IplEuler[0,i],ht)

    IplEuler[1,i] = (IplEuler[1,i-1] -h*IplEuler[0,i-1])

    IplEuler[1,i] = numpy.divide(IplEuler[1,i],ht)

    IplEuler[2,i] = i*h





IXlist = []

IYlist = []

INlist = []



IXlist = IplEuler[0:1]

IVlist = IplEuler[1:2]

INlist = IplEuler[2:3]



#print(IXlist)

#print(IVlist)

#print(INlist)


if fig==9:
	plt.plot(INlist,IXlist,'ro')
	
	plt.suptitle('Implicit X vs Time')
	
	plt.xlabel('Time')
	
	plt.ylabel('X')
	
	plt.savefig(sys.argv[6])


if fig==10:
	plt.plot(INlist,IVlist,'ro')
	
	plt.suptitle('Implicit V vs Time')
	
	plt.xlabel('Time')
	
	plt.ylabel('V')
	
	plt.savefig(sys.argv[6])



#Implicit Error Analysis

IErrComp = IplEuler - Anal

IErrComp[2:3] = IplEuler[2:3]





IErrXlist = IErrComp[0:1]

IErrVlist = IErrComp[1:2]

IErrNlist = IErrComp[2:3]


if fig==11:
	plt.plot(IErrNlist,IErrXlist,'ro')
	
	plt.suptitle('Implicit Error X vs Time')
	
	plt.xlabel('Time')
	
	plt.ylabel('Error X')
	
	plt.savefig(sys.argv[6])


if fig==12:
	plt.plot(IErrNlist,IErrVlist,'ro')
	
	plt.suptitle('Implicit Error V vs Time')
	
	plt.xlabel('Time')
	
	plt.ylabel('Error V')
	
	plt.savefig(sys.argv[6])



if numpy.abs(IErrXlist.max())>numpy.abs(IErrXlist.min()):

    print(numpy.abs(IErrXlist.max()))

else:

    print(numpy.abs(IErrXlist.min()))


if fig==13:
	plt.plot([0.01,0.005,0.0025,0.00125,0.000625,0.0003125],[0.002777688,0.001395797,0.000699635,0.000350251,0.000175234,8.76E-05],'ro')
	
	plt.suptitle('Implicit Trunctation Error vs h')
	
	plt.xlabel('h')
	
	plt.ylabel('Max Error')
	
	plt.savefig(sys.argv[6])



#Implicit Energy Calculations

IElist = []

IElist = (IplEuler[0:1]*IplEuler[0:1])+(IplEuler[1:2]*IplEuler[1:2])


if fig==14:
	plt.plot(INlist,IElist,'ro')
	
	plt.suptitle('Implicit Energy vs Time')
	
	plt.xlabel('Time')
	
	plt.ylabel('Energy')
	
	plt.savefig(sys.argv[6])



#phase space calculations

SymEuler  = numpy.empty((3,N))



SymEuler[0,0] = Xi

SymEuler[1,0] = Vi

SymEuler[2,0] = 0



for i in range(1,N):

    SymEuler[0,i] = SymEuler[0,i-1] + h*SymEuler[1,i-1]

    SymEuler[1,i] = SymEuler[1,i-1] -h*SymEuler[0,i]

    SymEuler[2,i] = i*h





SymXlist = []

SymYlist = []

SymNlist = []



SymXlist = SymEuler[0:1]

SymVlist = SymEuler[1:2]

SymNlist = SymEuler[2:3]


if fig==15:
	plt.plot(Xlist,Vlist,'ro')
	
	plt.suptitle('Explicit X vs V')
	
	plt.xlabel('Position')
	
	plt.ylabel('Velocity')
	
	plt.savefig(sys.argv[6])


if fig==16:
	plt.plot(IXlist,IVlist,'ro')
	
	plt.suptitle('Implicit X vs V')
	
	plt.xlabel('Position')
	
	plt.ylabel('Velocity')
	
	plt.savefig(sys.argv[6])


if fig==17:
	plt.plot(aXlist,aVlist,'ro')
	
	plt.suptitle('Analytical X vs V')
	
	plt.xlabel('Position')
	
	plt.ylabel('Velocity')
	
	plt.savefig(sys.argv[6])


if fig==18:
	plt.plot(SymXlist,SymVlist,'ro')
	
	plt.suptitle('Symplectic X vs V')
	
	plt.xlabel('Position')
	
	plt.ylabel('Velocity')
	
	plt.savefig(sys.argv[6])



#Symplectic Energy Calculations

SymElist = []

SymElist = (SymEuler[0:1]*SymEuler[0:1])+(SymEuler[1:2]*SymEuler[1:2])


if fig==19:
	plt.plot(SymNlist,SymElist,'ro')
	
	plt.suptitle('Implicit Energy vs Time')
	
	plt.xlabel('Time')
	
	plt.ylabel('Energy')
	
	plt.savefig(sys.argv[6])

#Here is my change for the 4th set. I hate mercurial.

print("I'll be back!")
