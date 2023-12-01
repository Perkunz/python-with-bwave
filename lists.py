






fruits = ['apple', 'banana', 'orange', 'grape']

first_fruit = fruits[0]
second_fruit = fruits[1]

selected_fruits = fruits[:3]

fruits[1] = 'pear'   #index [1] changing the banana to pear

#append means to add, remove

fruits.append('adara')

fruits.remove('grape')

length_fruits = len(fruits)



print(fruits)
print(length_fruits)

#nested lists

matrix = [ [1, 2, 3], [4, 5, 6], [7, 8, 9,] ]


more_fruits = ['pineapple', 'watermelon']
all_fruits = fruits + more_fruits

#when we talk about operatios w can use loop or conditional

Is_banana_present = 'banana' in fruits

print(all_fruits)
print(Is_banana_present)

repeated_fruits = fruits * 3
print(repeated_fruits)