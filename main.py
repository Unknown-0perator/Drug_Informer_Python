from tkinter import *
import requests


def get_drug_info():
    user_input = drug_name_entry.get()
    response = requests.get(url=f'https://api.fda.gov/drug/drugsfda.json?search=openfda.brand_name:{user_input}')
    response.raise_for_status()
    data = response.json()
    brand_name = data['results'][0]['openfda']['brand_name']
    medicine_name_dec.config(text=brand_name)
    print(data['results'])


# --------------- UI ----------------------
window = Tk()
window.title('Drug Information')
window.config(width=800, height=600, padx=50, pady=50)
logo_image = PhotoImage(file='logo.png')
logo = Canvas(width=200, height=200)
logo.create_image(100, 100, image=logo_image)
logo.grid(row=0, column=0)
drug_name = Label(text='Drug Name: ')
drug_name.grid(row=0, column=1)
drug_name_entry = Entry()
drug_name_entry.grid(row=0, column=2)
search_btn = Button(text='Search', command=get_drug_info)
search_btn.grid(row=0, column=3)
medicine_name = Label(text='Medicine name')
medicine_name.grid(row=1, column=0)
dosage_text = Label(text='Dosage Text')
dosage_text.grid(row=2, column=0)
medicine_indication = Label(text='Medicine Indication')
medicine_indication.grid(row=3, column=0)
manufacturer_name = Label(text='Manufacturer Name')
manufacturer_name.grid(row=4, column=0)
generic_name = Label(text='Generic Name')
generic_name.grid(row=1, column=2)
substance_name = Label(text='Substance Name')
substance_name.grid(row=2, column=2)
medicine_type = Label(text='Medicine Type')
medicine_type.grid(row=3, column=2)

medicine_name_dec = Label(text='Medicine name')
medicine_name_dec.grid(row=1, column=1)
dosage_text_dec = Label(text='Dosage Text')
dosage_text_dec.grid(row=2, column=1)
medicine_indication_dec = Label(text='Medicine Indication')
medicine_indication_dec.grid(row=3, column=1)
manufacturer_name_dec = Label(text='Manufacturer Name')
manufacturer_name_dec.grid(row=4, column=1)
generic_name_dec = Label(text='Generic Name')
generic_name_dec.grid(row=1, column=3)
substance_name_dec = Label(text='Substance Name')
substance_name_dec.grid(row=2, column=3)
medicine_type_dec = Label(text='Medicine Type')
medicine_type_dec.grid(row=3, column=3)

window.mainloop()
