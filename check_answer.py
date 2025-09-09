WEIGHTS = [2, 7, 6, 5, 4, 3, 2]
def get_valid_nric():
  while True:
    user_nric = input("Enter NRIC: ")
    user_nric = user_nric.upper()
    if len(user_nric) != 9:
      print('NRIC must be 9 characters long.')
    elif user_nric[0] not in ['S','T','F','G']:
      print('Invalid starting letter.')  
    elif not user_nric[8].isalpha():
      print('Last character of NRIC must be a letter.')
    elif not user_nric[1:8].isdigit():
      print('Middle 7 characters must be digits.')
    else:
      return user_nric
    #   break

nric = get_valid_nric()


def calculate_weighted_sum(user_nric):
  digits = nric[1:8] 
  total = 0
  for i in range(7):
        total += int(digits[i]) * WEIGHTS[i]
  if user_nric[0] in ['T','G']:
    total += 4

  return total

