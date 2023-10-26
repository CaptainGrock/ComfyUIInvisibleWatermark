import math
import random
import torch

class watermark_Mark:
    """
    A example node

    Class methods
    -------------
    INPUT_TYPES (dict): 
        Tell the main program input parameters of nodes.

    Attributes
    ----------
    RETURN_TYPES (`tuple`): 
        The type of each element in the output tulple.
    RETURN_NAMES (`tuple`):
        Optional: The name of each output in the output tulple.
    FUNCTION (`str`):
        The name of the entry-point method. For example, if `FUNCTION = "execute"` then it will run Example().execute()
    OUTPUT_NODE ([`bool`]):
        If this node is an output node that outputs a result/image from the graph. The SaveImage node is an example.
        The backend iterates on these output nodes and tries to execute all their parents if their parent graph is properly connected.
        Assumed to be False if not present.
    CATEGORY (`str`):
        The category the node should appear in the UI.
    execute(s) -> tuple || None:
        The entry point method. The name of this method must be the same as the value of property `FUNCTION`.
        For example, if `FUNCTION = "execute"` then this method's name must be `execute`, if `FUNCTION = "foo"` then it must be `foo`.
    """
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        """
            Return a dictionary which contains config for all input fields.
            Some types (string): "MODEL", "VAE", "CLIP", "CONDITIONING", "LATENT", "IMAGE", "INT", "STRING", "FLOAT".
            Input types "INT", "STRING" or "FLOAT" are special values for fields on the node.
            The type can be a list for selection.

            Returns: `dict`:
                - Key input_fields_group (`string`): Can be either required, hidden or optional. A node class must have property `required`
                - Value input_fields (`dict`): Contains input fields config:
                    * Key field_name (`string`): Name of a entry-point method's argument
                    * Value field_config (`tuple`):
                        + First value is a string indicate the type of field or a list for selection.
                        + Secound value is a config for type "INT", "STRING" or "FLOAT".
        """
        return {
            "required": {
                "image": ("IMAGE",),
                "encode": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": ""
                }),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    #RETURN_NAMES = ("image_output_name",)
    FUNCTION = "mark"
    # OUTPUT_NODE = True
    CATEGORY = "Invisible Watermark"

    @staticmethod
    def mark(image, encode):
        if(len(encode) > 12):
            raise Exception
        w = image.shape[1]-1
        h = image.shape[2]-1
        chars = [ord(c)-65 for c in encode]
        for i in range(3):
            if(int(image[0][1][0][i%3]*255) % 2 == 0):
                image[0][1][0][i%3] += 1/255
            if(int(image[0][w-1][0][i%3]*255) % 2 == 0):
                image[0][w-1][0][i%3] += 1/255
            if(int(image[0][1][h][i%3]*255) % 2 == 0):
                image[0][1][h][i%3] += 1/255
            if(int(image[0][w-1][h][i%3]*255) % 2 == 0):
                image[0][w-1][h][i%3] += 1/255
            image[0][2][0][0] = len(chars)/255
        for i in range(len(chars)):
            if(i < 3):
                image[0][0][0][i%3] = chars[i] / 255
                binary = bin(int(image[0][0][0][i%3]*255))
                while(len(binary) < 10):
                    binary = binary[0:2] + "0" + binary[2:]
                if(binary[3] == 1):
                    image[0][0][0][i%3] += 64/255
                if(binary[2] == 1):
                    image[0][0][0][i%3] += 128/255
            elif(i < 6):
                image[0][w][0][i%3] = chars[i] / 255
                binary = bin(int(image[0][w][0][i%3]*255))
                while(len(binary) < 10):
                    binary = binary[0:2] + "0" + binary[2:]
                if(binary[3] == 1):
                    image[0][w][0][i%3] += 64/255
                if(binary[2] == 1):
                    image[0][w][0][i%3] += 128/255
            elif(i < 9):
                image[0][0][h][i%3] = chars[i] / 255
                binary = bin(int(image[0][0][h][i%3]*255))
                while(len(binary) < 10):
                    binary = binary[0:2] + "0" + binary[2:]
                if(binary[3] == 1):
                    image[0][0][h][i%3] += 64/255
                if(binary[2] == 1):
                    image[0][0][h][i%3] += 128/255
            else:
                image[0][w][h][i%3] = chars[i] / 255
                binary = bin(int(image[0][w][h][i%3]*255))
                while(len(binary) < 10):
                    binary = binary[0:2] + "0" + binary[2:]
                if(binary[3] == 1):
                    image[0][w][h][i%3] += 64/255
                if(binary[2] == 1):
                    image[0][w][h][i%3] += 128/255
        return (image,)
    

class watermark_Extract:
    """
    A example node

    Class methods
    -------------
    INPUT_TYPES (dict): 
        Tell the main program input parameters of nodes.

    Attributes
    ----------
    RETURN_TYPES (`tuple`): 
        The type of each element in the output tulple.
    RETURN_NAMES (`tuple`):
        Optional: The name of each output in the output tulple.
    FUNCTION (`str`):
        The name of the entry-point method. For example, if `FUNCTION = "execute"` then it will run Example().execute()
    OUTPUT_NODE ([`bool`]):
        If this node is an output node that outputs a result/image from the graph. The SaveImage node is an example.
        The backend iterates on these output nodes and tries to execute all their parents if their parent graph is properly connected.
        Assumed to be False if not present.
    CATEGORY (`str`):
        The category the node should appear in the UI.
    execute(s) -> tuple || None:
        The entry point method. The name of this method must be the same as the value of property `FUNCTION`.
        For example, if `FUNCTION = "execute"` then this method's name must be `execute`, if `FUNCTION = "foo"` then it must be `foo`.
    """
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        """
            Return a dictionary which contains config for all input fields.
            Some types (string): "MODEL", "VAE", "CLIP", "CONDITIONING", "LATENT", "IMAGE", "INT", "STRING", "FLOAT".
            Input types "INT", "STRING" or "FLOAT" are special values for fields on the node.
            The type can be a list for selection.

            Returns: `dict`:
                - Key input_fields_group (`string`): Can be either required, hidden or optional. A node class must have property `required`
                - Value input_fields (`dict`): Contains input fields config:
                    * Key field_name (`string`): Name of a entry-point method's argument
                    * Value field_config (`tuple`):
                        + First value is a string indicate the type of field or a list for selection.
                        + Secound value is a config for type "INT", "STRING" or "FLOAT".
        """
        return {
            "required": {
                "image": ("IMAGE",),
                # "output": ("STRING", {
                #     "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                #     "default": "0"
                # }),
            },
        }

    # RETURN_TYPES = ("STRING",)
    RETURN_TYPES = ("STRING",)
    #RETURN_NAMES = ("image_output_name",)
    FUNCTION = "extract"
    # OUTPUT_NODE = True
    CATEGORY = "Invisible Watermark"

    @staticmethod
    def extract(image):
        w = image.shape[1]-1
        h = image.shape[2]-1
        chars = []
        good = False
        for i in range(int(image[0][2][0][0]*255)):
            if(i < 3):
                if(int(image[0][1][0][i%3]*255)%2 == 1):
                    temp = int(image[0][0][0][i%3]*255)
                    binary = bin(temp)
                    while(len(binary) < 10):
                        binary = binary[0:2] + "0" + binary[2:]
                    if(binary[3] == "1"):
                        temp -= 64
                    if(binary[2] == "1"):
                        temp -= 128
                    chars.append(temp)
                else:
                    break
            elif(i < 6):
                if(int(image[0][w-1][0][i%3]*255)%2 == 1):
                    temp = int(image[0][w][0][i%3]*255)
                    binary = bin(temp)
                    while(len(binary) < 10):
                        binary = binary[0:2] + "0" + binary[2:]
                    if(binary[3] == "1"):
                        temp -= 64
                    if(binary[2] == "1"):
                        temp -= 128
                    chars.append(temp)
                else:
                    break
            elif(i < 9):
                if(int(image[0][1][h][i%3]*255)%2 == 1):
                    temp = int(image[0][0][h][i%3]*255)
                    binary = bin(temp)
                    while(len(binary) < 10):
                        binary = binary[0:2] + "0" + binary[2:]
                    if(binary[3] == "1"):
                        temp -= 64
                    if(binary[2] == "1"):
                        temp -= 128
                    chars.append(temp)
                else:
                    break
            else:
                if(int(image[0][w-1][h][i%3]*255)%2 == 1):
                    temp = int(image[0][w][h][i%3]*255)
                    binary = bin(temp)
                    while(len(binary) < 10):
                        binary = binary[0:2] + "0" + binary[2:]
                    if(binary[3] == "1"):
                        temp -= 64
                    if(binary[2] == "1"):
                        temp -= 128
                    chars.append(temp)
                else:
                    break
        else:
            good = True
        if(good):
            stri = ''.join(chr(i+65) for i in chars)
            return (stri,)
        else:
            return (" ",)


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "Apply Invisible Watermark": watermark_Mark,
    "Extract Watermark": watermark_Extract,
}