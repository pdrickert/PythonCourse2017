def binarify(num):
  """convert positive integer to base 2"""
def binarify(num):
    if num <= 0: return [0]
    digits = []
    while num:
        digits.append(num % 2)
        num = num / 2
        return ''.join(str(digits[::-1]))

def int_to_base(num, base):
  """convert positive integer to a string in any base"""
  if num<=0:  return '0'
  digits = []
  while num>0:
      digits.insert(0, num % base)
      num = num / base
  return digits

def base_to_int(string, base):
  """take a string-formatted number and its base and return the base-10 integer"""
  if string=="0" or base <= 0 : return 0
  result = 0
  num = len(string)
  for i in string:
    num -= 1
    result += ((base ** num) * int(i))
  return result

def flexibase_add(str1, str2, base1, base2):
  """add two numbers of different bases and return the sum"""
  result=base_to_int(str1, base1) + base_to_int(str2, base2)
  return result

def flexibase_multiply(str1, str2, base1, base2):
  """multiply two numbers of different bases and return the product"""
  result=base_to_int(str1, base1) * base_to_int(str2, base2)
  return result

def romanify(num):
  """given an integer, return the Roman numeral version"""
  if num<5:
    result = "I" * num
  elif num<10:
    result = "V" + ((num-5)*"I")
  elif num < 50:
    result = (num/10 * "X") + (((num % 10)/5) * "V") + (((num % 10)-5) * "I")
  elif num < 100:
    result = (num/50 * "L") + (((num % 50)/10) * "X") + (((num % 50)/5) * "V") + (((num % 10)-5) * "I")
  elif num < 500:
     result = (num/100 * "C")+ (((num % 100)/50) * "L") + ((((num % 100)-50)/10)*"X") + (((num % 10)/5) * "V") + (((num % 10)-5) * "I")
  return result





# Copyright (c) 2014 Matt Dickenson
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
