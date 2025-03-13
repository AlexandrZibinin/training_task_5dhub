Description of the task

Implement an http service that processes incoming requests. The server starts at http://127.0.0.1:8080 (the default value can be changed).

<details>
<summary> List of possible endpoints (can be changed) </summary>

1. Get an abbreviated version of the transmitted URL.

POST /

The method accepts the URL string for shortening in the request body and returns a response with the code 201.

2. Return the original URL.

GET /<shorten-url-id>

The method takes the identifier of the shortened URL as a parameter and returns a response with the code 307 and the original URL in the Location header.

3. Make an async service request and return the data
___________________________________________________

For start: Run file main.py or use command "uvicorn main:app --reload"