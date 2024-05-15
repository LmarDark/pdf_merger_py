from tkinter import filedialog
from tkinter import *
import tkinter as tk
from time import sleep as s
import PyPDF2
import os

root = tk.Tk()
root.withdraw()
merger = PyPDF2.PdfMerger()

s(2)
print("Bem vindo ao PDF_Merger!")
s(2)
print("Um projeto desenvolvido por LmarDark")
s(2.5)
print("Por favor, lembre-se de que a pasta '/pdfs' é o local onde você deve colocar os PDFs que deseja mesclar!")
s(5)
input("Está pronto?")
s(0.3)

root.lift()
pdf_folder_selected = filedialog.askdirectory()

archives_amount = os.listdir(pdf_folder_selected)
for archive in archives_amount:
    if ".pdf" in  archive:
        merger.append(f"{pdf_folder_selected}/{archive}")

merger.write("final-pdf.pdf")
input("PDF mesclado com sucesso!")


