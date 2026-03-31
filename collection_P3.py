"""Collections Module Practice #3
A double-ended queue or deque is a linear data structure that allows elements to be inserted and deleted at both ends.

Find out more about it on any documentation site, and then implement a deque from the collections module. The initial elements of the list are provided below.

["London", "Berlin", "Paris", "Madrid", "Rome", "Moscow"]

The list must have the ability to incorporate elements from the left, and be named cities_list."""

from collections import deque

cities_list = deque(["London", "Berlin", "Paris", "Madrid", "Rome", "Moscow"])

# Agregar a la izquierda
cities_list.appendleft("Lisbon")

print(cities_list)