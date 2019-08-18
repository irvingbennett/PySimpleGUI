# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 16:31:23 2019

@author: Irving
"""

import PySimpleGUI as sg

layout = [[sg.Text('Filename')],
          [sg.Input(), sg.FileBrowse()], 
      [sg.OK(), sg.Cancel()]] 

window = sg.Window('Get filename example', layout)

event, values = window.Read()