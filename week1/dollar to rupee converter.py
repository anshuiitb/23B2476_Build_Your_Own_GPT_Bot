def convert():
    c=int(e1.get())
    f=float(82.71)*c
    t1.config(state='normal')
    t1.delete('1.0', tk.END)
    t1.insert(tk.END,f)
    t1.config(state ='Disabled')





import tkinter as tk

window=tk.Tk()
window.geometry("300x250")
window.config(bg="#E9967A")
window.resizable(width="false" , height="false")
window.title("Dollar to ruppe converter")





l1 = tk.Label(window ,text = "Dollar to ruppe converter", font=("Arial" , 15), fg="white" , bg="#C0C0C0")
l2 = tk.Label(window ,text="Enter dollar amount", font=("Arial", 10, "bold"),fg = "white", bg="#A569BD")

l3=tk.Label(window , text="Amount in ruppes: ", font=("Arial", 10, "bold"),fg = "white", bg="#A569BD")

empty_l1=tk.Label(window, bg="#E9967A")
empty_l2=tk.Label(window, bg="#E9967A")

# l1.place(x=50 , y=10)
# l2.place(x=50 ,y=40)
# l3.place(x= 50 ,y= 70)
e1 = tk.Entry(window , font=("Arial",10))
btn1 = tk.Button(window,text="Convert to ruppe", font=("Arial", 10), command= convert)

t1= tk.Text(window, state="disable", width =15, height=0)

l1.pack()
l2.pack()
e1.pack()
btn1.pack()
l3.pack()
t1.pack()

window.mainloop()

