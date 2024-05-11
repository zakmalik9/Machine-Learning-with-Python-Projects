import random

def player(prev_play, opponent_history=[], count=0, player_history=[], player_move_frequency={"RR": 0,"RP": 0,"RS": 0,"PR": 0,"PP": 0,"PS": 0,"SR": 0,"SP": 0,"SS": 0}, count_abbey=0):
  opponent_history.append(prev_play)
  
  player_last_two = ''.join(player_history[-2:])
  if len(player_last_two) == 2:
    player_move_frequency[player_last_two] += 1
  
  guess = random.choice(['R', 'P', 'S'])
  win_move_for = {
    "R":"P",
    "P":"S",
    "S":"R"
  }

  if len(opponent_history) >= 21:
    # countering abbey
    last_guess = player_history[-1]
    potential_plays = [last_guess + "R", last_guess + "P", last_guess + "S"]
    play_frequencies = {}
    play_frequencies = {play:player_move_frequency[play] for play in potential_plays}
    opp_prediction = max(play_frequencies, key=play_frequencies.get)[-1]
    
    opp_play = win_move_for[opp_prediction]
    guess = win_move_for[opp_play]

    # countering quincy
    pattern = []
    if (opponent_history[-5:] == opponent_history[-10:-5]) and (opponent_history[-15:-10] == opponent_history[-20:-15]):
      pattern = opponent_history[-5:]
      opp_play = pattern[count]
      guess = win_move_for[opp_play]
      count += 1
      player_move_frequency["RR"]=0
      player_move_frequency["RP"]=0
      player_move_frequency["RS"]=0
      player_move_frequency["PR"]=0
      player_move_frequency["PP"]=0
      player_move_frequency["PS"]=0
      player_move_frequency["SR"]=0
      player_move_frequency["SP"]=0
      player_move_frequency["SS"]=0
    else:
      # countering kris
      player_counter = [win_move_for[move] for move in player_history[-11:-1]]
      if player_counter == opponent_history[-10:]:
        if player_history[-1] == prev_play:
          guess = win_move_for[win_move_for[prev_play]]
        else:
          guess = prev_play
        player_move_frequency["RR"]=0
        player_move_frequency["RP"]=0
        player_move_frequency["RS"]=0
        player_move_frequency["PR"]=0
        player_move_frequency["PP"]=0
        player_move_frequency["PS"]=0
        player_move_frequency["SR"]=0
        player_move_frequency["SP"]=0
        player_move_frequency["SS"]=0
      else:
        # countering mrugesh
        player_last_twenty_ten = player_history[-21:-11]
        most_frequent1 = max(set(player_last_twenty_ten), key=player_last_twenty_ten.count)
        player_last_ten = player_history[-11:-1]
        most_frequent2 = max(set(player_last_ten), key=player_last_ten.count)
        if (win_move_for[most_frequent1] == opponent_history[-11]) and (win_move_for[most_frequent2] == opponent_history[-1]):
          player_last_ten = player_history[-10:]
          most_frequent = max(set(player_last_ten), key=player_last_ten.count)
          guess = win_move_for[win_move_for[most_frequent]]

  player_history.append(guess)
  return guess
