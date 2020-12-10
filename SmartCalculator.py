from tkinter import *
import tkinter.messagebox as tmsg

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def mod(a,b):
    return a % b

def lcm(a,b):
    L = a if a>b else b
    while L <= a*b:
        if L%a == 0 and L%b == 0:
            return L
        L+=1

def hcf(a,b):
    H = a if a<b else b
    while H >= 1:
        if a%H == 0 and b%H == 0:
            return H
        H-=1

def extraxt_from_text(text):
    l = []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l

def term_of_use():
    tmsg.showinfo('Terms of Use ','This Smart Calculator will work only for two numbers. Make sure you give input according to this term.')

def send_feedback():
    ans=tmsg.askquestion('Feedback Hub','Was your experience good with us ? ')
    if ans=='yes':
        tmsg.showinfo('Feedback','Please Rate us on PlayStore')
    else:
        tmsg.showinfo('Feedback','We will contact you soon to know about your bad experience')


def calculate():
    text = textin.get()
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l = extraxt_from_text(text)
                r = operations[word.upper()](l[0] , l[1])
                list.delete(0,END)
                list.insert(END,r)
            except:
                list.delete(0,END)
                list.insert(END,'Something went wrong...')
                list.insert(END,'Please Enter Valid digits!')
            finally:
                break
        elif word.upper() not in operations.keys():
            list.delete(0,END)
            list.insert(END,'Something went wrong...')
            list.insert(END,'Please Enter Valid Operations!')
            

operations = {'ADD':add , 'ADDITION':add , 'SUM':add , 'PLUS':add ,
                'SUB':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,
                 'LCM':lcm , 'HCF':hcf , 'PRODUCT':mul , 'MULTIPLICATION':mul, 'MUL':mul,
                 'MULTIPLY':mul , 'DIVISION':div , 'DIV':div ,'DIVIDE':div, 'MOD':mod ,
                  'REMANDER':mod , 'MODULUS':mod , '+': add, '-':sub, '*':mul, '/':div, '%':mod}

win=Tk()
canvas_width=600
canvas_height=350
win.geometry(f'{canvas_width}x{canvas_height}')
win.maxsize(canvas_width,canvas_height)
win.minsize(canvas_width,canvas_height)
win.configure(bg='lightskyblue')
win.title('Smart Calculator')

l1 = Label(win , text='Hey! My name is Monty',width=20 , padx=3)
l1.place(x=220,y=10)
l2 = Label(win , text='I can perform Addition, subtraction, Multiplication, Division, LCM, and HCF between two digits.' , padx=3)
l2.place(x=40,y=50)
l3 = Label(win , text='What can I do for you ?' , padx=3)
l3.place(x=220,y=150)

textin = StringVar()
e1 = Entry(win , width=50 , textvariable = textin)
e1.place(x=140,y=180)

b1 = Button(win , text='Just this' ,command=calculate)
b1.place(x=260,y=250)

list = Listbox(win,width=30,height=2)
list.place(x=200,y=280)

my_menu=Menu(win)
m1=Menu(my_menu,tearoff=0,fg='black')
m1.add_command(label='Terms of Use',command=term_of_use)
m1.add_command(label='Send Feedback',command=send_feedback)
win.config(menu=my_menu)
my_menu.add_cascade(label=' About ',menu=m1)
my_menu.add_command(label='Exit',command=quit)

win.mainloop()
