class student:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
    
    def get_info(self): 
        print(f"   • {self.firstName} {self.lastName}   |   ასაკი: {self.age}")


class school:
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress
        self.students = []

        print("\n" + "=" * 50)
        print(f"🏫 სკოლა: {self.name}")
        print(f"📍 მისამართი: {self.adress}")
        print("=" * 50)
        
    def add_student(self, student):
        student.school = self.name
        self.students.append(student)
        
    def remove_student(self, index):
        self.students.pop(index)
        
    def show_students(self):
        print("\n" + "-" * 50)
        print(f"📚 მოსწავლეების სია — {self.name}")
        print("-" * 50)
        
        if len(self.students) == 0:
            print("   (სტუდენტები არ არიან დამატებული)")
        
        for st in self.students:
            st.get_info()

        print("-" * 50 + "\n")

# 1 სკოლა

sch1 = school("N85 საჯარო სკოლა", "თბილისი")

# s1 = student("ესმირა", "აღამედოვა", 16)
# s2 = student("ნინი", "იაკობიძე", 17)
# s3 = student("ლუკა", "მუმლაძე", 15)
# s4 = student("თამარ", "გიორგაძე", 16)

# sch1.add_student(s1)
# sch1.add_student(s2)
# sch1.add_student(s3)
# sch1.add_student(s4)

sch1.show_students()

# sch1.remove_student(1)

print("❌ ნინი იაკობიძე წაიშალა სიიდან")
sch1.show_students()

# 2 სკოლა

sch2 = school("კომაროვი", "თბილისი")

a1 = student("რომა", "ქვრივიშვილი", 16)
a2 = student("მარიამ", "გიორგაძე", 15)
a3 = student("თორნიკე", "მუმლაძე", 17)


sch2.add_student(a1)
sch2.add_student(a2)
sch2.add_student(a3)

sch2.show_students()

sch2.remove_student(0)
print("❌ რომა ქვრივიშვილი წაიშალა სიიდან")
sch2.show_students()
