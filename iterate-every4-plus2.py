# This is one of my favorite because I came up with this fun experiment while laying on bed :)

#### Task
# do an action every 4 times and every time add  2 times
# so after 4 then after 6 then after 8 then after 10. The result is: 4th, 10th, 18th, 28th...etc

Start_value = 4 # Beginning 
Incremental_value = 4
for i in range(1, 100):
    if i == 4:
        print(i)
        Start_value  += 2
        Incremental_value  = i + Start_value 
    elif i % Incremental_value == 0:
        print(i)
        Start_value  += 2
        Incremental_value  = i + Start_value 
