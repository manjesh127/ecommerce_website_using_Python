from django.shortcuts import render
from web3 import Web3
# my_provider = Web3.IPCProvider('https://rinkeby.infura.io/v2/87d8eb0d3c004535bced571f19986f18')
w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v2/87d8eb0d3c004535bced571f19986f18"))

# Create your views here.

def account(request):
    myAccount = w3.eth.account.create('pass')
    myAddress = myAccount.address
    myPrivateKey = myAccount.privateKey
    print('my address is     : {}'.format(myAccount.address))
    print('my private key is : {}'.format(myAccount.privateKey.hex()))

def home(request):
    if w3.isConnected():
        print("connected=== block=>",w3.eth.blockNumber)
        block = w3.eth.blockNumber
        return render(request,'blockchainhome.html',{'block':block})
    else:
        print("not connected")
        