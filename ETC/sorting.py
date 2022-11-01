from random import shuffle
from time import perf_counter

numOfElements = 10
data = [i for i in range(numOfElements)]
shuffle(data)
#print(f"Initial Data: {data}")

def isSorted(arr):
	for i in range(len(arr)-1):
		if arr[i] > arr[i+1]:
			return False
	else:
		return True

def bogoSort(arr):
	l_arr = arr[:]
	while not isSorted(l_arr):
		shuffle(l_arr)
		print(l_arr)
	return l_arr[:]

def insertionSort(arr):
	l_arr = arr[:]
	for i in range(1,len(l_arr)):
		key = l_arr[i]
		j = i-1
		while j >= 0 and l_arr[j] > key:
			l_arr[j+1] = l_arr[j]
			j-=1
		l_arr[j+1] = key
	return l_arr[:]

def mergeSort(arr,b,e):
	l_arr = arr[:]
	if b >= e:
		return None
	m = b + (e - b) / 2
	mergeSort(l_arr,b,m)
	mergeSort(l_arr,m+1,e0)
	merge(l_arr,b,m,e)

def merge(arr,l,m,r):
	l_arr = arr[:]
	s1 = m - l + 1
	s2 = r - m

	arr1 = arr[:s1]
	arr2 = arr[s2:]

	i1 = 0
	i2 = 0

	i_m = l

	while(i1 < s1 and i2 < s2):
		if arr1[i1] <= arr2[i2]:
			l_arr[i_m] = arr1[i1]
			i1 += 1
		else:
			l_arr[i_m] = arr2[i2]
			i2 += 1
		i_m += 1

	while(i1 < s1):
		l_arr[i_m] = arr1[i1]
		i1 += 1
		i_m += 1

	while(i2 < s2):
		l_arr[i_m] = arr2[i2]
		i2 += 1
		i_m += 1

	return l_arr[:]

print(mergeSort(data,0,numOfElements))

