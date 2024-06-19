import tkinter as tk
from tkinter import ttk
from gerador_tab_cifraclub import printTab, next, next_mod



def submit(entrys, n_strings, output):
    print(entrys[0][0].get())
    
    notas = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[]}
    for j in range(len(entrys[0])):
        maiorq9=[]
        for i in range(len(entrys)):
            notemquestao = entrys[i][j].get()
            if notemquestao=='':
               notas[i].append(-1)
            elif notemquestao=='X' or notemquestao=='x':
                notas[i].append(-2)
            else:
               if int(notemquestao)>9:
                   maiorq9.append(i)
               notas[i].append(notemquestao)
        next_mod(notas, maiorq9)
        next(notas)
               
    
    notas =  {'e':notas[0], 'b':notas[1], 'g':notas[2], 'd':notas[3], 'a':notas[4], 'E':notas[5], 'B':notas[6], 'G':notas[7]}
    printTab(notas, n_strings, output)
# Create the main window


# Function to enforce numerical input
def validate(P):
    if str.isdigit(P) or P == "" or P=='X' or P=='x':
        return True
    else:
        return False

def janela(n_strings, n_entries, output):
    root = tk.Tk()
    root.title(f"6x{n_entries} Grid of Number Inputs")

    # Register the validation function
    vcmd = (root.register(validate), '%P')

    # Create a frame to hold the grid
    frame = ttk.Frame(root)
    frame.grid(row=0, column=0, padx=10, pady=10)

    # Create 6 rows and 40 columns of Entry widgets
    entrys = []
    for i in range(n_strings):
        entrys.append([])
        for j in range(n_entries):
            entrys[i].append(ttk.Entry(frame, validate='key', validatecommand=vcmd, width=5))
            entrys[i][-1].grid(row=i, column=j, padx=2, pady=2)
    submit_button = ttk.Button(root, text="Submit", command=lambda:submit(entrys, n_strings, output))
    submit_button.grid(row=1, column=0, pady=10)
    # Run the application
    root.mainloop()