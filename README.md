Boot server first, then client. 

Any message sent by client will be encoded and sent to the server.
The server will decode the client's message, reverse it, encode the reversed message, and send back to client.
The client will receive the decoded reversed message in terminal.
