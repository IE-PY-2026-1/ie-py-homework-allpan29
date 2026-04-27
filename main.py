# 파일이름 : main.py
# 작 성 자 : 60261925 강현민
import random

# 초기 설정
trainer_name = input("반가워요! 당신의 이름은 무엇인가요? ")
print(f"\n환영합니다, {trainer_name} 트레이너님! 박사님이 첫 포켓몬을 준비하셨습니다.")

# 선택 가능한 스타팅 포켓몬 리스트
starters = ["이상해씨", "파이리", "꼬부기"]
print("1. 이상해씨 (풀) | 2. 파이리 (불꽃) | 3. 꼬부기 (물)")

choice = int(input("함께 모험을 떠날 포켓몬의 번호를 선택하세요: ")) - 1
my_pokemon_list = [starters[choice]]  # 내가 가진 포켓몬 리스트
my_pokemon_hp = 100  # 내 포켓몬의 현재 체력
pokedex = [starters[choice]]  # 도감 (발견한 포켓몬)

print(f"\n축하합니다! {my_pokemon_list[0]}(와)과 함께 모험을 시작합니다!")

# 메인 루프
while True:
    print("\n" + "="*30)
    print("메인 메뉴")
    print("1. 내 포켓몬 상태 확인")
    print("2. 야생 포켓몬 배틀 (모험)")
    print("3. 나의 포켓몬 도감 조회")
    print("4. 포켓몬 센터 (회복)")
    print("5. 모험 종료")
    print("="*30)

    menu = input("원하시는 활동의 번호를 입력하세요: ")

    if menu == '1':
        print(f"\n[상태창] 트레이너: {trainer_name}")
        print(f"대표 포켓몬: {my_pokemon_list[0]} (HP: {my_pokemon_hp}/100)")

    elif menu == '2':
        wild_pokemons = ["피카츄", "구구", "꼬렛", "캐터피"]
        wild_one = random.choice(wild_pokemons)
        print(f"\n앗! 야생의 {wild_one}(이)가 나타났다!")
        
        # 도감에 없으면 추가
        if wild_one not in pokedex:
            pokedex.append(wild_one)
            print(f"(신규 포켓몬 {wild_one}의 데이터를 도감에 등록했습니다!)")
        
        action = input("1. 싸운다 | 2. 도망친다 : ")
        if action == '1':
            damage = random.randint(10, 30)
            my_pokemon_hp -= damage
            print(f"승리했다! 하지만 {my_pokemon_list[0]}의 HP가 {damage}만큼 감소했다.")
        else:
            print("무사히 도망쳤다.")

    elif menu == '3':
        print("\n--- 나의 포켓몬 도감 ---")
        for i, p in enumerate(pokedex, 1):
            print(f"{i}. {p}")

    elif menu == '4':
        print("\n포켓몬 센터에 방문했습니다. 간호순 누나가 포켓몬을 치료해줍니다.")
        my_pokemon_hp = 100
        print(f"{my_pokemon_list[0]}의 체력이 모두 회복되었습니다!")

    elif menu == '5':
        print(f"\n{trainer_name}님, 오늘의 모험을 종료합니다. 다음에 또 만나요!")
        break

    else:
        print("\n잘못된 입력입니다. 1~5번 사이의 숫자를 입력해 주세요.")
