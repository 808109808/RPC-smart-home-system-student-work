import xmlrpc.client

def main():
    with xmlrpc.client.ServerProxy("http://localhost:9000/") as proxy:
        # Call the server's set_temperature method
        result = proxy.set_temperature(22)  # Example: Set temperature to 22°C
        print(result)

if __name__ == '__main__':
    main()
