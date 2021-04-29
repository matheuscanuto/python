#importing the library that we will use
#commands to download: pip intall openpyxl
from openpyxl import Workbook
wb = Workbook
spreadsheet = wb.worksheets[0] 

spreadsheet['A1']= "sport"  #will insert in A1 the word "sports" and so on
spreadsheet['B1']= "car"

wb.save("MeuArquivo.xlsx") #will save in the same folder as the python file, you can put any name, as long as it is .xlsx at the end

