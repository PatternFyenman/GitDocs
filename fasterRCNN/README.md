
*base_func.py*

	**Convloution function**
	===========
	Conv(picture, kernel, stride, padding) => 2-d Conv_matrix
	===========
	input a picture and a kernel and output a feature map

	**ReLU function**
	==========
 	ReLU(feature_map) => 2-d Result
	==========
	input a feature map and output a rectified feature map
	
	**Pooling funciton**
	==========
	Pooling(feature_map, size, stride) => 2-d result 
	==========
	input a feature map and output a pooled feature map that scaled down 

	**RoI Pooling function**
	==========
	RoIPooling(RoI, target_size=7) => 2-d result
	==========
	input a Region of Interest in a feature map and output a feature map in a defined size

*resize.py*

	**resize functio**
	==========
	resize(Original_picture, target_H, target_W, keep_ratio) => 2-d Resized_picture
	==========
	input a original picture and output a resized picture

*anchor_func.py*
	**get 9 anchors' info for one pixel**
	==========
	unit_anchor_gen(pixel_x,pixel_y,Original_picture_H, Original_picture_W) => 2-d 9anchors' coordinate and height and width
	==========
	

*full_connected.py*
	**FC**
	==========
	FC(feature map, layer_number, activateType, result vector)
	==========
	input a feature map and ground truth categories, output the result from loss calculation 

	**Backword Fully Connected Func**
	==========
	BackFC(loss_vector, all_init_weight, all_layers_value,lr)
	2 fully connected layer, feature map as input layer and classified vector as output layer

