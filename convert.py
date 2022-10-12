    # pip install pdf2docx

    #------------------------//-----------------------#
    #---------------Convert PDF to docx---------------#
    #------------------------//-----------------------#

from pdf2docx import Converter
pdf_file = input("Insira o nome do arquivo a ser convertido: ")
docx_file = input("Digite o novo nome do arquivo: ")
print("Convertendo, aguarde...")
cv = Converter(pdf_file)
cv.convert(docx_file)
print("Arquivo convertido com sucesso!")
cv.close()