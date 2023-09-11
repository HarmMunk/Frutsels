from array import array
from os import linesep

floats1 = array('d', (1.0, 2.0, 3.0))
floats2 = array('d', (4.0, 5.0, 6.0))

print(f"floats1={floats1}; floats2={floats2}")
print(f"floats1.__add__(floats2)={floats1.__add__(floats2)}; floats1={floats1}; floats2={floats2}")
print(f"floats1.__iadd__(floats2)={floats1.__iadd__(floats2)}; floats1={floats1}; floats2={floats2}")

floats1 = array('d', (1.0, 2.0, 3.0))
print(f"floats1.byteswap()={floats1.byteswap()}; floats1={floats1}; floats2={floats2}")

floats1 = array('d', (1.0, 2.0, 3.0))
floats3 = floats1.__copy__()
floats3.append(10.0)
floats4 = floats1.__deepcopy__(None)
floats4.append(20.0)
print(f"floats3={floats3}; floats4={floats4}; floats1={floats1}; floats2={floats2}")

floats3 = array('d', (7.0, 8.0, 9.0))
it1 = (11.0, 12.0, 13.0)
it2 = {14.0, 15.0, 16.0}
it3 = [17.0, 18.0, 19.0]
floats1.extend(it1)
floats2.extend(it2)
floats3.extend(it3)
print(f"floats1.extend((11.0, 12.0, 13.0)): {floats1}; floats2.extend({14.0, 15.0, 16.0}): {floats2}; floats3.extend([17.0, 18.0, 19.0]): {floats3}")

floats1 = array('d', (1.0, 2.0, 3.0))
floats1.fromlist([1, float("2.0"), 3])
print(f"floats1.fromlist([1, 2, 3]: {floats1}")

print(f"floats1.__iter__(): {floats1.__iter__()}")

floats1 = array('d', (1.0, 2.0, 3.0))
print(f"floats1.__mul__(3): {floats1.__mul__(3)}; floats1={floats1}")
print(f"floats1.__imul__(3): {floats1.__imul__(3)}; floats1={floats1}")
floats1 = array('d', (1.0, 2.0, 3.0))
print(f"floats1.__rmul__(3): {floats1.__rmul__(3)}; floats1={floats1}")
