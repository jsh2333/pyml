from PIL import Image
 # 이미지 열기
#---------------------------------------
#  이미지 열고 저장
im = Image.open('python.png')
 # 이미지 크기 출력
print(im.size)
 # 이미지 JPG로 저장
im.save('python.jpg')

#---------------------------------------
#  이미지 사이즈 변경,  저장
im = Image.open('python.png')
 # Thumbnail 이미지 생성
size = (64, 64)
im.thumbnail(size)  
im.save('python-thumb.jpg')

#---------------------------------------
#  이미지 잘라내고, 저장
im = Image.open('python.png')
cropImage = im.crop((100, 100, 150, 150))
cropImage.save('python-crop.jpg')

#---------------------------------------
#  이미지 회전하고, 저장
im = Image.open('python.png')
 
# 크기를 600x600 으로
img2 = im.resize((600, 600))
img2.save('python-600.jpg')
 
# 90도 회전
img3 = im.rotate(90)
img3.save('python-rotate.jpg')

#---------------------------------------
#  이미지 필터적용하고, 저장
from PIL import Image, ImageFilter
 
im = Image.open('python.png')
blurImage = im.filter(ImageFilter.BLUR)
 
blurImage.save('python-blur.png')