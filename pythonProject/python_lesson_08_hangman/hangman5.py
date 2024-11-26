import random
import hangman_word_list        # 외부의 파이썬 파일(.py)을 참조하는 방법
import hangman_art
'''
지시 사항

1. text to ascii art 사이트에서 hangman 로고를 하나 만드시오.
2. 해당 로고를 hangman_art.py 파일에 logo라는 변수명으로 저장하시오. -> 복수 line에 해당하는 데이터 저장하는 방법 생각해야 함.
3. import 문을 이용하여 hangman_art.py 파일을 참조하고, hangman5.py에서 print()문을 사용하여 콘솔에
    해당 로고를 출력할 수 있도록 코드를 작성하시오. 작성 위치는 -> chosen_word 위에.
'''

print(hangman_art.logo)
# random.choice()의 경우에는 -> 모듈명.메서드명() / hangaman_word_list.word_list -> 모듈명.변수명 : 소괄호유무밖에 없음
chosen_word = random.choice(hangman_word_list.word_list)
print(f"테스트 단어 : {chosen_word}")

# hangman4에서 필요한 코드들을 다 긁어와서 hangman5에 편집하시오.

display = []
for _ in chosen_word:
    display.append("_")
print(display)
# 변수 선언 부분
end_of_game = False
lives = 6

while not end_of_game:
    guess = input("알파벳 입력 >>> ").lower()

    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if guess == letter:
            display[i] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"당신의 기회는 {lives}번 남았습니다.")
        if lives == 0:
            print("모든 기회를 잃었습니다.")
            print(f"정답은 {chosen_word} 입니다.")
            end_of_game = True

    # .join(display)를 활용한 풀이    -> end_of_game = True로 썼을 때 변수 전환이 빨라 while문이 먼저 종료됨
    # if "".join(display) == chosen_word:
    #     print("정답입니다!!:)")
    #     break

    # '_'이 diplay에 없으면 정답임을 활용한 풀이
    if "_" not in display:
        print("정답입니다.")
        # end_of_game = True
        break

    # 정답을 맞췄을 때 while 반복문을 탈출하는 코드를 작성하시오.

    print(hangman_art.stages[lives])
    print(display)
    print(" ".join(display))



