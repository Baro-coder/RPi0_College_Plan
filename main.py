#!/usr/bin/python
# -- College_Plan: main.py --

import sys
import configparser as cfgp

import functions as func

APP_DIR = '/home/pi/.Private/RPi0_College_Plan'
CONFIG_FILE = f'{APP_DIR}/config.ini'

def config_init():
    try:
        config = cfgp.ConfigParser()

        config.read(CONFIG_FILE)
        
        # Web
        global URL, KEY, GROUP
        
        URL = config['Web']['url']
        KEY = config['Web']['key']
        GROUP = config['Web']['group']
        
        # Paths
        global FILE_HTML, FILE_CSV, FILE_ERR
        
        FILE_HTML = f"{APP_DIR}/{config['Paths']['file_html']}"
        FILE_CSV  = f"{APP_DIR}/{config['Paths']['file_csv']}"
        FILE_ERR  = f"{APP_DIR}/{config['Paths']['file_err']}"
    
    except KeyError as e:
        sys.stderr.write('-- Config Key Error --')
        sys.stderr.write(str(e))
        sys.exit(1)
    
    except Exception as e:
        sys.stderr.write('-- Unexpected Error Config --')
        sys.stderr.write(str(type(e)))
        sys.stderr.write(str(e))
        sys.exit(1)


def main():
    # -- Config
    print('Reading config... ', end='')
    config_init()
    print('Done.')
    
    try:
        # get HTML source
        soup = func.send_request(URL, KEY, GROUP)

        # save HTML source code to file
        func.save_html_to_file(soup, FILE_HTML)

        # parse html document and select data
        func.select_data(soup)

        # standardize data and pack into class
        func.standarize_data()
        
        # save data to csv file
        func.save_data_to_csv_file(FILE_CSV)
    
    except Exception as e:
        sys.stderr.write('-- Unexpected Error --')
        sys.stderr.write(str(type(e)))
        sys.stderr.write(str(e))
        sys.exit(1)
        

if __name__ == '__main__':
    main()
    sys.exit(0)