import PySimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select files to compress")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")


label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
output_lable = sg.Text(key="output")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button, output_lable]])

while True:
    event, values = window.read()
    print(event, values)
    filepath = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepath, folder)
    window["output"].update(value="Compression completed!")

window.close()
