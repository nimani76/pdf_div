import glob,os
from PyPDF2 import PdfFileWriter, PdfFileReader
import os, tkinter, tkinter.filedialog, tkinter.messagebox
import sys

def logs(message):
    with open('log.txt', 'a') as f:
        f.write(str(message) +'\n')

def pdf(file):
    try:
        (name, extention) = os.path.splitext(file_name)
        pdf_file_reader = PdfFileReader(file_name)
        page_nums = pdf_file_reader.getNumPages()
        if page_nums == 1:
            return
        for num in range(page_nums):
            file_object = pdf_file_reader.getPage(num)
            pdf_file_name = name + '-' + str(num+1) + '.pdf'
            pdf_file_writer = PdfFileWriter()
            with open(pdf_file_name,'wb') as f:
                pdf_file_writer.addPage(file_object)
                pdf_file_writer.write(f)
            os.remove(file_name)
    except:
        pass

print(sys.argv)
if(sys.argv == None):
    root = tkinter.Tk()
    root.withdraw()
    fTyp = [("","*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    file_name = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
# ファイル選択ダイアログの表示
else:
    file_name = sys.argv

logs(file_name)
# 処理ファイル名の出力
pdf(file_name)