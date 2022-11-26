
import PySimpleGUI as sg
import math
import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler 
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from datetime import date
import sys
  
# Add some color to the window
sg.theme('BlueMono')

layout = [
    [sg.Text('Ticket Symbol', size =(20, 1)), sg.InputText()],
    [sg.Text('Number of Share', size =(20, 1)), sg.InputText()],
    [sg.Text('Distribution Frequency', size =(20, 1)),
    sg.Combo(['Monthly','Quarterly','Annually'],key='period', size=(20, 1))],
    [sg.Text('Holding Period (years)', size =(20, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]

def main():
    window = sg.Window('Dividend Forecast Calculator', layout)
    event, values = window.read()
    window.close() 

    # ticket symbol
    if event == 'Submit':

        # Returns the current local date
        today = date.today()
        ticket = values[0]
        stock = yf.Ticker(ticket)
        
        # Check invalid ticket symbol
        if stock.info['regularMarketPrice'] == None:
            sg.Popup('Ticket Symbol "' + ticket + '" is not listed')
            sys.exit("Ticket Symbol Not Found")
        
        result_table = []

        headings = ['Year', 'Address', 'Phone Number']

        result_layout = [
                [sg.Table(values=result_table, 
                headings=headings, 
                max_col_width=35,
                            auto_size_columns=True,
                            justification='right',
                            key='-TABLE-',
                            row_height=35)]
            ]

        w = sg.Window("Dividend Calculator", result_layout)
        w.read()
        w.close()

    
    else:
        print("Cancel")


if __name__ == "__main__":
    main()