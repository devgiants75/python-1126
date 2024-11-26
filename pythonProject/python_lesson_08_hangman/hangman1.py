import random
# word_list 내부의 요소들 중 하나를 임의로 선택하기 위해 외부 모듈인 random을 도입
'''
python_lesson_08_hangman -> hangman1.py

사용 예시
'''
# number_list = [1, 2, 3, 4, 5]
# random_number = random.choice(number_list)  # 모듈명.메서드명()
# print(random_number)
'''
random.choice(객체) method는 list 내에서 임의로 요소 하나를 추출하는 방법이다.
.append()와 같은 형식으로 호출 -> 차이점이 있다면 외부의 module에서 import를 해와서 해당 메서드를 사용함.
'''

word_list = ["apple", "banana", "camel"]
#TODO-1 word_list에서 단어 하나를 임의적으로 선택하고, 해당 단어를 chosen_word라는 변수에 담으세요.
chosen_word = random.choice(word_list)
print(chosen_word)
#TODO-2 유저에게 알파벳을 하나 추측해서 입력하라고 요청하고, 이를 guess 변수에 담으세요.
# 그리고 대문자로 입력하는 경우를 방지하기 위해 input함수 뒤에 .lower()를 적용하세요.
guess = input("알파벳 입력 >>> ").lower()   # .lower() : string의 메서드 중 하나로 대/소문자로 입력하더라도 결과값은 소문자로 출력
#TODO-3 guess에서 입력한 문자 하나가 chosen_word의 string 중 문자 하나와 일치하는지를
# 반복문을 통해 확인할 수 있도록 프로그램을 구현하세요.

# 고전적 for문을 통한 풀이
# for i in range(len(chosen_word)):
#     if guess == chosen_word[i]:
#         print("정답")
#     else:
#         print("오답")

# 향상된 for문을 통한 풀이
for letter in chosen_word:
    if guess == letter:
        print("정답")
    else:
        print("오답")

# 고전적 for문에서의 chosen_word[i]와 letter가 동일하다는 점을 인지해야 함.
'''
만약에 임의로 선택한 단어가 apple이고, guess에 a가 대입됐다면,
실행 예
알파벳 입력 >>> a
정답
오답
오답
오답
오답

으로 출력되어야 함.
'''