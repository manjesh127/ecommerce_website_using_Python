from django.shortcuts import render,redirect
from django.contrib import messages
import json
from django.http import JsonResponse
from web3 import Web3
w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v2/87d8eb0d3c004535bced571f19986f18"))


def account(request):
    myAccount = w3.eth.account.create('pass')
    myAddress = myAccount.address
    myPrivateKey = myAccount.privateKey
    print('my address is     : {}'.format(myAccount.address))
    print('my private key is : {}'.format(myAccount.privateKey.hex()))

def home(request):
    if w3.isConnected():
        # print("connected=== block=>",w3.eth.blockNumber)
        block = w3.eth.blockNumber
        return render(request,'blockchainhome.html',{'block':block})
    else:
        print("not connected")
        
def txn(request):
    if request.method == 'GET':
        return redirect('/blockchain')
    else:
        data=json.loads(request.body)
        print(data['address'])
        if w3.isAddress(data['address']):
            try:
                nonce = w3.eth.getTransactionCount('0x030810339E7441AEd6639Eda5d7d6B65aF0fD518')
                transaction={
                    'to':data['address'],'value': w3.toWei(2, 'gwei'),'gas': 21000,'gasPrice': w3.toWei('1', 'gwei'),'nonce': nonce,} 

                key ='0xE08F88AC9E86ECD0E6B2F9F46AD71B1E4357CE033C38A2B6E9E04E4561B82F5E'   
                signed = w3.eth.account.sign_transaction(transaction, key)
                txnhash = w3.eth.sendRawTransaction(signed.rawTransaction)
                print("transaction hash===>",w3.toHex(txnhash))
                return JsonResponse({'success':True,'message':txnhash})
            except Exception as e:
                print("exception",e)
                return JsonResponse({'success':False,'message':'Invalid address'})
            else:
                return JsonResponse({'success':False,'message':'Invalid address else try'})
            
        else:
            return JsonResponse({'success':False,'message':'Invalid address'})
    


    # nonce = w3.eth.getTransactionCount('0x030810339E7441AEd6639Eda5d7d6B65aF0fD518')
    # transaction={
    #     'to':"0xaCEe93eC465888D84337586d44273D110672032e",'value': w3.toWei(2, 'gwei'),'gas': 21000,'gasPrice': w3.toWei('1', 'gwei'),'nonce': nonce,} 

    # key ='0xE08F88AC9E86ECD0E6B2F9F46AD71B1E4357CE033C38A2B6E9E04E4561B82F5E'   
    # signed = w3.eth.account.sign_transaction(transaction, key)
    # txnhash = w3.eth.sendRawTransaction(signed.rawTransaction)
    # print("transaction hash===>",w3.toHex(txnhash))



def balance(request):
   
    try:
        if request.method == "POST":
            username = request.POST['address']
            banance_eth = w3.eth.getBalance(username)
            ether = w3.fromWei(banance_eth,'ether')
            messages.success(request,ether)
            return redirect('/blockchain')
        else:
            return redirect('/blockchain')  

    except:
        print("error invalid etherum address")
        messages.info(request,'invalid etherum address')
        return redirect('/blockchain')


    else:
        messages.info(request,'invalid etherum address')
        return redirect('/blockchain')
    