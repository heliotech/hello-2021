#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Brand new source file in new repository """
import numpy as np
from khutils import printhead

title = "start"

def main():
  printhead(title, xline=True)
  
  resolution = 2000
  x = np.linspace(0, 10, resolution)
  y = x **2
  
  
if __name__ = "__main__":
  main()
