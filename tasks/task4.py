from datetime import datetime, timedelta
from task1 import get_days_from_today, get_date

BASE_FORMAT = '%Y.%m.%d'
BLACKLIST_DAYS = [{"name": "Saturday", "shift_days": 2}, {"name": "Sunday", "shift_days": 1}]

def get_upcoming_birthdays(users):
  output_users_array = []
  for user in users:
    output_users_array.append({"name": user["name"], "congratulations_date": get_congratulation_date(user["birthday"])})
      
  return output_users_array 

def get_congratulation_date(date):
  current_year = datetime.now().year
  current_year_birthdate = f"{current_year}{date[4:]}"
  is_birthdate_passed = False if get_days_from_today(current_year_birthdate, BASE_FORMAT) < 0 else True

  if is_birthdate_passed: 
    next_year_birthdate = f"{current_year + 1}{date[4:]}"
    return get_congratulation_date_helper( next_year_birthdate)
  else:
    return get_congratulation_date_helper(current_year_birthdate)

def get_congratulation_date_helper(congratulation_date_str):
  congratulation_date = get_date(congratulation_date_str, BASE_FORMAT)

  is_in_black_list = get_is_in_black_list(congratulation_date)

  if is_in_black_list:
    congratulation_date = move_to_monday(congratulation_date)
  
  return congratulation_date.strftime(BASE_FORMAT)


def get_is_in_black_list(date):
  day_name = get_day_name(date)
  is_in_black_list = False
  for day_obj in BLACKLIST_DAYS:
    if day_obj['name'] == day_name:
      is_in_black_list = True
  
  return is_in_black_list


def get_day_name(date):
  return date.strftime('%A')


def move_to_monday(date):
  day_name = get_day_name(date)
  shifted_days_amount = 0
  for day_obj in BLACKLIST_DAYS:
    if day_obj['name'] == day_name:
      shifted_days_amount = day_obj['shift_days']
  return date + timedelta(days=shifted_days_amount)

users = [
    {"name": "John Doe", "birthday": "1985.01.25"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Test Name", "birthday": "1980.07.27"}
]

print(get_upcoming_birthdays(users))