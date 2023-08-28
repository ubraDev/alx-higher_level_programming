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
  for i in range(list_length):
    try:
      new_list.append(my_list_1[i] / my_list_2[i])
    except (TypeError, ZeroDivisionError):
      new_list.append(0)
  return new_list
