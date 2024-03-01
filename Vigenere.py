legend = dict()

legend = {
  'a': 0,
  'b': 1,
  'c': 2,
  'd': 3,
  'e': 4,
  'f': 5,
  'g': 6,
  'h': 7,
  'i': 8,
  'j': 9,
  'k': 10,
  'l': 11,
  'm': 12,
  'n': 13,
  'o': 14,
  'p': 15,
  'q': 16,
  'r': 17,
  's': 18,
  't': 19,
  'u': 20,
  'v': 21,
  'w': 22,
  'x': 23,
  'y': 24,
  'z': 25,
  0: 'a',
  1: 'b',
  2: 'c',
  3: 'd',
  4: 'e',
  5: 'f',
  6: 'g',
  7: 'h',
  8: 'i',
  9: 'j',
  10: 'k',
  11: 'l',
  12: 'm',
  13: 'n',
  14: 'o',
  15: 'p',
  16: 'q',
  17: 'r',
  18: 's',
  19: 't',
  20: 'u',
  21: 'v',
  22: 'w',
  23: 'x',
  24: 'y',
  25: 'z',
}

def encrypt(plain_text: str, key: str):
  cipher_text = str()
  key_ind = 0

  plain_text = plain_text.lower()
  key = key.lower()

  for i in plain_text:
    if i.isalpha():
      new_val = (legend[i] + legend[key[key_ind]]) % 26
      
      # move to next character in key, and handle reaching the end of the key string
      key_ind += 1
      if key_ind >= len(key):
        key_ind = 0

      cipher_text += legend[new_val]
    else:
      cipher_text += i

  return cipher_text

def decrypt(cipher_text: str, key: str):
  plain_text = str()
  key_ind = 0

  cipher_text = cipher_text.lower()
  key = key.lower()

  for i in cipher_text:
    if i.isalpha():
      new_val = (legend[i] - legend[key[key_ind]]) % 26
      
      # move to next character in key, and handle reaching the end of the key string
      key_ind += 1
      if key_ind >= len(key):
        key_ind = 0

      plain_text += legend[new_val]
    else:
      plain_text += i

  return plain_text