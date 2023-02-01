from matplotlib import image
from numpy import block

# Convert Image to Binary Data
def convertToBinaryData(filename):

    # Convert binary format to images or files data
    with open(filename, 'rb') as file:
        blobData = file.read()
    
    # Return a Binary Data
    return blobData



