import os
from PIL import Image

image_filename = os.path.join(os.path.join('images/70/7525.jpg'))
img=Image.open(image_filename)  
img.save('images/70/7525.jpg')