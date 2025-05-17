import numpy as np

kuji = np.random.rand()

def amidakuji():
    if kuji <= 0.17:
      print("あなたの運勢は「大吉」です")
    elif 0.17 < kuji <= 0.52:
      print("あなたの運勢は「吉」です")
    elif 0.52 < kuji <= 0.57:
      print("あなたの運勢は「半吉」です")
    elif 0.57 < kuji <= 0.61:
      print("あなたの運勢は「小吉」です")
    elif 0.61 < kuji <= 0.64:
      print("あなたの運勢は「末小吉」です")
    elif 0.64 < kuji <= 0.70:
      print("あなたの運勢は「末吉」です")
    else:
      print("あなたの運勢は「凶」です")

amidakuji()