import cv2
source='pikachu.jpeg'
destination='resize.jpeg'
scale_percent = 50

src=cv2.imread(source,cv2.IMREAD_UNCHANGED)
# cv2.imshow("title", src)


# Calculate the 50 percent of original dimension
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)


# resize image
output = cv2.resize(src , (width, height))

cv2.imwrite(destination,output)
# cv2.waitKey(0)