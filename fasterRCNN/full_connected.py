import numpy as np
#=======
#fully connected network function
"""
Input a feature map and calculate nonlinear activation 
output the difference between activation and real result
in default, the layers has same size

INPUT:
    feature map, 2-d, height H, width W
    layer number, the size of fully connected network, not included the output layer
    activateType, string, "Sigmoid", "tanh", ...
    result vector, 1-d, 
OUTPUT:
    result weight, 2-d, the weight of different layers, the weights of each layer to be a colmum in result matrix
"""
#=======

def FC(feature_map, layer_number=2, activateType='sigmoid', result_vector):
    H,W = get_size(feature_map)
    res_size = get_size(result_vector)

    init_layer = np.flatten(feature_map)
    
    #init_weight, 2-d
    init_weight = get_init_weight('random', size)
    init_bias = get_init_bias('random',size)
            
    
    linearOut1 = np.dot(init_weight, init_layer) + init_bias
    layer1 = activate_func(linearOut1, activateType)

    liearOut2 = np.dot(init_weight, layer1) + init_bias
    layer2 = activate_func(liearOut2, activateType)

    outputlayer1 = np.dot(get_init_weight('random', [H*W,res_size]), layer2) + init_bias

    diff_res = MSE(outputlayer1 - result_vector)
    return diff_res

#=======
#Backward Propagation function
"""
INPUT:
    loss_vector, 1-d, the difference of output of FC and the ground truth, output-Truth_layer
    all_init_weight, 3-d, consist of three layers' weight
    all_layers_value, 2-d(5* H*W), consist of 5 vector, each vector present the value in each layer
    learning rate
OUTPUT:
    the weight after training, 3-d, consist of three layers' weight
"""
#=======
def BackFC(loss_vector, all_init_weight, all_layers_value, lr):
    feature_map_layer = all_layers_value[0]
    layer1 = all_layers_value[1]
    layer2 = all_layers_value[2]
    outputlayer1 = all_layers_value[3]
    Truth_layer = all_layers_value[4]

    weight_fm2layer1 = all_init_weight[0]
    weight_layer12layer2 = all_init_weight[1]
    weight_layer2outputlayer = all_init_weight[2]

    all_weight_after_training = []
    #Assuming the weight we calculate in second last layer using the weight that "doesn't change" in last one layer
    #backward, weight between layer2 and outputlayer
    H1, W1 = get_size(weight_layer2outputlayer)
    d_w1 = np.zeros[H1,W1]
    for j in range(W1):
        for k in range(H1):
            d_w1[k,j] = layer2[j] * loss_vector[k] * outputlayer1[k] * (1-outputlayer1[k])
            weight_layer2outputlayer[k,j] -= lr * d_w1[k,j]           
    all_weight_after_training.append(weight_layer2outputlayer)

    #backward, weight between layer1 and layer2
    #1. calculate the diff from the output layer
    d_w2_from_last = np.zero(W1)#1-d
    for j in range(W1):
        for k in range(H1):
            d_w2_from_last[j] += loss_vector[k] * outputlayer1[k]* (1-outputlayer1[k]) * weight_layer2outputlayer[k,j] 
    H2, W2 = get_size(weight_layer12layer2)
    d_w2 = np.zeros(H2, W2)
    #2. calculate the weight in this layer
    for j in range(W2):
        for i in range(H2):
            d_w2[i,j] = layer1[i] * layer2[j] * (1-layer2[j]) * d_w2_from_last[i]
            weight_layer12layer2[i,j] -= lr * d_w2[i,j]
    all_weight_after_training.append(weight_layer12layer2)

    #backward, weight between feature map layer and layer1
    #1. calculate the diff from the output layer
    d_w3_from_last = np.zero(W2)#1-d
    for j in range(W2):
        for i in range(H2):
            d_w3_from_last[j] += weight_layer12layer2[i,j] * layer2[i] *(1-layer1[i]) * d_w2_from_last[i]
    #2. calculate the weight in this layer
    H3, W3 = get_size(weight_fm2layer1)
    d_w3 = np.zeros(H3,W3)
    for j in range(W3):
        for i in range(H3):
            d_w3[i,j] = feature_map_layer[i] * layer1[j] * (1-layer1[j]) * d_w3_from_last[i]
            weight_fm2layer1 -= lr * d_w3_from_last[i,j]
    all_weight_after_training.append(weight_fm2layer1)

    return all_weight_after_training

def MSE
def get_init_weight
def get_init_bias
def activate_func
def get_size

