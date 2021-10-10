from PIL import Image

image=Image.open(r'path\to\file.file_format')
size=(int(150),int(100))#150=width in px          100=width in px         must be in circular bracket
image=image.resize(size,Image.ANTIALIAS)
image.save(r'path\to_save\file.file_format')
