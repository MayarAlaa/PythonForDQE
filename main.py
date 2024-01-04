import random

# create list of 100 random numbers from 0 to 1000
random_numbers = [random.randint(0, 1000) for _ in range(100)]

# sort list from min to max (without using sort())
min_num = random_numbers[0]
sorted_list = [min_num]

#selection sort
for i in range(len(random_numbers)):
    min_idx = i
    for j in range(i + 1, len(random_numbers)):
        if random_numbers[j] < random_numbers[min_idx]:
            min_idx = j
    random_numbers[i], random_numbers[min_idx] = random_numbers[min_idx], random_numbers[i]

print("Sorted List:", random_numbers)

# calculate average for even and odd numbers
even_sum = 0
even_cnt = 0
odd_sum = 0
odd_cnt = 0

for num in random_numbers:
    if num%2 == 0:
        even_sum += num
        even_cnt += 1
    else:
        odd_sum += num
        odd_cnt += 1


# Calculate averages
average_even = even_sum / even_cnt if even_cnt != 0 else 0
average_odd = odd_sum / odd_cnt if odd_cnt != 0 else 0
#print(type(average_odd))

# print both average result in console 
print("Average of even numbers:", average_even)
print("Average of odd numbers:", average_odd)

