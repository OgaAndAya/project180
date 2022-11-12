from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Language Translator")
root.geometry("500x500")
root.configure(background_color= "orange")

label= Label(root,text= "LANGUAGE TRANSLATOR",bg= "orange",font= "cursive")
label.place(relx=0.5,rely= 0.1,anchor= CENTER)
enter= Label(root,text="Enter Text",bg= "orange",font= "cursive")
enter.place(relx=0.2,rely=0.5,anchor=CENTER)
text_area= Text(root,bg= "orange",fg="cursive",height=50,wrap= WORD,width=75,padx=15,pady=20,bd=0)
text_area.place(relx=0.35,rely=0.5,anchor=CENTER)

root.mainloop()