import random 
classes_per_week = 3
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes / weeks))
print ("Cost per week:", cost_per_week)
cost_per_class = ((cost_per_week / classes_per_week))
print ("Cost per class: ", cost_per_class)
print (classes_per_week, type (classes_per_week))    
print (weeks, type(weeks))
print (classes, type(classes))
print (tuition, type (tuition))
print (cost_per_week, type (cost_per_week))
print (cost_per_class, type (cost_per_class))
my_list = ["apple", "banana", 5.1, "cat", " dog", 4, "monkey"]
my_thing = (random.choice (my_list))
print ("My thing:", my_thing)
