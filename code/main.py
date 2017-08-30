# Credit: Li-Hsin Tseng
from PIL import Image
from conv import Conv2D
from torchvision import transforms
import matplotlib.pyplot as plt
import torch
import time

base = '/Users/lihsintseng/Desktop/BME595HW1/'

def known_helper(conv2d, img, name):
	if conv2d.mode == 'known':
		if conv2d.kernel_size == 3:
			for i in range(conv2d.o_channel):
				if i == 0:
					conv2d.K.append(conv2d.K1)
				elif i == 1:
					conv2d.K.append(conv2d.K2)
				elif i == 2:
					conv2d.K.append(conv2d.K3)
			cnt, new_img = conv2d.forward(img)
		elif conv2d.kernel_size == 5:
			for i in range(conv2d.o_channel):
				if i == 0:
					conv2d.K.append(conv2d.K4)
				elif i == 1:
					conv2d.K.append(conv2d.K5)
			cnt, new_img = conv2d.forward(img)
		for i in range(len(new_img)):
				trans_to_PIL = transforms.ToPILImage()
				pil_img = trans_to_PIL(new_img[i])
				pil_img.save(base + name + '_' + str(i+1) + '.JPG')
	
img2 = Image.open(base + '1920x1080.JPG')
img1 = Image.open(base + '/1280x720.JPG')

trans_to_Tensor = transforms.ToTensor()
img = trans_to_Tensor(img1)

'''
Part A
Initialize Conv2D in main.py (conv2d = Conv2D(*args)) for one of the task.
Call conv2d.forward() with your input image. The forward() function must return output [int, 3D FloatTensor].
Save each channel of output tensor separately as a grayscale image in your main repository.
Repeat 2-4 for all the three tasks.
'''
# Conv2d(self, in_channel, o_channel, kernel_size, stride, mode)
print('partA')
task1_conv2d = Conv2D(3, 1, 3, 1, 'known') # K1
known_helper(task1_conv2d, img, 'task1')
task2_conv2d = Conv2D(3, 2, 5, 1, 'known') # K4, K5
known_helper(task2_conv2d, img, 'task2')
task3_conv2d = Conv2D(3, 3, 3, 2, 'known') # K1, K2, K3
known_helper(task3_conv2d, img, 'task3')

'''
Part B
Initialize Conv2D using values of Task 1 and set o_channel to 2^i (i = 0, 1, …, 10) and mode=’rand’.
Plot the time taken for performing each forward() pass as a function of i.
'''
print('partB')
b_time = []

for i in range(8, 11):
	o_channel = 2 ** i
	task1_conv2d = Conv2D(3, o_channel, 3, 1, 'rand')
	start_time = time.time()
	cnt, new_img = task1_conv2d.forward(img)
	total_time = time.time() - start_time
	b_time.append(total_time)
	print(i, total_time)

plt.plot([0] + b_time, marker='o', linestyle='--', color='b')
plt.xlabel('value of i')
plt.ylabel('time (sec)')
plt.savefig('/Users/lihsintseng/Desktop/BME595HW1/partB.JPEG')

'''
Part C
Initialize Conv2D using values of Task 2 with kernel_size=3, 5, …, 11 and mode=’rand’.
Plot number of operations (int returned by forward()) used to perform convolution as a function of kernel_size.
'''
print('partC')
c_cnt = []
for i in range(5):
	k_size = (i + 1) * 2 + 1
	task2_conv2d = Conv2D(3, 2, k_size, 1, 'rand')
	cnt, new_img = task2_conv2d.forward(img)
	c_cnt.append(cnt)
	print(i, cnt)

plt.plot([(i + 1) * 2 + 1 for i in range(5)], c_cnt, marker='o', linestyle='--', color='b')
plt.xlabel('value of kernel_size')
plt.ylabel('count (times)')
plt.savefig('/Users/lihsintseng/Desktop/BME595HW1/partC.JPEG')


