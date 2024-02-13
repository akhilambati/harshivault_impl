const axios = require("axios")

token="hvs.UdOmnFHEXyCVjkzYGRjmqb2r"
url="https://hashicorpvault.corp.multiscale.tech/v1/testsecret/data/"
const requestConfig = {
    headers: {
        "X-Vault-Token": token
    }
}

async function getVaultKeyValue(path, ...keys) {
    vaultPath = url + path;
    vals = new Array()
    const response = await axios.get(vaultPath, requestConfig);
    vaultData = response.data.data.data;
    for(let key of keys){
	if(key in vaultData) {
		vals.push(vaultData[key])
	}
    }
    return vals;
}

getVaultKeyValue("mysql", "username","password").then(value => console.log(value));

