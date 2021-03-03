import tkinter as tk
 
window = tk.Tk() # Это инициализация окна
hello = tk.Label(
    text = 'Проверка окна раp раз гав гав',
    fg = 'white',
    bg = '#af2b1e',
    width = 50,
    height = 25
) #это виджет

textbox = tk.Entry(
    width = 50
)

button1 = tk.Button(
    text = 'Привет мир',
    fg = 'purple',
    bg = 'white',
    width = 50,
    height = 5
    )


hello.pack() # этот метод пакует виджет в окно
textbox.pack()
button1.pack()

name = textbox.get()
print(name)

window.mainloop()