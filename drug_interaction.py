import requests
import json
from datetime import date
from pathlib import Path
from requests.exceptions import ConnectionError, Timeout, RequestException

class Drug():
    def __init__(self):
        self.drug_A = input('Enter a drug name: ').strip().lower()
        self.drug_B = input('Enter another drug name: ').strip().lower()
        
    def fetch_drug(self, drug_name):
        try:
            url = f'https://api.fda.gov/drug/label.json?search=openfda.brand_name:{drug_name}&limit=1'
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print('Error:', response.status_code)
                return None

        except ConnectionError:
            print("Could not connect to the server.")
                
        except Timeout:
            print('The server is taking too long to respond.')
                 
        except RequestException:
            print('An unexpected error occurred. Try again.')
        
    def save_data(self, drug_name, data):
        
        if 'results' not in data:
            print('No data is found.')
            return None
       
        if not isinstance(data['results'], list):
            print('The data is not a list.')
            return None
        
        result = data['results']
        if not result:
            print('No data is found.')
            return None
                
        drug_result = data['results'][0]
            
        brand_name = drug_result['openfda'].get('brand_name', 'Not available')
        indications_and_usage = drug_result.get('indications_and_usage', 'Not available')

        warnings = drug_result.get('warnings', 'Not available')

        if isinstance(warnings, str):
            warnings = [warnings]
        elif not isinstance(warnings, list):
            warnings = ['Not available']
    
        drug_interactions = drug_result.get('drug_interactions', 'Not available')

        adverse_reactions = drug_result.get('adverse_reactions', 'Not available')

        if isinstance(adverse_reactions, list):
            adverse_reactions = " ".join(adverse_reactions)

        dosage_and_administration = drug_result.get('dosage_and_administration', 'Not available')
        do_not_use = drug_result.get('do_not_use', 'Not available')
        ask_doctor = drug_result.get('ask_doctor', 'Not available')
        
        dic = {
            'Brand name': brand_name,
            'Indications and usage': indications_and_usage,
            'Warnings': warnings,
            'Drug interactions': drug_interactions,
            'Adverse reactions': adverse_reactions,
            'Dosage and administration': dosage_and_administration,
            'Do not use': do_not_use,
            'Consult doctor': ask_doctor
        }
    
        with open(f'{drug_name}.json', 'w', encoding='UTF-8') as file:
            json.dump(dic, file)
        

    def comparison(self, drug_name_A, drug_name_B):
        with open(f'{drug_name_A}.json', encoding='UTF-8') as f:
            drug_A = json.load(f)

        with open(f'{drug_name_B}.json', encoding='utf-8') as x:
            drug_B = json.load(x)

        warnings_A = drug_A.get('Warnings', [])
        
    def comparison(self, drug_name_A, drug_name_B):
        with open(f'{drug_name_A}.json', encoding='UTF-8') as f:
            drug_A = json.load(f)
        with open(f'{drug_name_B}.json', encoding='utf-8') as x:
            drug_B = json.load(x)

        interactions_A = drug_A.get('Drug interactions', 'Not available')
        interactions_B = drug_B.get('Drug interactions', 'Not available')

        a_mentions_b = drug_name_B in str(interactions_A).lower()
        b_mentions_a = drug_name_A in str(interactions_B).lower()

        if a_mentions_b and b_mentions_a:
            risk = 'High risk'
        elif a_mentions_b or b_mentions_a:
            risk = 'Moderate risk'
        else:
            risk = 'Low risk'

        return {
            'Risk level': risk,
            'Drug_A': drug_name_A,
            'Drug_B': drug_name_B,
            'Drug_A data': drug_A,
            'Drug_B data': drug_B
        }

    def generate_report(self, compared_data):
        if compared_data['Risk level'] == 'High risk':
            color = 'red'
        elif compared_data['Risk level'] == 'Moderate risk':
            color = 'orange'
        else:
            color = 'green'

        def get_side_effects(drug_data):
            ae = drug_data.get('Adverse reactions', 'Not available')
            if isinstance(ae, list):
                return " ".join(ae)
            return ae  # already a string

        side_A = get_side_effects(compared_data['Drug_A data'])
        side_B = get_side_effects(compared_data['Drug_B data'])

        with open('result.html', 'w', encoding='UTF-8') as f:
            f.write(f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body{{
            font-family: Georgia;
            background-color: #e8e8e8;
            margin: 0;
            padding: 30px;
        }}
        .container{{
            background-color: #f7fafa;
            margin: auto;
            max-width: 900px;
            padding: 40px;
            border-radius: 10px;
        }}
        .warning-box {{
            max-height: 150px;
            overflow-y: auto;
            background-color: #fff8e1;
            border-left: 5px solid orange;
            padding: 15px;
            border-radius: 5px;
            font-size: 14px;
            margin-bottom: 15px;
        }}
        .warning {{
            max-height: 150px;
            overflow-y: auto;
            background-color: #FFFFE0;
            border-left: 5px solid orange;
            padding: 15px;
            border-radius: 5px;
            font-size: 14px;
            margin-bottom: 20px;
        }}
    </style>
</head>
<body>
<div class="container">
    <h2 style="text-align:center;">Drug Interaction Report</h2>
    <p><strong>Drug A:</strong> {compared_data['Drug_A'].title()}</p>
    <p><strong>Drug B:</strong> {compared_data['Drug_B'].title()}</p>
    <p><strong>Risk:</strong> <span style="color:{color}">{compared_data['Risk level']}</span></p>

    <div class="warning-box">
        <p><strong>{compared_data['Drug_A'].title()} Warning:</strong></p>
        <p>{"<br>".join(compared_data['Drug_A data']['Warnings'])}</p>
    </div>

    <div class="warning">
        <p><strong>{compared_data['Drug_B'].title()} Warning:</strong></p>
        <p>{"<br>".join(compared_data['Drug_B data']['Warnings'])}</p>
    </div>

    <p><strong>{compared_data['Drug_A'].title()} Side effects:</strong> {side_A}</p>
    <p><strong>{compared_data['Drug_B'].title()} Side effects:</strong> {side_B}</p>
</div>
</body>
</html>
''')
        
    def save_history(self, drug_name_A, drug_name_B, risk_level):
        dic = {
            'Risk level': risk_level,
            'Drug_A': drug_name_A.title(),
            'Drug_B': drug_name_B.title(),
            'Date': str(date.today())
        }
        
        file = Path('history.json')
        
        if not file.exists():
            with open('history.json', 'w', encoding='UTF-8') as file:
                json.dump([dic], file)
        else:
            if file.stat().st_size == 0:
                history = []
            else:
                with open('history.json', 'r', encoding='UTF-8') as file:
                    history = json.load(file)

            history.append(dic)

            with open('history.json', 'w', encoding='UTF-8') as file:
                json.dump(history, file)
