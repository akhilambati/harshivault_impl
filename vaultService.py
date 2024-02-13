import requests

url = "http://hashicorpvault.corp.multiscale.tech/v1/testsecret/data/"
token = "hvs.UdOmnFHEXyCVjkzYGRjmqb2r"
headers={"X-Vault-Token": token}

def getVaultValue(path,keys):
    val = []
    response = requests.get(url + path, headers=headers)
    if response.status_code == 200:
        vault_data = response.json()['data']['data']
        for key in keys:
            if key in vault_data:
                val.append(vault_data[key])
        return val
    else:
        print("Error file fetching response from vault, response code {}".format(response.status_code))
        raise Exception("Error file fetching response from vault, response code {}".format(response.status_code))

print(getVaultValue("mongo",["username","password"]))


