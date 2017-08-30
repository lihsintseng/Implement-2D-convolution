# Credit: Li-Hsin Tseng
import torch


class Conv2D(object):
	def __init__(self, in_channel, o_channel, kernel_size, stride, mode):
		self.in_channel = in_channel
		self.o_channel = o_channel
		self.kernel_size = kernel_size
		self.mode =	mode
		self.stride	= stride
		self.K = []
		self.K1 = [[-1, -1, -1], [0, 0, 0], [1, 1, 1]] 
		self.K2 = [[-1,  0,  1], [-1, 0, 1], [-1, 0, 1]] 
		self.K3 = [[1,  1,  1], [1, 1, 1], [1, 1, 1]]
		self.K4 = [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
		self.K5 = [[-1, -1, 0, 1, 1], [-1, -1, 0, 1, 1], [-1, -1, 0, 1, 1], [-1, -1, 0, 1, 1], [-1, -1, 0, 1, 1]] 


	def forward(self, input_image):
		# outputs: [int (number of operation), 3D FloatTensor (output feature map)]
		channel, row, col = input_image.size()
		res_row, res_col = int((row - self.kernel_size) / self.stride) + 1, int((col - self.kernel_size) / self.stride) + 1
		res = []
		input_image = sum(input_image)

		if self.mode == 'rand':
			self.K = torch.rand(self.kernel_size, self.kernel_size)
		
		for o_channel_cnt in range(self.o_channel):
			tmp = torch.zeros(res_row, res_col)
			for i in range(res_row):
				for j in range(res_col):
					if self.mode == 'known':
						tmp[i][j] = torch.sum(torch.mul(input_image[i * self.stride: i * self.stride + self.kernel_size, j * self.stride: j * self.stride + self.kernel_size], torch.Tensor(self.K[o_channel_cnt])))
					else:
						tmp[i][j] = torch.sum(torch.mul(input_image[i * self.stride: i * self.stride + self.kernel_size, j * self.stride: j * self.stride + self.kernel_size], self.K))
						'''
						for m in range(self.kernel_size):
							for n in range(self.kernel_size):
								tmp[c][i][j] += input_image[c][(i - 1) * self.stride + m][(j - 1) * self.stride + n] * self.K[m][n]
						'''
			tmp = tmp.unsqueeze(0)
			tmp = (tmp - tmp.min()) / (tmp.max() - tmp.min())
			res.append(tmp)
			#print(self.o_channel*res_row*res_col*channel*self.kernel_size*self.kernel_size*2)
		# number of operation is multiplication and addition both
		return self.o_channel*res_row*res_col*channel*self.kernel_size*self.kernel_size*2, res