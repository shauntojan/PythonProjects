from  PyPDF2 import PdfWriter

merger = PdfWriter()

for pdf in ["cn m1.pdf","cn m2.pdf","cn m3.pdf","cn m4.pdf","cn m5.pdf"]:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()