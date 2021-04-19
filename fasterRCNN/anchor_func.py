import numpy as np
#===============================
#anchor generalization function
#===============================
#generalize 9 anchor in a pixel
#anchor ratio: 0.5, 1, 2; anchor scale ratio: 2.
'''
INPUT:
    pixel_x, pixel_y, Original_picture_H, Original_picture_W
OUTPUT:
    9 anchors coordinate and height and width
'''
def unit_anchor_hw_gen(pixel_x, pixel_y, Original_picture_H, Original_picture_W):
    length = np.max(Original_picture_H, Original_picture_W)
    length = length +1 if length//2==0 
    #height and width of anchor while ratio = 1:2, 2:1
    length1 = (length-1) / 2
    length2 = (length-1)

    #height and width of anchor while ratio = 1:1
    length3 = np.ceil((length-1) / 1.414)
    
    #a scale-defined anchor has three kinds of data(h,w)
    anchor9_single_pixel = \
            [[pixel_x, pixel_y, length1, length2], 
            [pixel_x, pixel_y, length2, length1],
            [pixel_x, pixel_y, length3, length3],
            [pixel_x, pixel_y, length1/2, length2/2],
            [pixel_x, pixel_y, length2/2, length1/2],
            [pixel_x, pixel_y, length3/2, length3/2],
            [pixel_x, pixel_y, length1/4, length2/4],
            [pixel_x, pixel_y, length2/4, length1/4],
            [pixel_x, pixel_y, length3/4, length3/4]]
    return anchor9_single_pixel
