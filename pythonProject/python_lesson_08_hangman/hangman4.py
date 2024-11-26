import random       # 어떤 모듈을 가지고 왔는지 맨 처음에 명시해주는 편

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["apple", "banana", "camel"]
chosen_word = random.choice(word_list)
print(f"테스트 단어 : {chosen_word}")
display = []
for _ in chosen_word:
    display.append("_")
print(display)

end_of_game = False

#TODO-1 남은 목숨 수를 추적하기 위한 'lives'라는 변수를 선언하고, 6으로 초기화하세요.
lives = 6


#TODO-3 display list의 모든 요소를 결합하여 문자열로 변환하세요.

#TODO-4 사용자가 모든 문자를 맞췄는지 확인하세요 -> 정답을 맞췄다면 "정답입니다!!:)"를 출력하세요

while not end_of_game:
# while True:
    guess = input("알파벳 입력 >>> ").lower()
    # TODO-2 추측한 알파벳이 chosen_word에 없으면 lives를 1 감소시키세요.
    #  lives가 0이 되면 "모든 기회를 잃었습니다."를 출력하고 게임을 끝내세요.

    #추측한 알파벳을 확인하는 코드
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        # 추측한 알파벳이 맞다면 사용될 조건문
        if guess == letter:
            display[i] = letter     # guess로 쓰셔도 상관없습니다.
        # 틀렸을 때 사용될 조건문     -> 이대로 하면 틀리는 예시
        # elif letter != guess:
        #     lives -= 1
        #     print(f"당신의 기회는 {lives}번 남았습니다.")
        #     if lives == 0:
        #         print("모든 기회를 잃었습니다.")
        #         end_of_game = True
        # 라고 작성하시면 안됩니다. -> 알파벳 하나 입력할 때마다 모든 단어에서 알파벳이 맞는지 아닌지 확인하는 조건문이 실행되기 때문.
        # 즉, 반복문 내부에 조건문이 있기 때문에 guess를 한 번만 입력하고도 lives가 여러번 -=1이 이루어지게 됨.

    # 이상을 이유로 for문 바깥에서 guess가 chosen_word에 속하지 않는 지를 확인하는 조건문을 작성해야 함.
    if guess not in chosen_word:    # 여기서는 letter라는 변수를 선언할 수 없다 -> letter는 반복문 내부에서 정의된 것이기 때문
        lives -= 1
        print(f"당신의 기회는 {lives}번 남았습니다.")
        # lives가 감소하고 있는 중에 만약에 0번이 되었다면 while 반복문이 끝나면서 game over가 돼야 함.
        if lives == 0:
            print("모든 기회를 잃었습니다.")
            print(f"정답은 {chosen_word} 입니다.")
            # while 반복문을 탈출 하는 방법 #1    -> lives==0
            end_of_game = True
            # while 반복문을 탈출 하는 방법 #2    -> lives==0
            # break
    print(stages[lives])
    print(display)
    print(" ".join(display))










