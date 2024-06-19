from janela_tkinter_guitarra import janela

n_strings = 6
n_entries = 20
output = 1 # print to terminal (0) or to file (1)
def main(n_strings, n_entries, output):
    
    janela(n_strings, n_entries, output)

if __name__ == '__main__':
    main(n_strings, n_entries, output)