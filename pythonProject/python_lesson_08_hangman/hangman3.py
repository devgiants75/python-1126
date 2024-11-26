import random

'''
"".join(반복가능객체) method : "."앞에 있는 문자열을 기준으로 반복가능객체의 요소들을 합쳐서 string 형태로 반환함.
'''
# temp = ["안", "녕", "하", "세", "요"]
# hello = ""
# for letter in temp:
#     hello += letter
# print(hello)
# print("".join(temp))
# print("/".join(temp))

word_list = ["apple", "banana", "camel"]
chosen_word = random.choice(word_list)
print(f"테스트 단어 : {chosen_word}")

display = []

#TODO-1 "_"가 들어간 display 구현하세요.

for letter in chosen_word:
    display.append("_")

print(display)

#TODO-2 사용자가 추측을 반복할 수 있도록 while 반복문을 작성하세요. 사용자가 chosen_word의 모든 문자들을 맞추고
# display에 더이상 빈칸("_")이 없을 때만 반복문이 멈추도록 작성합니다. 반복문 탈출 후 print("정답입니다!!:)")를 출력하세요.

while "_" in display:
    guess = input("알파벳 입력 >>> ").lower()
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
    print(display)

# 위에서 배운 .join() method를 활용하여 display의 각 요소를 string으로 반환하고, 콘솔에 출력하시오.
print(" ".join(display))
print("정답입니다!!:)")