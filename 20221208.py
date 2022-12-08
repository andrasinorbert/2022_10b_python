from typing import Callable, Iterable

input_string= "Árvíztűrőtükörfúrógép"

def maganhangzo_e(char):
    maganhangzok="aáeéiíoóöőuúüű"
    if(char.lower() in maganhangzok):
        return True
    return False

def szetvalogatasTetel(list:Iterable, feltetelFunc:Callable):
    """
    Args:
        list: iterable element
        feltetelFunc: return True/False function
    Returns:
        tuple[0]: list -> feltetelFunc if True
        tuple[1]: list -> feltetelFunc if False
    """
    c=0
    Y=[]
    Z=[]
    for i in range(len(list)):
        if(feltetelFunc(list[i])):
            Y.append(list[i])
            c+=1
        else:
            Z.append(list[i])
    return (Y,Z)

print(szetvalogatasTetel("hAjÓ", maganhangzo_e))
