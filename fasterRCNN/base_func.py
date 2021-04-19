import numpy as np
#==========================
#Convolutional Function
#=========================
#calculate the convolution of picture and kernel
#subfunction: get_size, Unit_conv
'''
INPUT:
    single picture,height h, width w, 2-dimension
    kernel, 3x3 or 5x5, 2-dimension
    stride, 0 or 3 or 5(these would be better)
    padding, bool type, the size of OUTPUT feature map woud be as the same as INPUT if padding=True
OUTPUT:
    Conv_matrix, feature map, 2-dimension
'''
def Conv(picture=[[],[],[]], kernel=[[],[],[]], stride=0, padding=True):
    kernel_size = get_size(kernal)
    if padding:
        pad_size = (kernel_size-1)/2
    else:
        pad_size = 0
        
        h,w = getsize(picture)#receive the hight and width of 2D_matrix
        padding_matrix = np.zeros(h+2*pad_size,w+2*pad_size)#padding original picture with 0, maybe no padding but do so
        for i in range(h-2*pad_size):
            for j in range(w-2*pad_size):
                padding_matrix[i+pad_size,j+pad_size] = picture[i,j]

        Conv_matrix = np.zeros(h+2*pad_size-(kernel_size+1),w+2*pad_size-(kernel_size+1))
        for i in range(h+2*pad_size-(kernel_size+1)):
            for j in range(w+2*pad_size-(kernel_size+1)):
                2D_matrix = picture[i+stride:i+stride+kernel_size,j+stride:j+stride+kernel_size]
                Conv_matrix[i,j] = Unit_conv(2D_matrix, kernel)
        return Conv_matrix
#calculate the convolution of single matrix and kernel
def Unit_conv(2D_matrix, kernel):
    m1,m2 = get_size(2D_matrix)
    k1,k2 = get_size(kernel)
    if m1==m2 && k1==k2 && m1==k1:
        result = 0
        for i,j in range(m1):
            result += 2D_matrix[i,j]*kernel[i,j]
        return result
    else:
        return "The size of matrix to conv does not match the kernel"


#=======================
#ReLU function(Rectified Linear Unit)
#=======================
#turn the negative number in feature map to zero
#subfunction: get_size
'''
INPUT:
    feature_map, height H, width W, 2-dimension
OUTPUT:
    Result, 2-dimension
'''
def ReLU(feature_map):
    H,W = get_size(feature_map)
    Result = np.zeros(H,W)
    for x in range(H):
        for y in range(W):
            Result[x,y] = feature_map[x,y] if feature_map[x,y] >= 0
    return Result


#=====================
#Pooling function
#=====================
#do statistic calcuation in local feature map
#subfunction: get_size
#attention: stride could be 1 or as the same as size, when stride=size, pooling could scale down the original picture
'''
INPUT:
    feature_map, heigh H, width W, 2-dimension
    size, pooling the matrix (size x size)
    stride, the moving step
OUTPUT:
    result, feature map, 2-dimension
'''
def Pooling(feature_map, 'max', size=3, stride=1):
    H,W = get_size(feature_map)

    if stride == 1:
        res_H = H - (size - stride)
        res_W = W - (size - stride)
        result = np.zeros(res_H, res_W)
        for x in range(res_H):
            for y in range(res_W):
                result[x,y] = np.max(feature_map[x:x+size, y:y+size])
    if stride == size:
        res_H = H / size
        res_W = W / size
        result = np.zeros(res_H, res_W)
        for x in range(res_H):
            for y in range(res_W):
                result[x,y] = np.max(feature_map[x*stride:x*stride+size, y*stride:y*stride+size])
    return result

#====================
#RoI Pooling function
#====================
#Max Pooling the region of Interest, only work for fast R-CNN
'''
INPUT:
    RoI, Region of Interest OR the provisional Proposal, height H, width W, 2-dimension
    target_size, the size of pooling region
OUTPUT:
    res, feature map, height target_size, width target_size, 2-dimension

DESCRIPTION:
    It's difficult to understand these codes. Take an example in 1-dimension.
    H = 20, target_size = 7, then Pooling region subsequently would be 3,3,3, 3,3,3, 2
    How could we get pool_region_H=3? 20//7=2, 2+1=3, that's it!
    How could we get H_final=2? 3*7-20=2, that's it!

    i from 0 to 5, result[i] = feature_map[i*3:(i+1)*3]
    result[6] = feature_map[(5+1)*3, 20]
'''
def RoIPooling(RoI, target_size=7):
    H,W = get_size(RoI)
    
    pool_region_H = H // target_size + 1
    H_final = pool_region_H - (pool_region_H * target_size - H)
    pool_region_W = W // target_size + 1
    W_final = pool_region_W - (pool_region_W * target_size - W)
    
    res = np.zeros(target_size)

    for i,j in range(target_size-1):
        res[i,j] = np.max(RoI[i*pool_region_H:(i+1)*pool_region_H), j*pool_region_W:(j+1)*pool_region_W)])
    res[target_size-1,taget_size-1] = np.max(RoI[(target_size-1)*pool_region_H):H, (target_size-1)*pool_region_W:W])

    return res
