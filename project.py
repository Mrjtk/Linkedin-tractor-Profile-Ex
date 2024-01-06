#
import csv
import requests
import json
import re
from time import sleep
role="Php Developer"          #input("Enter role : ")
location="Delhi"        #input('Enter location : ')
degree=""           #input('Enter degree type: ')
language=""                   #input("Enter programing language required : ")
d='''"'''

f=("url.csv","w+")

def google_scrap1():
                dork=(f'''{d}{role}{d} {d}{location}{d} intext:"open to work" -intitle:"profiles" -inurl:"dir/ " site:in.linkedin.com/in/ OR site:in.linkedin.com/pub/ {degree} OR degree OR licence''')
                search_query = dork
                api_key = 'AIzaSyD0vDJBklNDiXDBUDJgz1axe1Y90rgUGtE'
                search_id='052b22c14536c4b19'
                url = 'https://www.googleapis.com/customsearch/v1'
                start_index=1
                num_results = 100
                all_results=[]
                while start_index<=num_results:
                                params={
                                    'q': search_query,
                                    'key': api_key,
                                    'cx': search_id,
                                    'num':min(10,num_results-start_index+1),
                                    'start':start_index,
                                    'cr': 'countryIN', 
                                    'gl': 'IN'  
                                }

                                response=requests.get(url,params=params)
                                results=response.json()

                                try:
                                    for item in results['items']:
                                            all_results.append(item['link'])
                                except:
                                    pass
                                start_index+=10
                f=open('googleresult.csv','w+')
                j=csv.writer(f)

                for link in all_results:
                        if link.startswith("https://in.linkedin.com" or "https://linkedin.com"):
                                                                                   j.writerow([link])
                        else:
                            pass
                        print("-> ",link)
                

def google_cvs():
                dork=(f'''(intitle:cv OR inurl:cv) -job -jobs -sample -samples -example -examples {d}{role}{d}''')
                search_query = dork
                api_key = 'AIzaSyD0vDJBklNDiXDBUDJgz1axe1Y90rgUGtE'
                search_id='052b22c14536c4b19'
                url = 'https://www.googleapis.com/customsearch/v1'
                start_index=1
                num_results = 100
                all_results=[]
                while start_index<=num_results:
                                params={
                                    'q': search_query,
                                    'key': api_key,
                                    'cx': search_id,
                                    'num':min(10,num_results-start_index+1),
                                    'start':start_index,
                                    'cr': 'countryIN', 
                                    'gl': 'IN'  
                                }

                                response=requests.get(url,params=params)
                                results=response.json()

                                try:
                                    for item in results['items']:
                                            all_results.append(item['link'])
                                except:
                                    pass
                                start_index+=10
                f=open('googleresult2.csv','w+')
                j=csv.writer(f)
                for link in all_results:
                        j.writerow([link])
                        sleep(0.5)
                        print("-> ",link)
                


def google_github():
                 f=("googleCV.csv","w+")
                 base_url = "https://api.github.com/search/users"
                 params = {
                   'q': f'location:{location} {role}',
                   'language': language,
                   'repos': '>5',
                 }

                 response = requests.get(base_url, params=params)

                 if response.status_code == 200:
                        a=[]
                        data = response.json()
                        for item in data.get('items', []):
                            print(f"-> {item['html_url']}")
                            b={item['html_url']}
                            a.append(b)
                 else:
                        print(f"{response.status_code}")
                 f=open("googlegithub.csv",'w+')
                 j=csv.writer(f)
                 j.writerows(a)
                 f.close()





google_github()

google_cvs()

google_scrap1()
