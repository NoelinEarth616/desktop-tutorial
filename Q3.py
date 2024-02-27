import itertools

def find_ball_combinations(total_sought, ball_count=10):
    combinations = list(itertools.combinations(range(1, ball_count + 1), 2))
    
    print("Ball Lottery\n")
    print(f"Total sought: {total_sought}")

    for index, combination in enumerate(combinations, start=1):
        ball1, ball2 = combination
        current_total = ball1 + ball2
        print(f"Result of picks {index} and {index + 1} : {ball1} + {ball2}")

        if current_total == total_sought:
            print(f"You got your total in {index} picks!")
            break

    else:
        print(f"Sorry, you didn't get the total {total_sought} with the given picks.")
