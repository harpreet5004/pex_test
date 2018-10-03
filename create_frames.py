import cv2
import os

'''
Two classes:
1. Indoor photographs(e.g. Bedroom, House, Hotel, Classroom, Office)
2. Outdoor photogr(e.g. Outdoor Recreation, Landscape, Mountain, Beach)
'''

def readVideoToCreateFrames(file_path):
	global count
	i = 0
	vidcap = cv2.VideoCapture(file_path)
	success,image = vidcap.read()
	while success:
		i+=1
		success,image = vidcap.read()
		if(i >400):
			cv2.imwrite("images/frame_%d.jpg" % count, image) # save frame as JPEG file
			#success,image = vidcap.read()
			count = count+1
			if(i > 600):
				break
	print(count)

dir_path = os.path.dirname(os.path.realpath(__file__))
#datadir = dir_path+'/input/indoor_data/videos'
datadir = dir_path+'/input/outdoor_data/videos'
all_files = os.listdir(datadir)
count = 0
for file in all_files:
	readVideoToCreateFrames(datadir +'/'+ file)