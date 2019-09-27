function txnfun() {
    console.log("hii")
    var addres = document.getElementById('ethaddtxn').value
    axios.post('/blockchain/txn/', {
            address: addres,
        })
        .then(function (response) {
            console.log("mmm", response);
        })
        .catch(function (error) {
            console.log(error);
        });
}