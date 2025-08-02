
import tkinter as tk



#def Hello():
 #   label = tk.Label(text= "Hello learners, welcome to tkinter tutorial" , bg= "green", fg="white").pack()

window = tk.Tk()
window.title("Simplilearn Tkinter tutorial")
window.geometry("600x500+300+100")


#greeting = tk.Label(text ="Hello learners, welcome to tkinter tutorial")
#greeting.place(x= 100, y=20)

#label = tk.Label(text ="Hello learners, welcome to tkinter tutorial", fg= "White", bg= "BLack" , width=50, height = 5)
#label.place(x=10,y=190)

#button = tk.Button(text = "click me to say Hi!!",width =25, height =2, bg= "white", fg="black", command=Hello)
#button.place(x=50,y=10)
#button.pack()

#label= tk.Label(text = "What is your name")
#entry =tk.Entry()

#label.pack()
#entry.pack()

# name = tk.Label(window, text="name").place( x=30, y=50)
# email = tk.Label(window, text="Email").place( x=30, y=90)
# password =tk.Label(window, text="Password").place( x=30, y=130)


# name_entry = tk.Entry(window).place( x=80, y=50)
# email_entry= tk.Entry(window).place( x=50+30, y=90)
# password_entry =tk.Entry(window).place( x=50+50, y=130)

# frame_a = tk.Frame()
# label_a = tk.Label(master = frame_a, text = " This is frame A", bg="#468284")
# label_a.pack()

# frame_b = tk.Frame()
# label_b = tk.Label(master = frame_b, text = " This is frame B", bg="#E9967A")
# label_b.pack()
# frame_b.pack()
# frame_a.pack()

border = {
    "flat": tk.FLAT,
    "sunken" : tk.SUNKEN, 
    "raised" :tk.RAISED,
    "groove":tk.GROOVE,
    "ridge": tk.RIDGE

}

# for relief_name, relief in border.items():
#     frame = tk.Frame(master = window, relief= relief, borderwidth = 5)
#     frame.pack(side = tk.LEFT)
#     label = tk.Label(master = frame , text = relief_name)
#     label.pack()

frame1 = tk.Frame(master = window, width= 100 , height = 100 , bg="red")

frame1.pack(fill = tk.X)

frame2 = tk.Frame(master = window, width= 100 , height = 100 , bg="blue")

frame2.pack(fill = tk.Y)

frame3 = tk.Frame(master = window, width= 100,height=100 , bg="yellow")

frame3.pack(fill = tk.Y)



window.mainloop()