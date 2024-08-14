import requests

def fetch_alphafold_data(uniprot_id, api_key):
    url = f"https://alphafold.ebi.ac.uk/api/prediction/{uniprot_id}?key={api_key}"
    headers = {
        "accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

