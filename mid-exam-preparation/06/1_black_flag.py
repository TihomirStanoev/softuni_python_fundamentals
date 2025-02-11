def calculate_plunder(total_plundes, expect_plunder):
    if total_plundes >= expect_plunder:
        return f'{total_plundes:.2f}', True
    else:
        precentage_plunder = (total_plundes / expect_plunder) * 100
        return f'{precentage_plunder:.2f}', False



def black_flag(days, plunder):

    total_plunder = 0
    for day in range(1, days+1):
        total_plunder += plunder
        if day % 3 == 0:
            total_plunder += plunder * 0.5

        if day % 5 == 0:
            total_plunder -= total_plunder * 0.30

    return total_plunder



days_of_plunder = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

collected_plunder = black_flag(days_of_plunder, daily_plunder)
plunder_gained, is_target = calculate_plunder(collected_plunder, expected_plunder)

if is_target:
    print(f"Ahoy! {plunder_gained} plunder gained.")
else:
    print(f"Collected only {plunder_gained}% of the plunder.")
