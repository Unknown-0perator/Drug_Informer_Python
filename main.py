from tkinter import *
import requests

FONT_PRIMAY = ('Arial', 10, 'bold')
FONT_SECONDARY = ('Arial', 8, 'bold')
BACKGROUND_COLOR = '#00ADB5'
FONT_SECONDARY_COLOR = '#EEEEEE'


def get_drug_info():
    user_input = drug_name_entry.get()
    response = requests.get(url=f'https://api.fda.gov/drug/drugsfda.json?search=openfda.brand_name:{user_input}')
    response.raise_for_status()
    data = response.json()
    brand_name = data['results'][0]['openfda']['brand_name']
    medicine_name_dec.config(text=brand_name)
    generic_name = data['results'][0]['openfda']['generic_name']
    generic_name_dec.config(text=generic_name)
    manufacturer_name = data['results'][0]['openfda']['manufacturer_name']
    manufacturer_name_dec.config(text=manufacturer_name)
    substance_name = data['results'][0]['openfda']['substance_name']
    substance_name_dec.config(text=substance_name)
    product_type = data['results'][0]['openfda']['product_type']
    medicine_type_dec.config(text=product_type)
    product_ndc = data['results'][0]['openfda']['product_ndc']
    medicine_indication_dec.config(text=product_ndc)
    route = data['results'][0]['openfda']['route']
    dosage_text_dec.config(text=route)


# --------------- UI ----------------------
window = Tk()
window.title('Drug Information')
window.config(width=800, height=600, padx=50, pady=50, bg=BACKGROUND_COLOR)
logo_image = PhotoImage(file='logo.png')
logo = Canvas(width=200, height=200)
logo.create_image(100, 100, image=logo_image)
logo.config(bg=BACKGROUND_COLOR, highlightthickness=0)
logo.grid(row=0, column=0)
drug_name = Label(text='Drug Name: ', font=FONT_PRIMAY, bg=BACKGROUND_COLOR)
drug_name.grid(row=0, column=1)
drug_name_entry = Entry()
drug_name_entry.grid(row=0, column=2)
search_btn = Button(text='Search', command=get_drug_info)
search_btn.grid(row=0, column=3)
medicine_name = Label(text='Medicine name', font=FONT_PRIMAY, bg=BACKGROUND_COLOR)
medicine_name.grid(row=1, column=0)
dosage_text = Label(text='Dosage Text', font=FONT_PRIMAY, bg=BACKGROUND_COLOR)
dosage_text.grid(row=2, column=0)
medicine_indication = Label(text='Medicine Indication', font=FONT_PRIMAY, bg=BACKGROUND_COLOR)
medicine_indication.grid(row=3, column=0)
manufacturer_name = Label(text='Manufacturer Name', font=FONT_PRIMAY, bg=BACKGROUND_COLOR)
manufacturer_name.grid(row=4, column=0)
generic_name = Label(text='Generic Name', font=FONT_PRIMAY, bg=BACKGROUND_COLOR)
generic_name.grid(row=1, column=2)
substance_name = Label(text='Substance Name', font=FONT_PRIMAY, bg=BACKGROUND_COLOR)
substance_name.grid(row=2, column=2)
medicine_type = Label(text='Medicine Type', font=FONT_PRIMAY, bg=BACKGROUND_COLOR)
medicine_type.grid(row=3, column=2)

medicine_name_dec = Label(text='', font=FONT_SECONDARY, bg=BACKGROUND_COLOR, fg=FONT_SECONDARY_COLOR)
medicine_name_dec.grid(row=1, column=1)
dosage_text_dec = Label(text='', font=FONT_SECONDARY, bg=BACKGROUND_COLOR, fg=FONT_SECONDARY_COLOR)
dosage_text_dec.grid(row=2, column=1)
medicine_indication_dec = Label(text='', font=FONT_SECONDARY, bg=BACKGROUND_COLOR, fg=FONT_SECONDARY_COLOR)
medicine_indication_dec.grid(row=3, column=1)
manufacturer_name_dec = Label(text='', font=FONT_SECONDARY, bg=BACKGROUND_COLOR, fg=FONT_SECONDARY_COLOR)
manufacturer_name_dec.grid(row=4, column=1)
generic_name_dec = Label(text='', font=FONT_SECONDARY, bg=BACKGROUND_COLOR, fg=FONT_SECONDARY_COLOR)
generic_name_dec.grid(row=1, column=3)
substance_name_dec = Label(text='', font=FONT_SECONDARY, bg=BACKGROUND_COLOR, fg=FONT_SECONDARY_COLOR)
substance_name_dec.grid(row=2, column=3)
medicine_type_dec = Label(text='', font=FONT_SECONDARY, bg=BACKGROUND_COLOR, fg=FONT_SECONDARY_COLOR)
medicine_type_dec.grid(row=3, column=3)
disclaimer = Label(text='Only use Brand Name with correct spelling\n\nread README', bg=BACKGROUND_COLOR, fg='red')
disclaimer.grid(row=5, column=0, columnspan=5)
window.mainloop()
