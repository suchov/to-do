from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path


filepaths = glob.glob("Text+Files/*.txt")

# create a pdf document with multiple pages
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    # read the file - we probably don't need it for the first iteration
    df = pd.read_csv(filepath)
    # adding page
    pdf.add_page()
    # get a file path ...
    filename = Path(filepath).stem
    name = filename.capitalize()
    # style for the pdf page
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=name)

# put all pages created into the pdf
pdf.output("cool.pdf")
