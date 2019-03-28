def tribonacci(n):
    if n in (1, 2, 3):
        return 1
    else:
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
    
    
def tallest_player(nba_player_data):
    height_dict = {}
    for player, value in nba_player_data.items():
        ft, inch = value[3].split('-')
        tmp_height = int(ft) * 0.3048 + int(inch) * 0.0254
        height_dict[player] = tmp_height 
    height_max = max(height_dict.values())
    tallest_list = [player  for player in height_dict.keys() if height_dict[player] == height_max]
    return tallest_list


def more_time_position_player(nba_player_data, position):
    if position not in ['F-C', 'C-F', 'C', 'G', 'F', 'G-F', 'F-G']:
        print('Ingrese una posición válida.')
        return
    else:
        time_dict = {}
        for player, value in nba_player_data.items():
            if value[2] == position:
                time_dict[player] = value[1] - value[0] 
        time_max = max(time_dict.values())
        more_time_list = [player for player in time_dict.keys() if time_dict[player] == time_max]
        return more_time_list