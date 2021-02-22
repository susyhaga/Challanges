import pytest
from adjacent_nodes import adjacency_matrix

a= [
    [ 0, 1, 0, 0 ],
    [ 1, 0, 1, 1 ],
    [ 0, 1, 0, 1 ],
    [ 0, 1, 1, 0 ]
    ]

rows=len(a)
columns=len(a[0])

class Testing:
  def adjacent(self):
    assert adjacency_matrix(a, 0, 1, rows, columns) == True

  def adjacent_nodes_test_true(self):
    assert adjacency_matrix(a, 1, 2, rows, columns) == True

  def adjacent_nodes_test_false(self):
    assert adjacency_matrix(a, 3, 0, rows, columns) == False 

  def tadjacent_nodes_test_false(self):
    assert adjacency_matrix(a, 2, 2, rows, columns) == False




