Jaideep Singh Kainth

DESCRIPTION: It is a multithreaded Web server and a simple web client project. The web server and client communicate using HTTP. The client requests a file from the server and the server checks if it exists - if it does, the server returns 200 OK message along with the contents of the file to the client; otherwise, it returns 404 Not Found error.

INSTRUCTIONS:

Instructions for running clients from the browser:
1. Run server.py [<port_number>] from the command prompt with the port number on which you want to run your server(Screenshots added). If you don't specify port number ther server will run automatically on port 8080.
2. Start a browser and type "localhost:<port_number>/<page_name>"  Type same port_number on which your server is currently running and the page name(if you dont specify page name Default page i.e index.html will be displayed)and press Enter to see page details.
3. Details of Server and Client will be displayed on command prompt with page details.

Instructions for running clients from the command prompt:
1. Run server.py [<port_number>] from the command prompt with the port number on which you want to run your server(Screenshots added). If you don't specify port number ther server will run automatically on port 8080.
2. Run client.py <server_IPaddress/name> <port_number> [<requested_file_name>]. Type localhost for server_IPadress and the same port number on which your server is currently running and the page name(if you dont specify page name Default page i.e index.html will be displayed)and press Enter to see page details.
3. Details of Server and Client will be displayed on command prompt with page details.
