// Credit: Li-Hsin Tseng
// [int] c_conv(in_channel, o_channel, kernel_size, stride)
#include <stdio.h>
#include <time.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int main(void){
	time_t start, end;
	int t, o_channel;
  	double elapsed_secs;
	int kernel_size = 3;
	int stride = 1;
	int x, i, j, m, n, c;
	int channel = 3;
	int row = 1080; //720;
	int col = 1920; //1280;
	int res_row = (int)(row - kernel_size) / stride + 1;
	int res_col = (int)(col - kernel_size) / stride + 1;
	double tmp;
	//int input_image[channel][row][col];
	int K[kernel_size][kernel_size];
  	
  	/*
  	for(x = 0; x < channel; x++){
		for(i = 0; i < row; i++){
			for(j = 0; j < col; j++){
				input_image[x][i][j] = ((double) rand() / (RAND_MAX));
			}
		}
	}*/
	
	for(t = 0; t < 11; t++){
		o_channel = pow(2, t);
		start = clock();
		for(m = 0; m < kernel_size; m++){
    		for(n = 0; n < kernel_size; n++){
    			K[m][n] = ((double) rand() / (RAND_MAX));
    		}
    	}
    
    	for(x = 0; x < o_channel; x++){
    		for(i = 0; i < res_row; i += stride){
    			for(j = 0; j < res_col; j += stride){
    				for(c = 0; c < channel; c++){
    					for(m = 0; m < kernel_size; m++){
    						for(n = 0; n < kernel_size; n++){
    							tmp = ((double) rand() / (RAND_MAX)) * K[m][n];
    							//tmp = input_image[c][i * stride + m][j * stride + n] * K[m][n];
    						}
    					}
    				}
    			}
    		}
    
    	}
		end = clock();
		elapsed_secs = (double)(end - start) / CLOCKS_PER_SEC;
		printf("t = %d, time = %lf.\n", t, elapsed_secs);
	}
	
	return 0;
}




