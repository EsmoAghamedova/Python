# პროგრამა 1:
# input ფუნქციის საშუალებით, მომხმარებელს შეაყვანინეთ რამე ციფრი და შეინახეთ ცვლადში.
# შემდეგ შეაყვანინეთ მეორე ციფრი და ისიც შეინახეთ ცვლადში.

# თუ პირველი ციფრი არის მეტი მეორეზე, დაუპრინტეთ მომხმარებელს რომ პირველი ციფრი მეტია.
# თუ მეორე ციფრი არის პირველზე მეტი, დაუპრინტეთ რომ მეორე შეყვანილი რიცხვი უფრო დიდია.
# ხოლო თუ ორივე ციფრი ტოლია, დაუპრინტეთ რომ ტოლია.


x = float(input("Enter first number:"))
y = float(input("Enter Second number:"))

if x > y:
    print("First num is bigger than second num")
elif x < y:
    print("Second num is bigger than first num")
else:
    print("They are equal")
