# Shipment-Imitation

## API design
* add record  


    url:  /record
    method: post
    contentType: 'application/json'
    dataType: 'json'
    body: {
        'user': <username>,
        'product': <product-name>,
        'age': <age>,
        'longitude': <longitude>,
        'latitude': <latitude>
        'hierarchy': <hierarchy>, #  hierarchy string should sparated by ','
    }
    
    response:
    // if succeed
    {
        record: {
            'user': <username>,
            'product': <product-name>,
            'age': <age>,
            'longitude': <longitude>,
            'latitude': <latitude>,
            'hierarchy': <hierarchy>, #  hierarchy string should sparated by ','
        }
        "status": "success"
    }
    
    // if fail
    {
        "status": "failed",
        "err_msg": <error message>,
    }