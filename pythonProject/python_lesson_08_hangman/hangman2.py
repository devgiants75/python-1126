import random

word_list = ["apple", "banana", "camel"]
chosen_word = random.choice(word_list)
print(f"테스트 단어 : {chosen_word}")

#TODO-1 비어있는 list인 display를 만드세요.
# chosen_word의 각 문자 개수마다 "_"를 추가하세요. 예를 들어 chosen_word = "apple"이라면,
# display = ['_', '_', '_', '_', '_']이 되어야 합니다. chosen_word가 몇 자로 이루어졌는지 확인하기 위하여
# 5개의 '_'로 구성됩니다.

display = []        # 비어있는 list 선언 방식
for letter in chosen_word:
    display.append("_")

print(display)

#TODO-2 chosen_word의 각 문자들을 반복시키세요.
# 만약 그 위치의 문자가 guess와 일치하면, 그 위치의 display에서 해당 문자를 공개하세요.
# ex) 사용자가 "p"를 입력했고, chosen_word가 "apple"라면 display = ['_', 'p', 'p', '_', '_']로 바뀌어야 합니다.

# 힌트 : list의 각 요소를 재대입하는 방식에 대한
# numbers = [1,2,3,4,5]
# print(numbers)
# numbers[0] = 100
# print(numbers)

guess = input("알파벳 입력 >>> ").lower()
# index 넘버를 예시로 들었다 -> 향상된 for문이 아니라 고전적 for 문(in range())을 사용하라는 의미
for i in range(len(chosen_word)):
    if guess == chosen_word[i]:
        display[i] = guess
    # else는 쓰지 않음 -> 틀렸을 경우에는 변동이 없기 때문에

print(display)