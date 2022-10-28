#Generate Barcode using Python
#pip install python-barcode

import barcode
from barcode.write import ImageWrite

#Define content of the barcode as a string
number = input("Enter the code to generate barcode : ")

#Get the required barcode format
barcode_format = barcode.get_barcode_class('upc')

#Generate barcode and render as image
my_barcode = barcode_format(number, write=ImageWrite())

#Save barcode as PNG
my_barcode.save("generated_barcode")

#number Output
#Images Output

from PIL Image #to open the barcode and show
Image.open('generated_barcode.png')