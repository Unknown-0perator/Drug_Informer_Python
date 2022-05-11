import tkinter

window = tkinter.Tk()
window.title('Drug Information')
window.config(width=800, height=600)
logo_image = tkinter.PhotoImage(file='logo.png')
logo = tkinter.Canvas(width=200, height=200)
logo.create_image(100, 100, image=logo_image)
logo.pack()
drug_name = tkinter.Label(text='Drug Name: ')
drug_name.pack()
drug_name_entry = tkinter.Entry()
drug_name_entry.pack()
search_btn = tkinter.Button(text='Search')
search_btn.pack()

window.mainloop()