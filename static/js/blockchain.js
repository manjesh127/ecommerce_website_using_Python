function txnfun() {
    console.log("hii")
    var addres = document.getElementById('ethaddtxn').value
    axios.post('/blockchain/txn/', {
            address: addres,
        })
        .then(function (response) {
            console.log("mmm", response);
            document.getElementById('result').innerHTML = response.data.message
        })
        .catch(function (error) {
            console.log(error);
        });
}