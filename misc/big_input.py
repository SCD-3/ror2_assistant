import tkinter as Tk

SIZE_X = 900
SIZE_Y = 600

def big_input(title: str, deafult: str = "", /) -> str:
    
    root = Tk.Tk()
    root.geometry(f'{SIZE_X}x{SIZE_Y}')
    root.title(title)
    
    textBox = Tk.Text(root, width=SIZE_X, height=SIZE_Y)
    textBox.insert("1.0", deafult)
    textBox.pack()
    
    result: str
    def on_close():
        nonlocal result
        result = textBox.get("1.0", "end-1c") # no idea what are those constants, but i trust stackoverflow
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()
    
    return result


if __name__ == "__main__":
    t = big_input("Please input text", 'bajobajo')
    print(t)