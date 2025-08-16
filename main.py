import mymath_fun as hel
import math
from PIL import Image

count=10

while count > 0:
    print(count)
    count=count-1

print("Goodbye")
print(hel.sum(4,5))
print(math.sqrt(9))
i=Image.open("img.png")
v=i.rotate(90)
v.save("image.jpg")
v.show()