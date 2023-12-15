from PIL import Image

img = Image.open('') 
xml_object = img.getxmp()
print(xml_object['xmpmeta']['RDF']['Description']['Rating'])