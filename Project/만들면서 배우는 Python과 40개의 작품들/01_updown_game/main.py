import random

random_number = random.randint(1,100)

# print(random_number)

game_count = 0
print(" Up & Down 게임 시작 !! ")
print(" { 1~100 사이의 숫자를 입력하세요. } ")
while True:
    try:
        my_number = int(input(f"({game_count} 번째) 입력 : "))

        if my_number > random_number:
            print("Down !!")
        elif my_number < random_number:
            print("Up !!")
        else:
            print(f"축하합니다! 당신은 {game_count}번만에 맞췄습니다.")
            break
        game_count += 1
    except:
        print("숫자를 입력해주세요.")