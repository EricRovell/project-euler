"""
Problem #034: Digit factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

# returns all possible factorions
def factorions():
  factorial_digits = []

  factorials = {'0': 1, '1': 1, '2': 2, '3': 6, '4': 24, '5': 120,
                '6': 720, '7': 5040, '8': 40320, '9': 362880}
  
  # there is no 8-digit number which can be sum of the factorials of it's digits
  # because 8 * 9! = 2 903 040 is a 7-digit number
  limit = 7 * factorials['9']

  for number in range(2, limit):
    total = 0
    for digit in str(number):
      total += factorials[digit]
    if number == total:
      factorial_digits.append(number)

  return factorial_digits

# tests
print(factorions())