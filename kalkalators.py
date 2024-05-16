from tkinter import*
def btnClick(number):
    current=e.get()#nolasa sk
    e.delete(0,END)#nodzēš
    newNumber=str(current)+str(number)
    e.insert(0,newNumber)#ievada displejā
    return 0

def btnCommand(command):
    global number
    global num1 #lāiegaumē skaitlis un darbība
    global mathOp#matemātiskais operātors
    mathOp=command
    num1=int(e.get())
    e.delete(0,END)
    return 0

def Vienads():
    num2=int(e.get())
    result=0
    if mathOp=='+':
        result=num1+num2
    elif mathOp=='-':
        result=num1-num2
    elif mathOp=='*':
        result=num1*num2
    elif mathOp=='/':
        result=num1/num2
    else:
        result=0
    e.delete(0,END)
    e.insert(0,str(result))
    return 0

def notirit():
    e.delete(0,END)
    num1=0
    mathOp=""
    return 0

mansLogs=Tk()
mansLogs.title('Kalkalators')
e=Entry(mansLogs,width=19,bd=10,font=("Arial Black",20),justify="right")
btn0=Button(mansLogs,text='0',padx='40',pady='20',command=lambda:btnClick(0),bg='#ffd5d5') 
btn1=Button(mansLogs,text='1',padx='40',pady='20',command=lambda:btnClick(1),bg='#ffd5d5') 
btn2=Button(mansLogs,text='2',padx='40',pady='20',command=lambda:btnClick(2),bg='#ffd5d5') 
btn3=Button(mansLogs,text='3',padx='40',pady='20',command=lambda:btnClick(3),bg='#ffd5d5')
btn4=Button(mansLogs,text='4',padx='40',pady='20',command=lambda:btnClick(4),bg='#ffd5d5')
btn5=Button(mansLogs,text='5',padx='40',pady='20',command=lambda:btnClick(5),bg='#ffd5d5')
btn6=Button(mansLogs,text='6',padx='40',pady='20',command=lambda:btnClick(6),bg='#ffd5d5')
btn7=Button(mansLogs,text='7',padx='40',pady='20',command=lambda:btnClick(7),bg='#ffd5d5')
btn8=Button(mansLogs,text='8',padx='40',pady='20',command=lambda:btnClick(8),bg='#ffd5d5')
btn9=Button(mansLogs,text='9',padx='40',pady='20',command=lambda:btnClick(9),bg='#ffd5d5')

btnPlus=Button(mansLogs, text='+',padx='40',pady='20',command=lambda:btnCommand('+'),bg='#ffbd77')
btnMinus=Button(mansLogs, text='-',padx='40',pady='20',command=lambda:btnCommand('-'),bg='#ffbd77')
btnDevide=Button(mansLogs,text='/',padx='40',pady='20',command=lambda:btnCommand('/'),bg='#ffbd77')
btnReiz=Button(mansLogs,text='*',padx='40',pady='20',command=lambda:btnCommand('*'),bg='#ffbd77')
btnC=Button(mansLogs,text='C',padx='40',pady='20',command=notirit,bg='#e06666')
btnVien=Button(mansLogs,text='=',padx='40',pady='20',bg='#e06666',command=Vienads)

e.grid(row=0,column=0,columnspan=5)

btn7.grid(row=1,column=0)
btn8.grid(row=1,column=1)
btn9. grid(row=1,column=2)

btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)

btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1)
btn3.grid(row=3,column=2)

btn0.grid(row=4,column=1)
btnC.grid(row=4,column=0)
btnVien.grid(row=4,column=2)

btnPlus.grid(row=1,column=4)
btnMinus.grid(row=2,column=4)
btnDevide.grid(row=3,column=4)
btnReiz.grid(row=4,column=4)


mansLogs.mainloop()
