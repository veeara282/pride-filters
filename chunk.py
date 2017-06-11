import numpy as np

def chunk(image, n_stripes=1):
    # Special cases
    if n_stripes < 1:
        raise ValueError("Only positive integers are allowed!")
    if n_stripes == 1:
        return [image]
    
    ## General case ##

    # Get height of image
    height = image.shape[0]
    
    # Set approximate minimum pixel heights for the stripes
    boundaries = [int(i * height / n_stripes) for i in range(n_stripes)]
    top = lambda i: boundaries[i]
    bottom = lambda i: boundaries[i+1] if i < (n_stripes - 1) else height

    # Divide image vertically into 'n_stripes' roughly equally sized horizontal bands
    stripes = [ image[top(i) : bottom(i)] for i in range(n_stripes)]

    return stripes

def unchunk(stripes):
    image = np.concatenate(stripes, axis = 0)
    return image
