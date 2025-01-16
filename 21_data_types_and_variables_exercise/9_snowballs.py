snowballs = int(input())

snowball_value = 0

snow_ball_list = [0,0,0,0]

for ball in range(1, snowballs + 1):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    if snowball_weight < 0 or snowball_weight > 1000:
        continue
    if snowball_time < 1 or snowball_time > 500:
        continue
    if snowball_quality < 0 or snowball_quality > 100:
        continue

    result = int((snowball_weight / snowball_time))
    result **= snowball_quality

    if result > snowball_value:
        snow_ball_list[0] = snowball_weight
        snow_ball_list[1] = snowball_time
        snow_ball_list[2] = result
        snow_ball_list[3] = snowball_quality
        snowball_value = result



print(f'{snow_ball_list[0]} : {snow_ball_list[1]} = {snow_ball_list[2]} ({snow_ball_list[3]})')