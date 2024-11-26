import random
from hangman_word_list import word_list
from hangman_art import logo, stages

'''
함수 수업을 들어가기 위한 사전 예제

def turn_right():
    turn_left()
    turn_left()
    turn_left()
'''

def play_hangman():
    print(logo)
    chosen_word = random.choice(word_list)
    # print(f"테스트 단어 : {chosen_word}")

    display = []
    for _ in chosen_word:
        display.append("_")
    # print(display)
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

        if "_" not in display:
            print("정답입니다.")
            # end_of_game = True
            break

        print(stages[lives])
        print(" ".join(display))

play_hangman()      # 함수 호출