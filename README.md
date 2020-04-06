# Shipment-Imitation
## links
* [demo](https://shipment-imitation.herokuapp.com/)  

* [github](https://github.com/mchozhang/Shipment-Imitation)

* [mongodb mlab](https://www.mlab.com/databases/heroku_4jww1vvv)
account: heroku_4jww1vvv  
password: admin123


## APIs design
* add record  


    url: shipment-imitation.herokuapp.com/record
    method: post
    contentType: "application/json"
    dataType: "json"
    body: {
        "user": <username>,
        "product": <product-name>,
        "age": <age>,
        "longitude": <longitude>,
        "latitude": <latitude>
        "hierarchy": <hierarchy>, #  hierarchy string should sparated by ","
    }
    
    response:
    // if succeed
    {
        record: {
            "user": <username>,
            """product": <product-name>,
            "age": <age>,
            "longitude": <longitude>,
            "latitude": <latitude>,
            "hierarchy": <hierarchy>, #  hierarchy string should sparated by ","
        }
        "status": "success"
    }
    
    // if fail
    {
        "status": "failed",
        "err_msg": <error message>,
    }
    
    examples:
    // add new record, body json data
    {
        "user": "wenhao",
        "product": "cat",
        "age": 20,
        "longitude": 114.5,
        "latitude": <latitude>
        "hierarchy""": "cat, dog, lion",
    }
    
    
* search record  
you can search records by using user or product parameters in url

    url:  /record
    param: {
        user: <user>,
        product: <product>,
    }
    method: get
    dataType: NoneType
    response:
    // if succeed
    {
        records: [{
            "id", <id>
            "user": <username>,
            "product": <product-name>,
            "age": <age>,
            "longitude": <longitude>,
            "latitude": <latitude>,
            "hierarchy": <hierarchy>, #  hierarchy string should sparated by ","
        }],
        "status": "success"
    }
    
    // if fail
    {
        "status": "failed",
        "err_msg": <error message>,
    }
    
    examples:
    // search all records
    https://shipment-imitation.herokuapp.com/record
    
    // search by user
    https://shipment-imitation.herokuapp.com/record?user=wenhao
    
    // search by product and user
    https://shipment-imitation.herokuapp.com/record?user=wenhao&product=pen
    
* delete one record  


    url: shipment-imitation.herokuapp.com//record
    method: delete
    dataType: 'json'
    contentType: 'application/json'
    body:
    {
        "id": <id>
    }
    
    response:
    // if succeed
    {
        "status": "success"
    }
    
    // if fail
    {
        "status": "failed",
        "err_msg": <error message>,
    }
    
    examples:
    // delete one record by id
    {
        "id": "5e8a7a879810639d7904ad28"
    }
    
* delete multiple records


    url: shipment-imitation.herokuapp.com/delete-records
    method: delete
    dataType: 'json'
    contentType: 'application/json'
    body:
    {
        "records": [ <id-1>, <id-2>, ...]
    }
    
    response:
    // if succeed
    {
        "status": "success"
    }
    
    // if fail
    {
        "status": "failed",
        "err_msg": <error message>,
    }
    
    examples:
    // delete multiple records by ids
    {
        "records": ["5e8a7a879810639d7904ad28", "5e8a7a939810639d7904ad29"]
    }