
To run the program, install python, Flask, and install sqlite3. 

Clone the repository, open a command prompt, navigate to the folder and execute the python file:

py app.py


Task 1: Create a Dog Application

1. Create a structured project containing a flask-restful webservice application

2. The API should have 1 resource (with CRUD HTTP methods) representing a Dog.
	a. Create - use the appropriate HTTP method to create a new dog (fields are up toyou, but something along the lines of name, breed, id etc.)
	b. Read - use the appropriate HTTP method to retrieve a list of dogs, as well as individual dogs by id
	c. Update - use the appropriate HTTP methods to allow editing of a dog’s attributes
	d. Delete - use the appropriate HTTP method to delete an individual dog record

3. Datastore for routes is arbitrary (i.e. in memory, sqlite - up to you)


Task 2: Implement Validation

Implement validation on the create and update methods, to ensure that the incoming request data is valid.


Task 3: Implement Caching

Implement a simple cache on the read method. The cache should:

1. Cache the results for a read on a given id

2. Return cached results for the same id

3. Expire the cached results after 90 seconds


Task 4 (bonus): Implement Configuration

Include configuration to differentiate production/test config, and configure the following:

1. Server port

2. Cache url

3. Cache default timeout/expiry
