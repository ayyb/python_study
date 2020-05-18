import keyword
print("TEST file 입니다.")
print("Hello Coding Python")
print("hello" * 3)
print("Python Programming")

print(keyword.kwlist)  # 주석처리

print()  # 줄바꿈하기.
print("안녕하세요", "저의", "이름은", "이명섭입니다.")

print(type("안녕하세요"))

print(type(273))
print('"안녕하세요"라고 말했습니다')

print("안녕하세요\n 안녕하세요")
print("안녕하세요\t안녕하세요")

print("""동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산 대한사람
대한으로 길이 보전하세""")

print(3 * "안녕하세요")


number = 100
number += 10
number += 20
number += 30
print("number:", number)

string = "안녕하세요"
string += "!"
string += "!"
print("string:", string)

input("인사말을 입력하세요>")

string = input("인사말을 입력하세요>")
print(string)

number = input("숫자를 입력하세요 >")
print(number)


a = "10 20 30 40 50 60".split(" ")
print(a)
