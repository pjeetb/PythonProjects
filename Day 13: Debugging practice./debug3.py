#here in the condition, or operator was used instead of and because of which both the conditions were not checked.
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0: 
    print("FizzBuzz")
  elif number % 3 == 0:   #here elif is used to check the condition again when the first condition is failed.
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
