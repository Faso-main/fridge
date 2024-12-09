from tkinter import *

class Fridge:
    def __init__(self):
        self.products = []

    def add_product(self, product, shelf, weight):
        self.products.append((product, shelf, weight))

    def remove_product(self, product):
        for item in self.products:
            if item[0] == product:
                self.products.remove(item)
                return True
        return False

    def get_products(self):
        return self.products


def error(text, color):
    message.config(text=text, fg=color)
    window.after(1000, clear_message)

def clear_message():
    message.config(text="")

def add_product():
    if checkbox_state.get():
        input_data = txt.get()
        product, shelf, weight = map(str.strip, input_data.split(","))
        fridge.add_product(product, shelf, weight)
        update_product_list()
        txt.delete(0, END)
    if not checkbox_state.get():
        error("Холодильник закрыт!", "red")
        return

def remove_product():
    if checkbox_state.get():
        product = txt.get().strip()
        if fridge.remove_product(product):
            update_product_list()
            txt.delete(0, END)
    if not checkbox_state.get():
        error("Холодильник закрыт!", "red")
        return

def update_product_list():
    listbox.delete(0, END)
    for product, shelf, weight in fridge.get_products():
        listbox.insert(END, f"Продукт: {product}, Полка: {shelf}, Вес: {weight}")


window = Tk()
window.title("Холодильник")
window.geometry('800x700')
font = ("Calibri", 12, "bold")

fridge = Fridge()

txt = Entry(window, width=30)
txt.place(x=300, y=20)

btn = Button(window, text="Положить", font=font, command=add_product)
btn.place(x=500, y=10)

btn2 = Button(window, text="Забрать", font=font, command=remove_product)
btn2.place(x=600, y=10)

listbox = Listbox(window, width=60, height=30)
listbox.place(x=300, y=50)

message = Label(window, text="", font=font)
message.place(x=300, y=400)

checkbox_state = BooleanVar()
checkbox_state.set(True)
checkbox = Checkbutton(window, text='Открыть/Закрыть', font=font, var=checkbox_state)
checkbox.place(x=50, y=10)

i = PhotoImage(file="fridge/fridge.gif")
ilabel = Label(window, image=i)
ilabel.place(x=-120, y=50)

etc = Label(window, text="Положить в холодильник: Продукт, Полка, Вес\n Забрать из холодильника: Продукт", font=font)
etc.place(x=300, y=550)

window.mainloop()
