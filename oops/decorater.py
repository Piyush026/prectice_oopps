# class Celsius:
#     def __init__(self, temperature = 0):
#         self.temperature = temperature
#     def fahrenheit(self):
#         return (self.temperature * 1.8) + 32
#     @property
#     def temperature(self):
#         print("Getting value")
#         return self._temperature
#     @temperature.setter
#     def temperature(self, value):
#         print("Setting value")
#         self._temperature = value
import time

li = [2, 4, 5, 7, 8]
# arr = []
for x in li:
    x = x * 2
    print(x)
    # arr.append(x)
# print(arr)
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))

ar = list(map(lambda x: x * 2, li))
print(ar)
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
##################chech funtion time in excution
# import timeit
#
#
# def my_function():
#     y = 3.1415
#     for x in range(100):
#         y = y ** 0.7
#     return y
#
#
# print(timeit.timeit(my_function, number=100000))
dic = {'Student Name': 'Berry', 'Roll No.': 12, 'Subject': 'English'}
print("Keys are:")
for k in dic.items():
    print(k)
