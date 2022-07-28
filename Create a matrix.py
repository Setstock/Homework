#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 15:49:33 2022

@author: patcharee
"""

import numpy as np
M = np.array ([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print (M[2,:])               # แสดงทุกค่าในเมตริกซ์ ที่แถวเท่ากับ 2
#answer 7 8 9    
print(M[2:])                 ## แสดงทุกค่าในเมตริกซ์ ที่แถวเท่ากับ 2 เป็นต้นไป
#answer 7 8 9 10 11 12
