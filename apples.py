apple = int((input) ("How many apples do you have?"))
weight = str((input) ("Kg or Lbs?"))

Kg = 0.2 
Lbs = 0.44

if weight == "Kg":
    print(apple * Kg)
else:
     print(apple * Lbs)