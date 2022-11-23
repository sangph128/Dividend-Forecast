
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

    # Returns the current local date
    today = date.today()
    print("Today date is: ", today)

if __name__ == "__main__":
    main()