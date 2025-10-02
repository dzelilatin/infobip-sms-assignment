import csv
import requests
import random
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

input_filename = 'messages.csv'
output_filename = 'messages_output.csv'

print("Starting the SMS sender script...")

with open(input_filename, mode='r') as infile:
    with open(output_filename, mode='w', newline='') as outfile:

        csv_reader = csv.reader(infile)
        csv_writer = csv.writer(outfile)

        header = next(csv_reader)
        csv_writer.writerow(header)

        for row in csv_reader:
            sender_id = row[0]
            msisdn = row[1]

            print(f"\nProcessing row for number: {msisdn}")

            random_id_for_request = str(random.randint(100000, 999999))

            full_api_url = f"{BASE_URL}/sms/2/text/advanced"

            headers = {
                'Authorization': f'App {API_KEY}',
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }

            payload = {
                'messages': [
                    {
                        'messageId': random_id_for_request, 
                        'from': sender_id,
                        'destinations': [
                            {'to': msisdn}
                        ],
                        'text': 'Hello from my Python script! This is a test for my Infobip assignment. :)'
                    }
                ]
            }
            
            try:
                print("Sending request...")
                response = requests.post(full_api_url, headers=headers, json=payload)
                response.raise_for_status() 

                response_data = response.json()
                print(" Request was successful!")
                
                message_details = response_data['messages'][0]
                
                infobip_message_id = message_details['messageId']
                status_description = message_details['status']['description']

                print(f" Infobip's Message ID: {infobip_message_id}")
                print(f" Status: {status_description}")
                
                row[2] = infobip_message_id
                row[3] = status_description

            except Exception as e:
                print(f" !! ERROR: Something went wrong. Here's the error: {e}")
                
                row[2] = "ERROR"
                row[3] = str(e)

            csv_writer.writerow(row)

print("\nAll done! Check your folder for the 'messages_output.csv' file with the results.")