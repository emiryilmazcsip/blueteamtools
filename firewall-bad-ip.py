'''
Firwall Rule Blocker
Author: Emir T. Yilmaz
Credits: https://www.youtube.com/watch?time_continue=211&v=7UWFJGeix_E&embeds_referring_euri=https%3A%2F%2Fvideo.search.yahoo.com%2F&embeds_referring_origin=https%3A%2F%2Fvideo.search.yahoo.com&source_ve_path=MjM4NTE

'''

import requests, csv, subprocess

#source=Abuse CH
response = requests.get("https://feodotracker.abuse.ch/downloads/ipblocklist.csv").text

rule="netsh advfirewall firewall delete rule name='BADIP'"
subprocess.run(["Powershell", "-Command", rule])

mycsv = csv.reader(filter(lambda x: not x.startswith("#"), response.splitlines()))
for row in mycsv:
    ip = row[1]
    if (ip)!=("dst_ip"):
        print("Added Rule to block:",ip)
        rule="netsh advfirewall firewall add rule name='BadIP' Dir=Out Action=Block RemoteIP="+ip
        subprocess.run(["Powershell", "-Command", rule])