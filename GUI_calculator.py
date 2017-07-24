from tkinter import *

window = Tk()
text_input=StringVar()
operator=""
text_input.set("Click some stuff")

#Do the math functions and collect the numbers
def numberClick(numbers):
    global operator
    if(numbers==":)"):
        operator=""
        text_input.set(operator)
        return
    if(numbers=="Enter"):
        sum=str(eval(operator))
        operator=sum
        text_input.set(operator)
        return
    operator=operator+str(numbers)
    text_input.set(operator)





#Make the buttons and text window
e1=Label(window,font=('arial',30,'bold'),textvariable=text_input,width=15)
e1.grid(row=0,column=0,columnspan=4)
smiley=Button(text=":)",command=lambda:numberClick(":)")).grid(row=1,column=0,sticky=N+S+E+W)
divide=Button(text="/",command=lambda:numberClick("/")).grid(row=1,column=1,sticky=N+S+E+W)
multiply=Button(text="*",command=lambda:numberClick("*")).grid(row=1,column=2,sticky=N+S+E+W)
minus=Button(text="-",command=lambda:numberClick("-")).grid(row=1,column=3,sticky=N+S+E+W)
seven=Button(text="7",command=lambda:numberClick(7)).grid(row=2,column=0,sticky=N+S+E+W)
eight=Button(text="8",command=lambda:numberClick(8)).grid(row=2,column=1,sticky=N+S+E+W)
nine=Button(text="9",command=lambda:numberClick(9)).grid(row=2,column=2,sticky=N+S+E+W)
plus=Button(text="+",command=lambda:numberClick("+")).grid(row=2,column=3,rowspan=2,sticky=N+S+E+W)
four=Button(text="4",command=lambda:numberClick(4)).grid(row=3,column=0,sticky=N+S+E+W)
five=Button(text="5",command=lambda:numberClick(5)).grid(row=3,column=1,sticky=N+S+E+W)
six=Button(text="6",command=lambda:numberClick(6)).grid(row=3,column=2,sticky=N+S+E+W)
one=Button(text="1",command=lambda:numberClick(1)).grid(row=4,column=0,sticky=N+S+E+W)
two=Button(text="2",command=lambda:numberClick(2)).grid(row=4,column=1,sticky=N+S+E+W)
three=Button(text="3",command=lambda:numberClick(3)).grid(row=4,column=2,sticky=N+S+E+W)
enter=Button(text="Enter",command=lambda:numberClick("Enter")).grid(row=4,column=3,rowspan=2,sticky=N+S+E+W)
zero=Button(text="0",command=lambda:numberClick(0)).grid(row=5,column=0,columnspan=2,sticky=N+S+E+W)
period=Button(text=".",command=lambda:numberClick(".")).grid(row=5,column=2,sticky=N+S+E+W)

window.mainloop()
