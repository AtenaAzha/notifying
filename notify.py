from tkinter import *

class publisher:
    def __init__(self):
        self.__observers = []
        self.last_book = None

    def register(self,observer):
        self.__observers.append(observer)
        
    def removing(self,observers_):
        self.__observers.pop(observers_)

    def  notifyAll(self,*args,**kargs):
        message =[]
        for observer in self.__observers:
           message.append(observer.notify(self,*args,**kargs))
        return '\n'.join(message)

    def add_book(self,book):
        self.last_book = book



class sms_subscriber:
    def __init__(self,publisher):
        publisher.register(self)

    def notify(self,*args,**kargs):
        return'new books are here we sent u some recomedation on sms'


class e_mail_subscriber:
    def __init__(self,publisher):
        publisher.register(self)

    def notify(self,*args,**kargs):
        return 'new books are here we sent u some recomedation on e_mail'


subject = publisher()
obs1 = sms_subscriber(subject)
obs2 = e_mail_subscriber(subject)




window = Tk()
window.geometry('500x700')
window.title('check')
lable1 = Label(window , text = '')
lable1.pack()
lable2 = Label(window , text = '')
lable2.pack()
status1 = IntVar()
status2 = IntVar()
Checkbutton(window , variable = status1).pack()
Checkbutton(window , variable = status2).pack()
def checking():
    
    

    if status1.get() == 1:
       
       obs1 = sms_subscriber(subject)
       output = subject.notifyAll()
       
       lable1.config(text = f'{output}')

    if status2.get() == 1:

        lable2.config(text = 'books new were sent on e_mail')


Button(window , text = 'press' , command = checking).pack()
window.mainloop()