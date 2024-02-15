from xmlrpc.server import SimpleXMLRPCServer
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def set_thermostat_temperature(temperature):
    logging.info(f"Setting thermostat temperature to {temperature}°C")
    # Here, you would add the actual code to communicate with the thermostat.
    return f"Temperature set to {temperature}°C"

def main():
    server = SimpleXMLRPCServer(('localhost', 9000), logRequests=True)
    server.register_function(set_thermostat_temperature, 'set_temperature')

    try:
        logging.info("Serving XML-RPC on localhost port 9000...")
        server.serve_forever()
    except KeyboardInterrupt:
        print("Exiting")

if __name__ == '__main__':
    main()
