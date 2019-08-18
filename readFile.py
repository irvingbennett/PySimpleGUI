# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 16:34:43 2019

@author: Irving
"""

import PySimpleGUI as sg

event, values = sg.Window('Get filename example', [[sg.Text('Filename')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()] ]).Read()