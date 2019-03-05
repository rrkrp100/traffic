from PIL import Image
import pytesseract
import glob

img_list = glob.glob("*.jpeg")

for img in img_list:
	im = Image.open(img)

	text = pytesseract.image_to_string(im, lang = 'eng')
	
	
	print(text,'\n')
	
