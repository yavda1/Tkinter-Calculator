from tkinter import *
import numpy
import math

root = Tk()
ans = ["", ""]
intL = []
# global ans
Second = False
Addition = False
result = 0
issqroot=False
MulAA = False
answ = 0
isFact = False
resultA = 0
SubAA = False
DiviA = False
root.title("Calculator")
Output = Label(root, text=f"")
numlab = Label(root, text="", font=("Arial", 50))
numlab.pack()

def multiplyList(myList):
    global result
    global answ

    result = 0
    for x in myList:
        result = result + x
    # return result
    # answ = result


def RemoveL():
    Output.pack_forget()


def AddNumA():
    if Second == False:
        ans[0] = ans[0] + "1"
        numlab.config(text=ans[0])

    else:
        ans[1] = ans[1] + "1"
        numlab.config(text=ans[1])


def AddNumB():
    if Second == False:
        ans[0] = ans[0] + "2"
        numlab.config(text=ans[0])

    else:
        ans[1] = ans[1] + "2"
        numlab.config(text=ans[1])


def AddNumC():
    if Second == False:
        ans[0] = ans[0] + "3"
        numlab.config(text=ans[0])
    else:
        ans[1] = ans[1] + "3"
        numlab.config(text=ans[1])


def AddNumD():
    if Second == False:
        ans[0] = ans[0] + "4"
        numlab.config(text=ans[0])
    else:
        ans[1] = ans[1] + "4"
        numlab.config(text=ans[1])


def AddNumE():
    if Second == False:
        ans[0] = ans[0] + "5"
        numlab.config(text=ans[0])
    else:
        ans[1] = ans[1] + "5"
        numlab.config(text=ans[1])


def AddNumF():
    if Second == False:
        ans[0] = ans[0] + "6"
        numlab.config(text=ans[0])
    else:
        ans[1] = ans[1] + "6"
        numlab.config(text=ans[1])


def AddNumG():
    if Second == False:
        ans[0] = ans[0] + "7"
        numlab.config(text=ans[0])
    else:
        ans[1] = ans[1] + "7"
        numlab.config(text=ans[1])


def AddNumH():
    if Second == False:
        ans[0] = ans[0] + "8"
        numlab.config(text=ans[0])
    else:
        ans[1] = ans[1] + "8"
        numlab.config(text=ans[1])


def AddNumI():
    if Second == False:
        ans[0] = ans[0] + "9"
        numlab.config(text=ans[0])
    else:
        ans[1] = ans[1] + "9"
        numlab.config(text=ans[1])


def AddNumJ():
    if Second == False:
        ans[0] = ans[0] + "0"
        numlab.config(text=ans[0])
    else:
        ans[1] = ans[1] + "0"
        numlab.config(text=ans[1])


def AdditionA():
    global answ
    global Second
    global Addition
    Second = True
    Addition = True


def MulA():
    global Second
    global MulAA
    Second = True
    MulAA = True


def DivA():
    global Second
    global DiviA
    Second = True
    DiviA = True


def SubA():
    global Second
    global SubAA
    Second = True
    SubAA = True


def factorial():
    global Second
    global isFact
    Second = False
    isFact = True
def squared():
    global issqu
    global Second
    Second=True
    issqu=True
def findsqrt():
    global Second
    global issqroot
    Second =True
    issqroot=True
def Equals():
    global isFact
    global Addition
    
    global Second
    global ans
    global MulAA
    global SubAA
    global DiviA
    global issqroot
    global issqu
    if Addition == True and Second == True:
        intL = [int(item) for item in ans]
        Second = False
        Addition = False
        multiplyList(intL)

        del ans
        ans = ["", ""]

        numlab.config(text=result)

    if MulAA == True and Second == True:
        intLL = [int(item) for item in ans]
        # print(intLL)
        resultC = numpy.prod(intLL)

        MulAA = False
        Second = False
        del ans
        ans = ["", ""]
        Output.pack()
        numlab.config(text=resultC)
        root.after(2000, RemoveL)
    if DiviA == True and Second == True:
        # print("A")
        intLLL = [int(item) for item in ans]
        # print(intLL)
        resultD = numpy.divide(intLLL[0], intLLL[1])

        Second = False
        DiviA = False
        del ans
        ans = ["", ""]

        numlab.config(text=resultD)

        root.after(2000, RemoveL)
    if SubAA == True and Second == True:
        intLLLL = [int(item) for item in ans]
        resultE = intLLLL[0] - intLLLL[1]

        Second = False
        SubAA = False
        del ans
        ans = ["", ""]
        numlab.config(text=resultE)
        root.after(2000, RemoveL)
    if isFact == True:
        anks = int(ans[0])

        resultH = math.factorial(anks)

        Second = False
        SubAA = False
        del ans
        ans = ["", ""]
        numlab.config(text=resultH)
        root.after(2000, RemoveL)
        Second = False
        isFact= False
    if issqroot == True:
        
        vaeff=ans[0]
        vaeff=int(vaeff)
        resultforthis= math.sqrt(vaeff)

        Second = False
        SubAA = False
        del ans
        ans = ["", ""]
        numlab.config(text=resultforthis)
        root.after(2000, RemoveL)
        Second = False
        issqroot= False
    if issqu == True:
        intLLLLLLLL = [int(item) for item in ans]
        vaeff=intLLLLLLLL[0]
        varef=intLLLLLLLL[1]
        resultforthis= vaeff**varef

        Second = False
        SubAA = False
        del ans
        ans = ["", ""]
        numlab.config(text=resultforthis)
        root.after(2000, RemoveL)
        Second = False
        issqu= False
highlightbackground="#ffffff"

root.geometry("400x550")
One = Button(root, text="1", command=AddNumA,width=7,height=5)
Two = Button(root, text="2", command=AddNumB,width=7,height=5)
Three = Button(root, text="3", command=AddNumC,width=7,height=5)
Four = Button(root, text="4", command=AddNumD,width=7,height=5)
Five = Button(root, text="5", command=AddNumE,width=7,height=5)
Six = Button(root, text="6", command=AddNumF,width=7,height=5)
Seven = Button(root, text="7", command=AddNumG,width=7,height=5)
Eight = Button(root, text="8", command=AddNumH,width=7,height=5)
Nine = Button(root, text="9", command=AddNumI,width=7,height=5)
Zero = Button(root, text="0", command=AddNumJ,width=7,height=5)
Add = Button(root, text="+", command=AdditionA,width=7,height=5)
EqualsA = Button(root, text="=", command=Equals,width=7,height=5)
Div = Button(root, text="÷", command=DivA,width=7,height=5)
Sub = Button(root, text="-", command=SubA,width=7,height=5)
Mul = Button(root, text="x", command=MulA,width=7,height=5)
fac = Button(root, text="!", command=factorial,width=7,height=5)
per = Button(root, text="√x", command=findsqrt,width=7,height=5)
squar = Button(root, text="x²", command=squared,width=7,height=5)

# ans = []
One.place(x=0,y=130)
Two.place(x=100,y=130)
Three.place(x=200,y=130)
Add.place(x=300,y=130)
Four.place(x=0,y=230)
Five.place(x=100,y=230)
Six.place(x=200,y=230)
Sub.place(x=300,y=230)
Eight.place(x=0,y=330)
Nine.place(x=100,y=330)
Zero.place(x=200,y=330)
Mul.place(x=300,y=330)
EqualsA.place(x=300,y=430)
Div.place(x=0,y=430)
per.place(x=100,y=430)
squar.place(x=200,y=430)


root.mainloop()
