#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Fri 14 09:34:03 2018

@author: MariusD
"""

#Server

from flask import Flask, jsonify 

server = Flask("phonebook")


phonebook={"Mum":"0173240", "Dad":"01717374", "Pepe":"01773849", "IE":"01"}

# Add contact
@server.route("/add_contact/<number>/<name>", methods=["POST"])
def add_contact(number, name): 
    if name not in phonebook: 
        phonebook.update({name:number})
        return jsonify("You added " + name + " the number is: " + number)
    else: 
        return jsonify("The contact " + name + " is already in your phonebook.")

# Get a phone by name
@server.route("/get_number/<name>")
def get_number(name): 
    if name in phonebook: 
        return jsonify(name + "phone number is: " + phonebook[name])
    else: 
        return jsonify("You don't have a contact called " + name + " in your phonebook.")

# Delete a phone by name
@server.route("/delete_contact/<name>", methods=["DELETE"])
def delete_contact(name):   
    if name not in phonebook: 
        return jsonify("You don't have a contact called " + name + " in your phonebook.")
    else:
        del phonebook[name]
        return jsonify("The contact "+ name + " has been deleted from your phonebook.")         

#• update a phone by name                
@server.route("/update_contact/<name>/<phone>", methods=["PUT"])
def update_contact(name, number): 
    if name not in phonebook: 
        return jsonify("You don't have a contact called "+ name + " in your phonebook.")
    else: 
        phonebook[name] = number
        return jsonify("You just updated: " + name + "'s number to: " + number)
    
  
@server.route("/phonebook")
def get_phonebook():
    return jsonify(phonebook)
            
server.run()