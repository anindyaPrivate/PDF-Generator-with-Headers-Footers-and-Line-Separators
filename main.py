from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics1.csv")


for key, row in df.iterrows():
    pdf.add_page()
    # add header
    pdf.set_font(family="Times", style="B", size=26)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)
    pdf.line(10, 20, 200, 20)

    # Add footer
    pdf.ln(262)
    pdf.set_font(family="Times", style="I", size=16)
    pdf.set_text_color(200, 200, 200)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='R', ln=1)
    pdf.line(10, 287, 200, 287)

    # add footer in all pages
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(274)
        pdf.set_font(family="Times", style="I", size=16)
        pdf.set_text_color(200, 200, 200)
        pdf.cell(w=0, h=12, txt=row['Topic'], align='R', ln=1)
        pdf.line(10, 287, 200, 287)

pdf.output("output.pdf")
