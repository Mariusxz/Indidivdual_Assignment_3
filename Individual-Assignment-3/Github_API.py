#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri 14 09:28:43 2018

@author: MariusD
"""

#Exercise 2 - Github-API Exercise

def github_api(username):
    
    import requests
    json_data = requests.get("https://api.github.com/users/" + username + "/repos").json()

    for repo in json_data:
        print("Name: " + repo["name"], 
              "Url: " + repo["html_url"],
              "Language: " + str(repo["language"]), 
              "Stars: " + str(repo["stargazers_count"]),
              "Description: " + str(repo["description"]))
        
github_api("Mariusxz")
