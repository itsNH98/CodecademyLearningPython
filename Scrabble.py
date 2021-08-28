letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {letter:point for letter, point in zip(letters, points)}
# print(letter_to_points)
letter_to_points[" "] = 0

def score_word(word):
  point_total = 0
  for letter in word:
    # print(letter)
    add = letter_to_points.get(str(letter.upper()), 0)
    # print(add)
    point_total += add
  return point_total
# print(score_word("Rockstar"))

brownie_points = score_word('Brownie')
# print(brownie_points)

player_to_words = {"player1": ["blue", "tennis", "exit"],"wordNerd": ["earth", "eyes", "machine"],"Lexi Con": ["eraser", "belly", "husky"],"Prof Reader": ["zap", "coma", "period"]}

player_to_points = {}

for item in player_to_words.items():
  player_points = 0
  player = item[0]
  words = item[1] 
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points
print(player_to_points)