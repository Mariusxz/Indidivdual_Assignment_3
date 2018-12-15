#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 09:38:13 2018

@author: MariusD
"""

# Client

import requests

def add_contact(number, name): 
    request = requests.post('http://127.0.0.1:5000/add_contact/{}/{}'.format(number, name))
    return request.json()

def get_number(name): 
    request = requests.get('http://127.0.0.1:5000/get_number/{}'.format(name))
    return request.json()

def delete_contact(name): 
    request = requests.delete('http://127.0.0.1:5000/delete_contact/{}'.format(name))
    return request.json()

def update_contact(name, number):
    request = requests.put('http://127.0.0.1:5000/update_contact/{}/{}'.format(name, number))
    return request.json()

def get_phonebook(): 
    request = requests.get('http://127.0.0.1:5000/phonebook') 
    return request.json()