import numpy as np 
import matplotlib.pyplot as plt

pattern_0 = np.array( [0,0,0,0,0,0,0,0,0,0,
                       0,0,0,1,1,1,1,0,0,0,
                       0,0,1,1,1,1,1,1,0,0,
                       0,1,1,1,0,0,1,1,1,0,
                       0,1,1,1,0,0,1,1,1,0,
                       0,1,1,1,0,0,1,1,1,0,
                       0,1,1,1,0,0,1,1,1,0,
                       0,1,1,1,0,0,1,1,1,0,
                       0,1,1,1,0,0,1,1,1,0,
                       0,0,1,1,1,1,1,1,0,0,
                       0,0,0,1,1,1,1,0,0,0,
                       0,0,0,0,0,0,0,0,0,0])

pattern_1 = np.array( [0,0,0,1,1,1,1,0,0,0,
                       0,0,0,1,1,1,1,0,0,0,
                       0,0,0,1,1,1,1,0,0,0,
                       0,0,0,1,1,1,1,0,0,0,
                       0,0,0,1,1,1,1,0,0,0,
                       0,0,0,1,1,1,1,0,0,0,
                       0,0,0,1,1,1,1,0,0,0,
                       0,0,0,1,1,1,1,0,0,0,
                       0,0,0,1,1,1,1,0,0,0,
                       0,0,0,1,1,1,1,0,0,0,
                       0,0,0,1,1,1,1,0,0,0,
                       0,0,0,1,1,1,1,0,0,0])

pattern_2 = np.array( [1,1,1,1,1,1,1,1,0,0,
                       1,1,1,1,1,1,1,1,0,0,
                       0,0,0,0,0,0,1,1,0,0,
                       0,0,0,0,0,0,1,1,0,0,
                       0,0,0,0,0,0,1,1,0,0,
                       1,1,1,1,1,1,1,1,0,0,
                       1,1,1,1,1,1,1,1,0,0,
                       1,1,0,0,0,0,0,0,0,0,
                       1,1,0,0,0,0,0,0,0,0,
                       1,1,0,0,0,0,0,0,0,0,
                       1,1,1,1,1,1,1,1,0,0,
                       1,1,1,1,1,1,1,1,0,0])

pattern_3 = np.array( [0,0,1,1,1,1,1,1,0,0,
                       0,0,1,1,1,1,1,1,1,0,
                       0,0,0,0,0,0,0,1,1,0,
                       0,0,0,0,0,0,0,1,1,0,
                       0,0,0,0,0,0,0,1,1,0,
                       0,0,0,0,1,1,1,1,0,0,
                       0,0,0,0,1,1,1,1,0,0,
                       0,0,0,0,0,0,0,1,1,0,
                       0,0,0,0,0,0,0,1,1,0,
                       0,0,0,0,0,0,0,1,1,0,
                       0,0,1,1,1,1,1,1,1,0,
                       0,0,1,1,1,1,1,1,0,0])

pattern_4 = np.array( [0,1,1,0,0,0,0,1,1,0,
                       0,1,1,0,0,0,0,1,1,0,
                       0,1,1,0,0,0,0,1,1,0,
                       0,1,1,0,0,0,0,1,1,0,
                       0,1,1,0,0,0,0,1,1,0,
                       0,1,1,1,1,1,1,1,1,0,
                       0,1,1,1,1,1,1,1,1,0,
                       0,0,0,0,0,0,0,1,1,0,
                       0,0,0,0,0,0,0,1,1,0,
                       0,0,0,0,0,0,0,1,1,0,
                       0,0,0,0,0,0,0,1,1,0,
                       0,0,0,0,0,0,0,1,1,0])

pattern_6 = np.array( [1,1,1,1,1,1,1,1,0,0,
                       1,1,1,1,1,1,1,1,0,0,
                       1,1,0,0,0,0,0,0,0,0,
                       1,1,0,0,0,0,0,0,0,0,
                       1,1,0,0,0,0,0,0,0,0,
                       1,1,1,1,1,1,1,1,0,0,
                       1,1,1,1,1,1,1,1,0,0,
                       1,1,0,0,0,0,1,1,0,0,
                       1,1,0,0,0,0,1,1,0,0,
                       1,1,0,0,0,0,1,1,0,0,
                       1,1,1,1,1,1,1,1,0,0,
                       1,1,1,1,1,1,1,1,0,0])

pattern_dot = np.array([1,1,1,1,1,0,0,0,0,0,
                        1,1,1,1,1,0,0,0,0,0,
                        1,1,1,1,1,0,0,0,0,0,
                        1,1,1,1,1,0,0,0,0,0,
                        1,1,1,1,1,0,0,0,0,0,
                        1,1,1,1,1,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0])

pattern_9 = np.array( [0,0,0,0,1,1,1,1,1,1,
                       0,0,0,0,1,1,1,1,1,1,
                       0,0,0,0,1,1,0,0,1,1,
                       0,0,0,0,1,1,0,0,1,1,
                       0,0,0,0,1,1,0,0,1,1,
                       0,0,0,0,1,1,1,1,1,1,
                       0,0,0,0,1,1,1,1,1,1,
                       0,0,0,0,0,0,0,0,1,1,
                       0,0,0,0,0,0,0,0,1,1,
                       0,0,0,0,0,0,0,0,1,1,
                       0,0,0,0,1,1,1,1,1,1,
                       0,0,0,0,1,1,1,1,1,1])

def HF_space(array):
    for i in range(array.shape[0]):
        if array[i] == 0:
            array[i] = -1
    return array

def corrupted_pattern(data,reversed_pixel):
    count = 0
    count_pixel = 0
    for j in range(data.shape[0]):
        if data[j] == 1:
            count_pixel = count_pixel +1
    while count < (1-reversed_pixel)*count_pixel:
        for i in range(data.shape[0]):
            if data[i] == 1:
                a = np.random.randint(0,2)
                if a == 0:
                    data[i] = data[i]*-1
                    count = count + 1
                if count >= (1-reversed_pixel)*count_pixel:
                    break
    # print(count)
    return data

# a = corrupted_pattern(pattern_4,0.25)
# print(a.reshape(12,10))
# 48 * 25% = 12 remain pixels, change 36 pixel 
# b = HF_space(pattern_0)
# print(b.reshape(12,10))

pattern_0 = HF_space(pattern_0)
pattern_1 = HF_space(pattern_1)
pattern_2 = HF_space(pattern_2)
pattern_3 = HF_space(pattern_3)
pattern_4 = HF_space(pattern_4)
pattern_6 = HF_space(pattern_6)
pattern_dot = HF_space(pattern_dot)
pattern_9 = HF_space(pattern_9)

# plt.imshow(corrupted_pattern(pattern_0,0.25).reshape(12,10))
# plt.colorbar()
# plt.show()
# plt.imshow(np.reshape(pattern_0,(12,10)),cmap="binary")
# plt.figure()
# corrupted0 = corrupted_pattern(pattern_0,0.25)
# plt.imshow(np.reshape(corrupted0,(12,10)),cmap="binary")
# plt.show()