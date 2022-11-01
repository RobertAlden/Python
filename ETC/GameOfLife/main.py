"""
Game of life using numpy solution inspired by APL.
"""
import numpy as np


def lifeInit(x, y):
    return np.random.randint(0, 2, (x, y), dtype=np.int8)


def lifeIter(arr):
    rollvec = [-1, 0, 1]
    all_rolls = [[np.roll(h, d, axis=1) for d in rollvec] for h in [np.roll(arr, d, axis=0) for d in rollvec]]
    sum_arr = np.add.reduce([np.add.reduce(v) for v in all_rolls])
    return (True & (sum_arr == 3)) | (arr & (sum_arr == 4))


def disp(arr):
    print("".join(['_'] * (2 + np.shape(arr)[0])))
    for i in arr:
        print('|'+"".join(['.O'[x] for x in i])+'|')
    print("".join(['_'] * (2 + np.shape(arr)[0])))


def main():
    # grid = lifeInit(5, 5)
    grid = np.pad(np.array([1, 1, 1,
                            1, 0, 0,
                            0, 1, 0]).reshape((3, 3)), 3, constant_values=0)
    for i in range(25):
        grid = lifeIter(grid)
        disp(grid)


if __name__ == '__main__':
    main()
