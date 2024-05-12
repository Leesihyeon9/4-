def calculate_lost_workdays():
    # 손실된 일수
    while True:
        days_lost = input("손실된 일수를 입력하세요: ")
        if not days_lost.isdigit() or int(days_lost) < 0:
            print("올바른 숫자를 입력하세요.")
        else:
            break

    # 시간당 임금
    while True:
        hourly_wage = input("시간당 임금을 입력하세요: ")
        try:
            hourly_wage = float(hourly_wage)
            if hourly_wage < 0:
                print("임금은 음수가 될 수 없습니다.")
            else:
                break
        except ValueError:
            print("올바른 숫자를 입력하세요.")

    # 생산성 감소율
    while True:
        productivity_loss_rate = input("생산성 감소율을 입력하세요 (소수로 표현): ")
        try:
            productivity_loss_rate = float(productivity_loss_rate)
            if productivity_loss_rate < 0 or productivity_loss_rate > 1:
                print("생산성 감소율은 0과 1 사이의 값이어야 합니다.")
            else:
                break
        except ValueError:
            print("올바른 숫자를 입력하세요.")

    # 손실
    total_wage_loss = int(days_lost) * 8 * hourly_wage  # 하루 일하는 시간을 8시간으로 가정
    productivity_loss = total_wage_loss * productivity_loss_rate
    total_loss = total_wage_loss + productivity_loss

    # 결과 출력
    print("총 근로 손실액은 {:.2f} 원입니다.".format(total_loss))

    # 근로 손실 등급


if __name__ == "__main__":
    calculate_lost_workdays()