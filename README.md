# Shipment-Imitation

## Problem Statement
A logistics company wants to know the location of their products, where they can use the api service
to track the product(GET), insert new products(POST) or delete an existing product(DELETE)

* User should be able to insert the prodcut details(let's say 5 columns[userid, age, latitude, logitude, productName] in the database
{Database can be of your choice(DynamoDB, MySQL, Postgres etc.}
* User should be able to locate the record(one at a time) and multiple(recursive at a time) from the API method.
* User should be able to delete the records ( same as Point 2 mentioned above)
* Provide the API documentation


### Bonus Points:
* If you can add multi level product chain ( Product 1 links to Product 2, product 3 ... Product N) and then use the API methods to retrieve the hierarchy.
* If you can provide a basic bootstrap frontend to test this service from a Front End UI.