import os
import cv2

path = "Images"

Images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        Images.append(file_name)

count = len(Images)
frame = cv2.imread(Images[0])
height,width,channels = frame.shape
size = (height,width)
print(size)
out = cv2.VideoWriter("Project.webm",cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)
for i in range(0,count-1):
    cv2.imread(i)
    out.write()