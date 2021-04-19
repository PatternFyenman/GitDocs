#resize the picture before input
def resize(Origin_picture, target_size_H, target_size_W, keep_ratio=True):
    H,W = get_size(Origin_picture)

#Problem: how to scale a picture?
