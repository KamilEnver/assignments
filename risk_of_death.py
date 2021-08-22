age = input("Are you a cigarette addict older than 75 years old?").strip().title()
chronic = input("Do you have a chronic disease?").strip().title()
immune = input("Is your immune system to weak?").strip().title()
if age == "Yes":
   age = True
else:
   age = False
if chronic == "Yes":
   chronic =True
else: 
   chronic = False
if immune == "Yes":
   immune = True
else:
  immune = False
risk = age or chronic or immune
if risk == True:
    print("You are in risky group")
else:
    print("you are not in risky group")
