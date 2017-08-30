### [BME595 HW1] Implement 2D convolution
###### Li-Hsin Tseng, PUID: 0029033989

Source code: main.c, conv.py, main.py, README.md.

* Original Images
Two input images of size 1280x720, 1920x1080 <br>

| Original Images |         1280x720          |         1920x1080          |
| --------------- |:-------------------------:| --------------------------:|
|                 | ![](1280x720/1280x720.JPG)|![](1920x1080/1920x1080.JPG)|

* 5 kernels

K1 = [[-1, -1, -1], [0, 0, 0], [1, 1, 1]] <br>
K2 = [[-1,  0,  1], [-1, 0, 1], [-1, 0, 1]] <br>
K3 = [[1,  1,  1], [1, 1, 1], [1, 1, 1]] <br>
K4 = [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]] <br>
K5 = [[-1, -1, 0, 1, 1], [-1, -1, 0, 1, 1], [-1, -1, 0, 1, 1], [-1, -1, 0, 1, 1], [-1, -1, 0, 1, 1]] 

* Kernel 1-3's effects on graph paper

> K1 extracts the horizontal lines of an image <br>
> K2 extracts the vertical lines of an image <br>
> K3 blurres the image

| Graph paper     |              | 
| --------------- |:------------:|
| Original Images |![](graph_paper/graph_paper.JPG)        |
| K1              |![](graph_paper/graph_paper_task3_1.JPG)| 
| K2              |![](graph_paper/graph_paper_task3_2.JPG)| 
| K3              |![](graph_paper/graph_paper_task3_3.JPG)|  

##### Part A
* Task 1

| Task 1          | 1280x720     | 1920x1080  |
| --------------- |:------------:| ----------:|
| K1              |![](1280x720/1280x720_task1_1.JPG)|![](1920x1080/1920x1080_task1_1.JPG)|

* Task 2

| Task 2          | 1280x720     | 1920x1080  |
| --------------- |:------------:| ----------:|
| K4              |![](1280x720/1280x720_task2_1.JPG)|![](1920x1080/1920x1080_task2_1.JPG)|
| K5              |![](1280x720/1280x720_task2_2.JPG)|![](1920x1080/1920x1080_task2_2.JPG)|

* Task 3

| Task 3          | 1280x720     | 1920x1080  |
| --------------- |:------------:| ----------:|
| K1              |![](1280x720/1280x720_task3_1.JPG)|![](1920x1080/1920x1080_task3_1.JPG)|
| K2              |![](1280x720/1280x720_task3_2.JPG)|![](1920x1080/1920x1080_task3_2.JPG)|
| K3              |![](1280x720/1280x720_task3_3.JPG)|![](1920x1080/1920x1080_task3_3.JPG)|

#### Part B
As the value of o_channel goes up, the time of covolution increases approximately two times for o_channel = 2**(i+1) comparing to 2 ** i.
| Part B          | 1280x720     | 1920x1080  |
| --------------- |:------------:| ----------:|
| Time Plot(sec)  |![](1280x720/1280x720_partB.JPG)|![](1920x1080/1920x1080_partB.JPG)|

#### Part C
The number of operations goes up as the kernel size increase.

| Part C           | 1280x720     | 1920x1080  |
| ---------------- |:------------:| ----------:|
| Times Plot(times)|![](1280x720/1280x720_partC.JPG)|![](1920x1080/1920x1080_partC.JPG)| 

#### Part D
Using C to implement the convolution would take a lot less time comparing using python as the language.

| Part D          | 1280x720     | 1920x1080  |
| --------------- |:------------:| ----------:|
| Time Plot(sec)  |![](1280x720/1280x720_partD.JPG)|![](1920x1080/1920x1080_partD.JPG)|


