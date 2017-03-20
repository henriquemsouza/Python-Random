from fpdf import FPDF  #pip install fpdf
from PIL import Image   #pip install Pillow
import glob
import os


# set here 
image_directory = 'C:/User/Documents/Screenshots'
extensions = ('*.jpg','*.png','*.gif')
# set 0 if you want to fit pdf to image
# unit : pt
margin = 10

imagelist=[]
for ext in extensions:
    imagelist.extend(glob.glob(os.path.join(image_directory,ext)))

for imagePath in imagelist:
    cover = Image.open(imagePath)
    width, height = cover.size

pdf = FPDF(unit="pt", format=[width + 2*margin, height + 2*margin])
pdf.add_page()

pdf.image(imagePath, margin, margin)

destination = os.path.splitext(imagePath)[0]
pdf.output(destination + ".pdf", "F")
