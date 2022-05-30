import numpy as np
x1 = np.array(['Hello', 'PHP', 'JS', 'examples', 'html'], dtype=np.str)
x2 = np.array(['Hello', 'php', 'Java', 'examples', 'html'], dtype=np.str)
print("\nArray1:")
print(x1)
print("Array2:")
print(x2)
print("\nEqual test:")
r = np.char.equal(x1, x2)
print(r)
print("\nNot equal test:")
r = np.char.not_equal(x1, x2)
print(r)
print("\nLess equal test:")
r = np.char.less_equal(x1, x2)
print(r)
print("\nGreater equal test:")
r = np.char.greater_equal(x1, x2)
print(r)
print("\nLess test:")
r = np.char.less(x1, x2)
print(r)
© 2022 GitHub