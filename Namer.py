letters = {
  "A": 1,
  "B": 2,
  "C": 3,
  "D": 4,
  "E": 5,
  "F": 6,
  "G": 7,
  "H": 8,
  "I": 9,
  "J": 10,
  "k":11,
  "L": 12,
  "M": 13,
  "N": 14,
  "O": 15,
  "P": 16,
  "Q": 17,
  "R": 18,
  "S": 19,
  "T": 20,
  "U": 21,
  "V": 22,
  "W": 23,
  "X": 24,
  "Y": 25,
  "Z": 26,

}

f = open("p022_names.txt", "r")
names_ordered = f.read()
x = names_ordered.split(",")

x.sort()
print(x)


user_input = input("Enter your number ")
try:
    val = int(user_input)
    print("Input is an integer number. Number = ", val)
except ValueError:
    try:
        val = float(user_input)
        print("Input is a float  number. Number = ", val)
    except ValueError:
        print("No.. input is not a number. It's a string")


name_value = x[val - 1]

char_letter=list(name_value)
char_value =[]

for w in char_letter:
  
  if w in letters.keys():
    char_value.append(letters.get(w)) 
  
sum =0
for num in char_value:
  sum+=num
print(char_letter)
def add_score_position(score,pos):
  return print (score*pos)
  

add_score_position(sum,val)   
  


   

  




