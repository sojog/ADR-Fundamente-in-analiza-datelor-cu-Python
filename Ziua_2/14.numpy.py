# pip install numpy
import numpy as np

print(np.__version__)



# int8 -> -128 .. 127  -2 ** 6
lista = [1, 2, 3, -128]
print("lista:", lista)
print("type(lista)", type(lista))

## Array spre deosebire de lista are toate elementele de acelasi tip
arr = np.array(lista, dtype=np.int8)
print("arr:", arr)
print("type(arr)", type(arr))
print("arr.dtype", arr.dtype)


# int64 -> - (2 ** 32 ) -> 2 **32 - 1
print(2 ** 63 - 1)