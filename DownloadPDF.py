#Download PDF books from Internet

#pip install urllib

import urllib.request
url=input("Enter Link to Download PDF : ")
Name=input("Enter a Name for the PDF File : ")
FilleName = Name+".pdf"
urllib.request.urlretrieve(url, FileName)