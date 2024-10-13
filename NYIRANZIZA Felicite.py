print("one dimensional_ array")


print("q1")

city_temperature =[15,23,30,45,50,38,49]
for i, a in enumerate(city_temperature):
   print(f"day {i+ 1}:{a}")
 
print("q2")
 
daily_sales= [100,200,300,400,500,250,350]
average_sales = sum(daily_sales) / 7
print(average_sales)

print("q3") 
price=  [110,540,650,800,300,890,1000]
print("max_price:",max(price))
print("min_price:",min(price))

print("q4")

math =[70,30,65,47,26,80,90,72]
math.reverse()
print("reversed marks:",math)

print("q5")

numbers= [10,15,20,30,50,43,76]
odd_c  ,even_c = 0 ,0
for num in numbers :
 if (num % 2  ==0 ) :
   even_c  += 1
 else:
  odd_c  += 1
print("the numbers of even numbers is:", even_c)
print("the numbers of odd numbers is :", odd_c)

     
print("multi_deminsion array")

print("Q6")

board =[
          ['x','o','o'],
          ['o','x','o'],
          ['x','x','x']
]
def check_winner(board):
   for row in board:
   	    if row[0] == row[1] == row[2]:
       	       return f"winner is {row[0]}"
   for col in range(3):
       if board[0][col] == board[1][col] == board[2][col]:
	         return f"the winner is {board[0][col]}"
	
   if board[0][0] == board[1][1] == board[2][2]:
		     return {board[0][0]}
   return'toe'

print(check_winner(board))
print('Q7')

shop = [
[100,200,300,400,250,500,700],
[250,200,300,400,600,500,700],
[100,200,250,400,600,500,700]
]
for index ,product in enumerate(shop):
	print (f"product{index+1}{list(product)}")
print("Q8")

colors =[
           [255,0,0],
           [0,255,0],
           [0,0,255]

 ]
colors[0] = colors[1]
colors[1] = colors[2]
colors[2] = colors[0]

print(colors)
print('Q9')
total_marks=[
       [90,80,20],
       [50,67,76],
       [98,87,86]


]
for index ,total in enumerate(total_marks):
	
	print(f"student {index+1} marks:{sum(total)}")

print('Q10')
temperatures_city = [
[20, 30, 40, 20, 40, 20, 30], 
[ 20, 40, 20, 30, 20, 40,10], 
[30, 20, 40, 10,30, 20, 40,], 
[30, 20, 40, 10,30, 20, 40,] 
]

for index , daily in enumerate(temperatures_city):
 print(f"the temperature of city{index+1} {sum(daily)/7:.2f}")



print('the quest on list')

print('Q1')

Meeting =['paul','enock','betty']
Meeting.append('tony')
print(Meeting)  

print('Q2')

shop =['meat','beans','oranges']
shop.remove ('beans')
print(shop)

print('Q3')
names=[24,60,34,55]

names.sort()
print(names)

print('Q4')

todo_list = ["driving", "teaching", "cleaning", "pray"]

print("Original to-do list:", todo_list)


def complete_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f'Task completed: "{task}"')
    else:
        print(f'Task not found: "{task}"')


complete_task("Pay bills")


print("Updated to-do list:", todo_list)


print('q5')

double_list=["belyse","kelen","enock"]
print(f"first list:{double_list}")
friend_list=["enock","annet","danny"]
print(f"second list:{friend_list}")
merged_friend_list= list(set(friend_list + double_list))
print(f"removed after duplicated names: {merged_friend_list}")



print('Q6')
for index ,days in enumerate(temperatures_city):
	print(f"the day{index+1}:{sum(days)/7:.2f}%")

students = [
 ['stud1', 30, 'A'],
 ['stud2', 28, 'C'],
 ['stud3', 32, 'B']
]
students.sort(key=lambda student: student[2])
print(students)

print('Q7')
expenses = [
    [1200, 300, 150],  
    [1300, 350, 200],
    [1250, 320, 180],
    [1400, 400, 220],
    [1350, 370, 210],
    [1300, 360, 230] 
]


total_expenses = [0] * len(expenses[0])


for month in expenses:
    for i in range(len(month)):
        total_expenses[i] += month[i]    


average_expenses = [total / len(expenses) for total in total_expenses]


categories = ["Rent", "Food", "Utilities"]
for category, average in zip(categories, average_expenses):
    print(f"Average monthly expense for {category}: Rwf{average:.2f}")

print('q8')

seating_arr=[
[1,2,3,4,5],
[6,7,8,9,10],
[11,12,13,14]
]

seating_arr.reverse()
print(seating_arr)


print('q9')


products=[
["apple",500,10],
["beans",1000,35],
["rice",1500,40],
["salt", 2000,80]
]
in_stock_products= [product for product in products if product[2] > 0]

print("in stock products:")
for product in in_stock_products:
	print(f"name:{product[0]},price: rwf{product[1]:.3f},stock:{product[2]}")

print('Q10')	
scores = [
    ["Derrick", [90, 85, 78]],
    ["Ora", [82, 91, 88]],
    ["Chantal", [75, 80, 95]],
    ["David", [100, 90, 85]]
]

def average_score(scores):
    return sum(scores) / len(scores)

winner = None
highest_average = 0

for player in scores:
    name = player[0]
    player_scores = player[1]
    avg = average_score(player_scores)
    
    if avg > highest_average:
        highest_average = avg
        winner = name


print(f"The winner is {winner} with an average score of {highest_average:.2f}.")











