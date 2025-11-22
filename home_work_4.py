# 1) ფუნქცია, რომელსაც გადაეცემა ერთი არგუმენტი, ეს არგუმენტი იქნება კილომეტრების რაოდენობა, ხოლო ფუნქციამ გადაცემული რიცხვი უნდა გადაიყვანოს მილებში. (1 mile = 1.6 km)
# მაგ: kilometres_to_miles(5) უნდა დააბრუნოს დაახლოებით 3.1

# 2) ფუნქცია, რომელსაც გადავცემთ 3 რიცხვს და უკან დაგვიბრუნებს მოცულობას. არცერთი არგუმენტი არ უნდა იყოს სავალდებულო.
# მაგ: calculate_volume(5, 3, 2) უნდა დააბრუნოს 30. calculate_volume(2, 5) უნდა დააბრუნოს 10, რადგან ერთი არგუმენტი არ გადავეცით.

# 3) ფუნქცია, რომელსაც გადავცემთ 1 რიცხვს და უკან დაგვიბრუნებს ლუწია თუ კენტი.
# მაგ: check_type(2) -> ლუწია 

# 4) ფუნქცია, რომელსაც შემიძლია გადავცე უსასრულო რაოდენობის სტრინგები, ხოლო უკან უნდა დამიბრუნოს სია სადაც იქნება მხოლოდ ისეთი სტრინგები რომელიც იწყება ხმოვანით.
# მაგ: get_vowels("Car", "Lap", "Allinol", "Interstate") უნდა დააბრუნოს ["Allinol", "Interstate"]

# N1

def kilometres_to_mile(km):
    mile = 1.6
    return km / mile

print(kilometres_to_mile(5))

# N2 (1)
def calculate_volume(x = None, y = None, z = None):
    
    if x is None and y is None and z is None:
        return 0
    
    x = x or 1
    y = y or 1
    z = z or 1
    return x * y * z

print(calculate_volume(3,4,6))
print(calculate_volume(6,4))
print(calculate_volume(5))
print(calculate_volume())

# N2 (2)

## def calculate_volume_1(x = 1, y = 1, z = 1):
##     return x * y * z

## print(calculate_volume(6,4,6))

# N3

def check_type(num):
    if num == 0: 
        return "It's not even or odd, it's just 0 :)"
    elif num % 2 == 0:
        return f"{num} is even"
    
    else: return f"{num} is odd"
    
print(check_type(2))
print(check_type(3))
print(check_type(0))

# N4
def get_vowels(*words):
    result = []
    vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    
    for word in words:
        if word[0] in vowels:
            result.append(word)
    
    return result

print(get_vowels("Car", "Lap", "Allinol", "Interstate"))
    
