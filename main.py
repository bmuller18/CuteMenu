from tkinter import *
import tkinter

textcolor = "#f56eb3"
lorem = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
text_center = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""
#DONT TOUCH ANYTHING----------------------------------------------------------------
root = Tk()
root.state("zoomed")
widthroot = root.winfo_screenwidth()
heightroot = root.winfo_screenheight()
root.geometry("%dx%d" % (widthroot, heightroot))
#-----------------------------------------------------------------------------------



top_label = Label(root, bg="#7f167f", fg=textcolor,text="Lorem Ipsum", font="Helvetica 32 bold", 
                    border=1, relief="solid")
top_label.pack(fill=X, side=TOP)

center_label = Label(root, bg="#460c68")

left_center_label = Label(center_label, bg="#7f167f", width=30, height=40, border=1, relief="solid")
left_center_label.grid(row=0, column=0)
center_center_label = Label(center_label, bg="#cb1c8d", text=text_center, width=200, height=40, border=1, relief="solid")
center_center_label.grid(row=0, column=1)

homebtn = Button(left_center_label, text="Home", fg="#f56eb3", bg="#7f167f").pack(side=TOP)

center_label.pack(fill=Y)

botom_label = Label(root, justify=CENTER,bg= "#460c68", text=lorem, fg=textcolor, height=2, width=30, 
                        border=1, relief="solid")
botom_label.pack(fill=BOTH, side=BOTTOM)

root.mainloop()