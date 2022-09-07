from __future__ import print_function


import time
import regex as re
import os
import pandas as pd
import numpy as np
import string

import argparse
from datetime import datetime
from natsort import natsorted



datasets = [ 'HDFS'] 

def sort_templates(templates):
    """
    Sort templates by its length. The shorter, the later.

    :param templates: a list of templates
    :return: a sorted list of templates
    """
    return sorted(templates, key=lambda x: len(x), reverse=True)


def get_pattern_from_template(template):
    escaped = re.escape(template)
    spaced_escape = re.sub(r'\\\s+', "\\\s+", escaped)
    return "^" + spaced_escape.replace(r"<\*>", r"(\S+?)") + "$"  # a single <*> can consume multiple tokens


def is_abstrac2(x, y):
    """
    Determine if template_x is more abstract than template_y.

    :param x: a template (str)
    :param y: a template or a message (str)
    self.result = :return: True if x is more abstract (general) than y
    """

    if y is np.NaN:
        return False


    m = re.match(get_pattern_from_template(x), y)
    if m:
        return True
    else:
        return False
    
def is_abstract(x, y):
    """
    Determine if template_x is more abstract than template_y.

    :param x: a template (str)
    :param y: a template or a message (str)
    self.result = :return: True if x is more abstract (general) than y
    """
 
    y2=transform(y)
    x2=transform(x)
    if y2 is np.NaN:

        return False
    x2=x2.lower()
    y2=y2.lower()

    #print("x2",x2)
    #print("y2",y2)
    m = re.match(x2.lower(), y2.lower())
    if m:
        #print("True")
        return True
    else:
        #print("false")
        return False
 
def compare(s1, s2):
        remove = string.punctuation + string.whitespace
        return s1.translate(remove) == s2.translate(remove)
       
def transform(x):

    x1= x.replace('\'', " ")
    x2= x1.replace(',', " ")
    
    
    x2= x2.replace('[', " ")
    x2= x2.replace(']', " ")
    
    x2= x2.replace('"', " ")

    x2= x2.replace(':', " ")
    
    x2= x2.replace('-', " ")
    
    x2= x2.replace('(', " ")
    
    x2= x2.replace(')', " ")
    
    x2= x2.replace('*', " ")
    
    x2= x2.replace('{', " ")
    
    x2= x2.replace('}', " ")
    
    x2= x2.replace('.', " ")

    
    #x2= re.sub('[^A-Za-z0-9\(\)]+ ', ' ', x2) 
    
    x2= x2.lstrip(' ').rstrip(' ')
    
    x2=re.sub(' +', ' ',x2)

    return x2



def common_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-dataset",'--dataset', help="Do the bar option")
    args = parser.parse_args()
    return args


def unique_output_dir(name):
    return os.path.join('{}_result'.format(name))


