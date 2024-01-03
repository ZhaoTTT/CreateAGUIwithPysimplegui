import PySimpleGUIQt as sg

form = sg.FlexForm('My first GUI')

layout = [
    [sg.Text('Enter your name'), sg.InputText()],
    [sg.Text('Enter your country'), sg.InputText()],
    [sg.Text('Enter your phone'), sg.InputText()],
    [sg.Text('Enter your city'), sg.InputText()],
    [sg.OK(), sg.Cancel()]
]

button, values = form.Layout(layout).Read()
# print(values[0])
# print(button)
name = values[0]
country = values[1]
phone = values[2]
city = values[3]

print(f"name {name}, country {country}, phone {phone}. city {city}")