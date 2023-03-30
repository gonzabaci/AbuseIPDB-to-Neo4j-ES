import requests
import json
import csv
import sys
import os
from datetime import datetime

if (len(sys.argv) < 2):
    file_path = str(os.path.join(os.path.dirname(__file__), 'in.txt'))
else:
    file_path = sys.argv[1]

ip = []

with open(file_path, 'r') as input_file:
    for line in input_file:
        ip.append(line.strip())

API_KEY = 'xxxxxxxxxxx'
url = 'https://api.abuseipdb.com/api/v2/reports'

headers = {
    'Accept': 'application/json',
    'Key': API_KEY
}

#https://www.abuseipdb.com/categories
categories_ref = {
    1: "DNS Compromise",
    2: "DNS Poisoning",
    3: "Fraud Orders",
    4: "DDoS Attack",
    5: "FTP Brute-Force",
    6: "Ping of Death",
    7: "Phishing",
    8: "Fraud VoIP",
    9: "Open Proxy",
    10: "Web Spam",
    11: "Email Spam",
    12: "Blog Spam",
    13: "VPN IP",
    14: "Port Scan",
    15: "Hacking",
    16: "SQL Injection",
    17: "Spoofing",
    18: "Brute-Force",
    19: "Bad Web Bot",
    20: "Exploited Host",
    21: "Web App Attack",
    22: "SSH",
    23: "IoT Targeted"
}

counter = 0
outputs = []
for i in ip:
    counter += 1
    print(f"Processing IP {counter} of {len(ip)}")
    querystring = {
        'ipAddress': i,
        'maxAgeInDays': 90,
        'page': 1,
        'perPage': 1
    }

    response = requests.request(method='GET', url=url, headers=headers, params=querystring)
    
    if response.status_code == 429:
        print('The Response to your request returned a 429 Status Code, your Daily Request Limit was likely reached.')
    
    decodedResponse = json.loads(response.text)
    IP = i

    result_payload = decodedResponse["data"]["results"]

    if (len(result_payload) == 0):
        continue

    result_data = result_payload[0]
    last_reported_at = result_data["reportedAt"]

    res = datetime.strptime(last_reported_at, '%Y-%m-%dT%H:%M:%S%z')
    last_reported_at = res.strftime('%d of %B of %Y at %I:%M:%S %p %Z')

    last_reported_at = last_reported_at

    categories = result_data["categories"]

    for category in categories:
        outputs.append([IP, last_reported_at, categories_ref[category]])

print("Processing complete!")
outputs.insert(0, ['IP', 'DATE', 'CATEGORIES'])
with open(os.path.join(os.path.dirname(__file__), 'out.csv'), 'w', newline='') as file:   
    write = csv.writer(file)
    write.writerows(outputs)