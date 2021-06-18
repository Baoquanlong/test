import os
import docx

file = docx.Document(r'/home/baoquanlong/data/Vscode_mypy/英语新闻/1.docx')


print(dir(file))
# for para in file.paragraphs:
#     print(para.text)