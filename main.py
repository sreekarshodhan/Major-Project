from tkinter import *

root = Tk()
root.geometry('1080x720')
# add title
root.title("Three tabs")
root['bg'] = 'green'


# create canvas
def tab():
    def tab1():
        ct1 = Canvas(root, bg='blue', width=1500, height=800)
        ct1.place(x=1, y=1)
        label1 = Label(root, text="This is Remainder app", bg='blue', font=('Arial', 30))
        label1.place(x=300, y=300)
        Speak_b = Button(root, text="Speak", font=('poppins', 15))
        Speak_b.place(x=500, y=500)
        tab()

    def tab2():
        ct1 = Canvas(root, bg='orange', width=1500, height=800)
        ct1.place(x=1, y=1)
        label2 = Label(root, text="This is Note taking app", bg="orange", font=("Arial", 30))
        label2.place(x=300, y=300)
        Speak_b = Button(root, text="Speak", font=('poppins', 15))
        Speak_b.place(x=500, y=500)
        tab()

    def tab3():
        ct1 = Canvas(root, bg="light green", width=1500, height=800)
        ct1.place(x=1, y=1)
        label3 = Label(root, text="This is task scheduling", bg="light green", font=("Arial", 30))
        label3.place(x=300, y=300)
        Speak_b = Button(root, text="Speak", font=('poppins', 15))
        Speak_b.place(x=500, y=500)
        tab()

    c1 = Canvas(root, bg='brown', width=1500, height=50)
    c1.place(x=1, y=20)
    tab1_b = Button(root, text='Remainder App', font=('Arial', 10), command=tab1)
    tab1_b.place(x=150, y=35)
    tab1_b = Button(root, text='NoteTaking App', font=('Arial', 10), command=tab2)
    tab1_b.place(x=450, y=35)
    tab1_b = Button(root, text='Task Scheduler App', font=('Arial', 10), command=tab3)
    tab1_b.place(x=750, y=35)


Speak_b = Button(root, text="Speak", font=('poppins', 15))
Speak_b.place(x=500, y=500)

tab()
root.mainloop()
