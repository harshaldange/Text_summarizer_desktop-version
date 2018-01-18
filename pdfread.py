# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:41:14 2018

@author: ADMIN
"""

import PyPDF2 as pypdf

file=pypdf.PdfFileReader("C:/Users/ADMIN/Downloads/npl.pdf")
text=""
pages=file.getNumPages()
for x in range(0,pages):
    page=file.getPage(x)
    text+=page.extractText()
   
print(text) 
