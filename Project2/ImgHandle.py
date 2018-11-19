from PIL import Image, ImageTk

def tk_image(path):
 img = Image.open(path)
 width, height = img.size
 img = img.resize((width * 2, height * 2))
 storeobj = ImageTk.PhotoImage(img)
 return storeobj