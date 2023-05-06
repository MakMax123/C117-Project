import os
import cv2

path="C:\\Users\\"

images=[]

for filename in os.listdir(path):
    name, ext = os.path.splitext(filename)
    if ext in [".gif",".png",".jpeg",".jpg",".jfif"]:
        file_name= path+"/"+filename
        print(file_name)
        images.append(file_name)

count=len(images)
frame = cv2.imread(images[0])
height,width,channels=frame.shape
size=(width,height)
print(size)
out= cv2.VideoWriter("project.avi",cv2.VideoWriter_fourcc(*"DIVX"),0.8,size)

for i in range(0,count):
    frame = cv2.imread(images[i])
    out.write(frame)


out.release()
print("Done")

        

