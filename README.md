# Technical Question

Using the most efficient Redis Data Type:

  * Insert 100 random (not predictable) values
  * Read and print the values in reverse insertion order

Note: It is acceptable to delete the values while retrieving them.
Explain why it is the most efficient Redis Data Type for this task.


# Answer to above question
Because the question is asking to have random (not predictable) values printed in reverse insertion order, a Redis [list](https://redis.io/docs/latest/develop/data-types/lists/) implemented as a stack (first in, last out) is the most efficient Redis Data Type for this exercise. This preserves the insertion order, so grabbing the last (or tail) inserted value is quick and easy. It's performed in constant time.