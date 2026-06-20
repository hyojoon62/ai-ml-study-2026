# 변수
name = "Kim"
age = 23

# 자료형
a = 10 # int
b = 3.14 # float
c = "hello" # str
d = True
e = False # boolean
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# 리스트 : 여러 개의 데이터를 저장
fruits = ["apple", "banana", "orange"]
# 접근
print(fruits[0])
# 추가
fruits.append("grape")

# 딕셔너리 : key -> value 저장
student = {
    "name": "Kim",
    "age": 23,
    "major": "DataScience"
}
# 조회
print(student["name"])
# AI 에서
{
    "input_ids": ...,
    "attention_mask": ...
}

# 함수 : 반복되는 코드를 묶음
def greet(name):
    print("Hello", name)
greet("Kim")

# 클래스 : 설계도 라고 생각하면 됨
class Dog:
    def bark(self):
        print("멍멍")
# 객체 생성
dog = Dog()
dog.bark()


class Student:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def introduce(self):
        print(f"안녕하세요. {self.name}입니다.")
        print(f"제 체력은 {self.hp}입니다.")

student = Student("효준", 100)
student.introduce()
