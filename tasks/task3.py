import re

def normalize_phone(phone_number):
  formatted_number = re.sub(r'[^\d+]', '', phone_number)

  if formatted_number.startswith('+380'):
    return formatted_number
  elif formatted_number.startswith('380'):
    return '+' + formatted_number
  else: 
    return '+38' + formatted_number




phone_numbers_array = ["    +38(050)123-32-34", "     0503451234", "(050)8889900", "38050-111-22-22", "38050 111 22 11   "]

for phone_number in phone_numbers_array: 
  print(normalize_phone(phone_number))

print('*' * 20)

def normalize_phone_short(phone_number):
  return '+38' + re.sub(r'^(?:\D*38|\D*)|[\D]', '', phone_number)



for phone_number in phone_numbers_array: 
  print(normalize_phone_short(phone_number))
