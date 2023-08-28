#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
  """
  Divides element by element 2 lists.

  Args:
    my_list_1: The first list.
    my_list_2: The second list.
    list_length: The length of the new list.

  Returns:
    A new list (length = list_length) with all divisions.
  """

  new_list = []
  try:
    for i in range(list_length):
      if not isinstance(my_list_1[i], (int, float)) or not isinstance(my_list_2[i], (int, float)):
        print("wrong type")
      elif my_list_2[i] == 0:
        print("division by 0")
      else:
        new_list.append(my_list_1[i] / my_list_2[i])
  except IndexError:
    print("out of range")
  finally:
    return new_list
