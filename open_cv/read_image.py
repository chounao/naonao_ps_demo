import cv2
import matplotlib.pyplot as plt
import numpy as np

# 读取图像
image_path ="C:/Users/86185/Desktop/周超杰/mimt/open_cv/微信图片_20240326154400.jpg"
# image_path ="open_cv/微信图片_20240326154400.jpg"
image = cv2.imread(image_path)

# 将图像转换为灰度图像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 显示原始图像
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

# 显示灰度图像
plt.subplot(1, 2, 2)
plt.title('Gray Image')
plt.imshow(gray_image, cmap='gray')
plt.axis('off')
plt.show()
# captcha_image = cv2.imread(image_path)
#
# # 显示验证码图片
# plt.imshow(cv2.cvtColor(captcha_image, cv2.COLOR_BGR2RGB))
# plt.axis('off')
# plt.show()