from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
pdf.alias_nb_pages()

df = pd.read_csv("topics1.csv")

page_no = 1  # Initialize page number

for key, row in df.iterrows():
    pdf.add_page()
    # add header
    pdf.set_font(family="Times", style="B", size=26)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)
    for y in range(20, 297, 10):
        pdf.line(10, y, 200, y)

    # Add footer with topic name and game number
    pdf.ln(262)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(200, 200, 200)
    pdf.cell(w=0, h=16, txt=f'{row["Topic"]} - Page {page_no}', align='R', ln=1)
    page_no += 1

    # add footer in all pages
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(274)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(200, 200, 200)
        pdf.cell(w=0, h=16, txt=f'{row["Topic"]} - Page {page_no}', align='R', ln=1)
        page_no += 1

        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

pdf.output("output.pdf")
