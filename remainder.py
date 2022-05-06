from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk
from plyer import notification
import time

t = Tk()
t.title("Notifier-app")
t.geometry("500x300")



def get_details():
    get_title = title_entry.get()
    get_msg = msg.get()
    get_time = time1.get()

    if get_title == "" or get_msg == "" or get_time == "":
        messagebox.showerror("Alert", "All fields need to be filled")
    else:
        int_time = int(float(get_time))
        min_to_sec = int_time * 60
        messagebox.showinfo("notifier set", "set notification")

        time.sleep(min_to_sec)

        notification.notify(title=get_title,
                            message=get_msg,
                            app_name="notifier",
                            timeout=10)



# Title
title_text = StringVar()
title_label = Label(t, text="Title to Notify", font=("bold", 10), pady=20, padx=20)
title_label.grid(row=0, column=0, sticky=W)
title_entry = Entry(t, textvariable=title_text)
title_entry.grid(row=0, column=1)
# label2
m_label = Label(t, text="Display Message", font=("poppins", 10))
m_label.grid(row=3, column=0, padx=20, pady=20)

# entry2
msg = Entry(t, width=40, font=("poppins", 13))
msg.grid(row=3 , column=1)

# label3
time_label = Label(t, text="Set Time", font=("poppins", 10))
time_label.place(x=50, y=175)

# entry3
time1 = Entry(t, width=5, font=("poppins", 13))
time1.place(x=123, y=175)

# label4
time_min_label = Label(t, text="min", font=("popopins", 10))
time_min_label.place(x=200, y=175)

# button
but = Button(t, text="SET NOTIFICATION", font=("poppins", 10, 'bold'), fg="#ffffff", bg="#528DFF", width=20,
             relief="raised", command=get_details)
but.place(x=100, y=230)

but2 = Button(t, text="Speak", font=("poppins", 10, 'bold'), fg="#ffffff", bg="#528DFF", width=10)
but2.place(x=300, y=230)

t.resizable(0, 0)
t.mainloop()
