import PySimpleGUI as sg


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


sg.theme("Black")


label1 = sg.Text("Enter feet:")
input1 = sg.Input(key="feets")


label2 = sg.Text("Enter inches:")
input2 = sg.Input(key="inches")

convert_button = sg.Button("Convert")
output_lable = sg.Text(key="output")
exit_button = sg.Button("Exit")


window = sg.Window("Conventor",
                   layout=[[label1, input1], [label2, input2],
                           [convert_button, output_lable, exit_button]])

while True:
    event, values = window.read()
    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
    try:
        feets = float(values["feets"])
        inches = float(values["inches"])
        result = convert(feets, inches)
        window["output"].update(value=f"{result} m", text_color="white")
    except ValueError:
        sg.popup("Please provide two numbers.", font=("Helvetica", 20))

window.close()
