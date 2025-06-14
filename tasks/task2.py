import random

def get_number_ticket(min, max, quantity):
  if quantity > max - min:  
    return []
  else:
    num_set_tpm = set()

    for _ in range(quantity):
      num_set_tpm.add(random.randint(min, max))

    output_num_array = sorted(list(num_set_tpm))
    return output_num_array

print(get_number_ticket(1, 10, 4))


def get_number_ticket_short(min, max, quantity):
  return [] if quantity > max - min else sorted(list(set(random.randint(min, max) for _ in range (quantity))))

print(get_number_ticket_short(1, 10, 4))