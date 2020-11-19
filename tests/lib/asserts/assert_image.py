import os,sys
from pprint import pprint
from diffimg import diff

def assertSameImage(img_expected, img_actual, error_msg='same image is expected but diff image found'):
  ''' exception if different image '''
  assert diff(img_expected, img_actual)==0, error_msg
