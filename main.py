# police_detective_game.py

def intro():
    print("=== 경찰 탐정 게임 ===")
    print("당신은 한 도시의 경찰 탐정입니다.")
    print("최근 발생한 살인사건을 해결해야 합니다.\n")

def scene_crime_scene(clues):
    print(">> 범죄 현장에 도착했습니다.")
    print("단서를 조사하세요.")
    clues.append("발견된 지문")
    clues.append("깨진 유리 조각")
    print("단서: 발견된 지문, 깨진 유리 조각을 얻었습니다.\n")

def scene_interview_suspect(clues):
    print(">> 용의자를 인터뷰합니다.")
    print("용의자가 알리바이를 주장합니다.")
    alibi = input("용의자의 알리바이가 믿을 만한가요? (y/n): ").strip().lower()
    if alibi == 'y':
        clues.append("용의자 알리바이 확인")
        print("알리바이를 확인했습니다.\n")
    else:
        clues.append("용의자 알리바이 거짓")
        print("용의자의 알리바이가 거짓일 수 있습니다.\n")

def final_guess(clues):
    print(">> 이제 범인을 추리할 시간입니다.")
    guess = input("범인이 누구라고 생각하나요? (용의자/모름): ").strip()
    if guess == "용의자" and "용의자 알리바이 거짓" in clues:
        print("정답입니다! 용의자가 범인입니다.")
    else:
        print("추리가 틀렸습니다. 범인을 놓쳤습니다.")

def main():
    clues = []
    intro()
    scene_crime_scene(clues)
    scene_interview_suspect(clues)
    final_guess(clues)
    print("\n게임 종료 감사합니다.")

if __name__ == "__main__":
    main()
