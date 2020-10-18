#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 16:28:41 2020

@author: qiupiao
"""

import xml.etree.ElementTree as ET
tree = ET.parse('blocklist.xml')
root = tree.getroot()
  
print("Print all the text lines with the “blockID” values that start with the letter “i” or “g”, and end with digits")
print("==================================") 
for item in root.iter():
    a = item.get('blockID')
    b = item.get('id')   
    if a is not None and (a[0] == 'i' or a[0] == 'g') and a[-1].isdigit():        
        print("<emItem blockID=“%s” id=“%s”>"%(a,b))


strlist = ['/','^',r'\\']  
print("Print all the text lines where the “ID” values are email addresses.")
print("==================================")     
for item in root.iter():
    a = item.get('blockID')
    b = item.get('id')
    if b is not None:
        if b[-4:] == '.com' and "@" in b:
            for string in strlist:
                if string not in b:
                    print("<emItem blockID=“%s” id=“%s”>"%(a,b))

        
