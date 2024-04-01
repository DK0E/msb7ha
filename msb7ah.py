import tkinter as tk 

count = 0 


def addNum():
    global count 
    count += 1
    counter_label.config(text="Counter: " + str(count))

def reset():
    global count 
    count = 0
    counter_label.config(text="Counter: " + str(count))


root = tk.Tk()
root.title("مسبحة ")

button = tk.Button(root, text = "click" , command= addNum)


button.pack()



reset = tk.Button(root, text = "Reset" , command= reset)
reset.pack()

counter_label = tk.Label(root, text="Counter: " + str(count))
counter_label.pack()

root.mainloop()
