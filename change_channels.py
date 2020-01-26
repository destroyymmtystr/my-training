import cv2

input_img_path = 'input/'
output_img_path = 'output/'
img_BGR = cv2.imread(input_img_path + 'girl.jpg')

#順番の入れ替え
img_RGB = img_BGR[:, :, [2, 1, 0]]
cv2.imshow('changed_channels', img_RGB)
cv2.imwrite(output_img_path + 'changed_channels.png', img_RGB)
cv2.waitKey(0)

#numpy配列はimg_BGR[:, :, ◯]に0(B),1(G),2(R),の順でチャネルが並んでいる
#img_BGR[:, :, [0, 1, 2]]