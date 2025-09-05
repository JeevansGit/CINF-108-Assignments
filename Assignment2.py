import math

class ProblemSolutions:

#problem 1
    def sum_average(self, numbers):
        total = sum(numbers)
        if numbers:
            average = total/len(numbers) 
        else:
            average = 0
        print(f'total: {total} average; {average}')
      
    
    
#problem 2
    def celcius_to_kelvin(self):
        celsius = float(input("Enter a number to turn into Kelvin: "))
        print(f'It is {celsius + 273.15} degrees Kelvin')

#problem 3 
    def palindrome(self):
        input_var = input("Enter a string: ")
        if input_var == input_var[::-1]:
          print("This is a palindrome! ")
        else:
            print("This is not a palindrome! ")

#problem 4
    def reverse_string(self):
        text = input("Input any text: ")
        print(f'The text reversed is {text[::-1]}')

#problem 5
    def combine_names(self):
        names = input("Enter names separated by a space: ").split()
        print("Combined string: " , " ".join(names))

#problem 6
    def is_panagram(self):
        text = input("Enter a string of words: ")
        alphabet = set("abcdefghijklmnopqrstuvwxyz")
        if alphabet.issubset(set(text.lower())):
            print("It is a pangram")
        else:
            print("It is not a pangram")

#problem 7
    def calc_area(self):
        radius = float(input("Enter a number for its radius: "))
        area = math.pi * pow(radius, 2)
        circumference = 2* math.pi * radius
        print(f'Your area is {area} and your circumference is {circumference}')

#problem 8  
    def mins_to_hours(self):
       mins =  int(input("Enter a number for minutes: "))
       hours = mins//60 #whole number division
       leftovers = mins % 60
       print(f'Converted to hours is {hours} and leftover minutes is {leftovers}')

#problem 9
    def vowels_in_string(self):
        text = input("Enter a string of words: ")
        vowels = set("aeiou")
        count = 0
        for char in text.lower():
            if char in vowels:
                count+=1
        if count > 0:
            print(f"{count} vowels in string ")
        else:
            print("No vowels in string ")

#problem 10
    def prime_checker(self):
        num = int(input("Enter a number: "))

        if num <=1:
            print(f'{num} is not prime')
            return
            
        prime_num = True
        for i in range(2, num):
            if num % i ==0:
                prime_num =False
                break
        
        if prime_num:
            print(f"{num} is a prime")
        else:
            print(f"{num} is not a prime")

# Create instance
ps = ProblemSolutions()

# Call some methods to test
ps.sum_average([10, 20, 30, 40])
ps.celcius_to_kelvin()     
ps.palindrome()             
ps.reverse_string()       
ps.combine_names()           
ps.is_panagram()            
ps.calc_area()              
ps.mins_to_hours()         
ps.vowels_in_string()    
ps.prime_checker()          
    

