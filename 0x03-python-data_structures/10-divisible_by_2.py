#!/usr/bin/python3
  if not my_list:
      return []

  new_list = [element % 2 == 0 for element in my_list]

  return new_list
