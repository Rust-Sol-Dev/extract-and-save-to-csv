import requests
import pandas as pd
from datetime import datetime

addresses = [
    "0xa67C820B9B50d8075CA99f46E86304EC7AeFE168",
    "0x9d444Fa4DB99ed548C6E8ecF5A89F18080aba970",
    "0x5dB7CbC12a312F81b5dD81ce2BF76A52e12aE884",
    "0xD7DA5C809fF83A5b798ef26C43dAFdCe8B5A9595",
    "0x92a91cC0D9D55D365F637f0894Cb0F1DF1e8a464",
    "0xFac1E6471559e3131be2FF9731c25372f1F34564",
    "0xB21872d7fda870122370281af77B9bd7A9BA2dE8",
    "0x107E569B61679b553826B7aA3A62eFc93e3437E4",
    "0xAfBF48add305A76e88E672d74022Ff58E55889c9",
    "0x33aD7E5C56619f762c3b486Fb66519e8DcaA2682"
]

for address in addresses:
    # Define the API URL
    api_url = f"https://swamps-explorer.tc.l2aas.com/api?module=account&action=tokentx&address={address}"
    
    # Fetch the data from the API
    response = requests.get(api_url)
    data = response.json()
    
    # Check if the response is successful
    if data['message'] == 'OK':
        # Extract the result
        transactions = data['result']
        
        # Convert the list of transactions to a DataFrame
        df = pd.DataFrame(transactions)
        
        # Convert the timestamp to a readable date-time format
        df['timeStamp'] = df['timeStamp'].apply(lambda x: datetime.utcfromtimestamp(int(x)).strftime('%Y-%m-%d %H:%M:%S'))
        
        # Save the DataFrame to a CSV file
        csv_filename = f'transactions_{address}.csv'
        df.to_csv(csv_filename, index=False)
        print(f"Data has been saved to {csv_filename}")
    else:
        print(f"Failed to fetch data for address {address}")