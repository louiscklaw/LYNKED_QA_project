import os,sys
from pprint import pprint
from diffimg import diff

HELLOWORLD_A_PNG='tests/self_test/helloworld_a.png'
HELLOWORLD_B_PNG='tests/self_test/helloworld_b.png'

def test_hello_diffimg():
  assert diff(HELLOWORLD_A_PNG, HELLOWORLD_A_PNG)==0, 'same image output not correct'
  assert diff(HELLOWORLD_A_PNG, HELLOWORLD_B_PNG)!=0, 'diff image output not correct'
