from collections import namedtuple
from typing import List

Box = namedtuple('Box', 'get_key')

def fatorial(n:int) -> int:
    #caso base
    if n == 1:
        return 1
    #caso recursivo - a função chama a si propria
    return n * fatorial(n - 1)

def search_key(box: List[Box], index: int=0) -> Box:
    #caso base
    if len(box) <= index:
        return Box(False)
    
    boxs = box[index]
    
    #caso base
    if boxs.get_key:
        return boxs
    
    #caso recursivo
    index += 1
    return search_key(box, index)



if __name__=="__main__":
    caixas: List[Box] = [
        Box(False), Box(False), Box(False),
        Box(False), Box(False), Box(False),
        Box(False), Box(True),Box(False),
    ]
    print(search_key(caixas))