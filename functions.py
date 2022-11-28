#!/usr/bin/python
# -- College_Plan: functions.py

from bs4 import BeautifulSoup
import requests
import csv
import re

from models.lesson import Lesson, LessonType
from models.date import Date
from models.plan import Plan

def _get_from_list(dates : list, date : Date):
    if len(dates) == 0:
        return None
    
    for d in dates:
        if d == date:
            return d
        
    return None


def send_request(URL : str, KEY : str, GROUP : str):
    payload = {KEY : GROUP}
    print('Sending request... ')
    
    r = requests.get(URL, params=payload)
    
    print(f'Status: {r.status_code}')
    
    soup = BeautifulSoup(r.content, 'html5lib')
    return soup

def save_html_to_file(soup : BeautifulSoup, FILE_HTML : str):
    pretty_html = soup.prettify()
    
    print('Writing HTML to file... ', end='')
    
    with open(FILE_HTML, 'w', encoding='utf-8') as f:
        f.write(pretty_html)
        
    print('Done.')

def select_data(soup):
    print('Selecting data... ', end='')
    
    quotes = []
    
    blocks = soup.find('div', attrs={'class' : 'lessons'})
    
    reg = r"^(?P<subject>.*)\((?P<type>.*)\)(?P<place>.*)\[.*$"
    
    for block in blocks:
            quote = {}

            date = list(map(int, block.find('span', attrs={'class' : 'date'}).text.split('_')))

            quote['day']   = date[2]
            quote['month'] = date[1]
            quote['year']  = date[0]
            quote['block_id'] = int(block.find('span', attrs={'class' : 'block_id'}).text[-1:])
            quote['info'] = block.find('span', attrs={'class' : 'info'}).text

            name = block.find('span', attrs={'class' : 'name'}).text

            quote['subject'] = '-'
            quote['type']    = '-'
            quote['place']   = '-'

            result = re.match(reg, name)
            if result:
                quote['place']      = result.group('place')
                quote['subject']    = result.group('subject')

                try:
                    quote['type']       = LessonType(result.group('type'))
                except ValueError:
                    quote['type']       = LessonType('I')

            quotes.append(quote)
    
    for quote in quotes:
        date = Date(day=quote['day'],
                    month=quote['month'], 
                    year=quote['year'],
                    lessons=[])
        
        lesson = Lesson(quote['block_id'],
                        quote['subject'],
                        quote['type'],
                        quote['place'],
                        quote['info'])
        
        d = _get_from_list(Plan.dates, date)
        
        if d is None:
            date.lessons.append(lesson)
            Plan.dates.append(date)
        
        else:
            d.lessons.append(lesson)
   
    print('Done.')

def standarize_data():
    print('Standarizing data... ', end='')
    
    for date in Plan.dates:
        date.standardize()
    
    print('Done.')


def save_data_to_csv_file(FILE_CSV : str):
    
    print('Writing data to CSV file... ', end='')
    
    headers = ['year', 'month', 'day', 'block_id', 'subject', 'type', 'place', 'info']
    
    with open(FILE_CSV, 'w', encoding='utf-8') as f:
        
        writer = csv.writer(f)    
        writer.writerow(headers)

        for date in Plan.dates:
            for lesson in date.lessons:
                row = [date.year, 
                       date.month, 
                       date.day, 
                       lesson.block_id, 
                       lesson.subject, 
                       lesson.type.value, 
                       str(lesson.place), 
                       lesson.info[:-1]]
                
                writer.writerow(row)
            
    print('Done.')