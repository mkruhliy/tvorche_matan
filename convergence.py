import tkinter as tk
import sys
from calculus import Series

def clearFrame():
    for widget in frame.winfo_children():
       widget.destroy()

def evaluate():

    def calculate():
        labl1['text'] = Series(exsprs.get()).calc()
    
    def reset():
        labl1['text'] = '0.0'

    clearFrame()

    exsprs=tk.StringVar()

    tk.Label(frame, text=' ', height=3).grid(row=0, column=1, columnspan=2)
    labl1 = tk.Label(frame, text='0.0', font=('Arial', 13), height=3)
    labl1.grid(row=1, column=1, columnspan=2)
    tk.Entry(frame,textvariable = exsprs, width=18).grid(row = 2,column = 1, columnspan=4)
    tk.Label(frame, text=' ', height=1).grid(row=3, column=1, columnspan=2)
    tk.Button(frame, text='Evaluate', command=calculate, width=15, height=1).grid(row=4, column=1, columnspan=2)
    tk.Button(frame, text='Reset', command=reset, width=15, height=1).grid(row=5, column=1, columnspan=2)
    tk.Button(frame, text='Back', command=main, width=15, height=1).grid(row=6, column=1, columnspan=2)

def about():
    clearFrame()
    tk.Label(frame, text=' ', height=4).grid(row=0, column=1, columnspan=2)
    tk.Label(frame, text='Computing a limit of partial series sum').grid(row=1, column=1, columnspan=2)
    tk.Label(frame, text='Author: Markiyan Kruhliy').grid(row=2, column=1, columnspan=2)
    tk.Button(frame, text='Back', command=main, width=15, height=1).grid(row=3, column=1, columnspan=2)

def main():
    clearFrame()
    tk.Label(frame, text='Series convergence calculator', font=("Arial", 14), height=3).grid(row=0, column=1, columnspan=2)
    tk.Button(frame, text='Evaluate', command=evaluate, width=20, height=2).grid(row=1, column=1, columnspan=2)
    tk.Button(frame, text='About', command=about, width=20, height=2).grid(row=2, column=1, columnspan=2)
    tk.Button(frame, text='Exit', command=sys.exit, width=20, height=2).grid(row=3, column=1, columnspan=2)



if __name__ == '__main__':
    roots = tk.Tk()
    roots.geometry("450x280")
    roots.title('Series Convergence')
    frame = tk.Frame(roots)

    main()

    frame.pack()
    roots.mainloop()
