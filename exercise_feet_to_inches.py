import PySimpleGUI as sg

label1 = sg.Text("Enter feet:")
input1 = sg.Input(key="feets")


label2 = sg.Text("Enter inches:")
input2 = sg.Input(key="inches")

convert_button = sg.Button("Convert")
output_lable = sg.Text(key="output")


window = sg.Window("Conventor",
                   layout=[[label1, input1], [label2, input2],
                           [convert_button, output_lable]])

while True:
    event, values = window.read()
    feets = float(values["feets"])
    inches = float(values["inches"])

    window["output"].update(value=feets * 0.3048 + inches * 0.0254)

window.close()
