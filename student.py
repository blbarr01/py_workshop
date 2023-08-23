class Student:
    def __init__(self, sid, name, es):
        self.name = name 
        self.sid = sid
        self.enrollment_status = es

    def salute(self):
        print(f"hello my name is {self.name}")

    def __repr__(self) -> str:
        return f"{self.name}\n{self.sid}\n{self.enrollment_status}"


# code only executes if file is ran as a script 
# does not exist if imported as a module
if __name__ == "__main__": 
    s1 = Student(123, "jim", True) 
    print(s1)
    s1.salute() 
