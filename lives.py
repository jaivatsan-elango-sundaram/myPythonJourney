currentLife = 0
def hang_stages():
    if currentLife == 1:
        print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========
          ''')
    elif currentLife == 2:
        print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
              ''')
    elif currentLife == 3:
        print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
              ''')
    elif currentLife == 4:
        print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
              ''')
    elif currentLife == 5:
        print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
              ''')
    elif currentLife == 6:
        print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
              ''')