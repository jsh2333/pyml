from PIL import Image

image = Image.open('./1.jpg')
# resize_image = image.resize((512,512))
resize_image = image.resize((64,64))
resize_image.save('./2.jpg')