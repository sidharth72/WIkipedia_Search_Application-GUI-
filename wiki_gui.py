from tkinter import *
import wikipedia as wk


# UI
root = Tk()
root.title("Wikipedia Mini")
heading = Frame(root)
frame = Frame(root)
result = Frame(root)


Label(heading,
	text="Wikipedia Mini",
	pady=20,
	font=("Times",30,'bold')).pack(side=TOP)

Label(frame,text='Search here:').pack(side=LEFT)

Label(result, 
	text='Search results:',
	pady=1,
	font=("Arial",17)).pack(side=LEFT)


input_box = Entry(frame,width=50)
input_box.pack(side=LEFT, fill=BOTH, expand=5)
input_box.focus_set()

query = ''
text = Text(root,font=("Roboto",13),padx=55,pady=10)


# search function
def Search():

	global query
	query = input_box.get()
	try:
		summary = wk.summary(query)
		text.insert('1.0',summary)
	except:
		text.insert('1.0','No results')



butt = Button(frame, text='Search',command=Search) 
butt.pack(side=RIGHT)

heading.pack()
frame.pack(side=TOP)
result.pack(side=TOP,fill=BOTH,pady=20,padx=50)
text.pack()

root.mainloop()

import tkinter


