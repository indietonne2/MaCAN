import can  # Importing the python-can library

class CANBusConnector:
    def __init__(self, channel='mock', bustype='virtual', simulate=False):
        """
        Initializes the CANBusConnector.

        :param channel: The channel or interface to use for the CAN-Bus.
                        Defaults to 'mock' for simulation purposes.
        :param bustype: The type of bus to be used. Defaults to 'virtual',
                        which is suitable for simulation.
        :param simulate: A boolean indicating whether to simulate the CAN-Bus
                         using a mock interface. Defaults to False.
        """
        self.channel = channel if not simulate else 'mock'  # Set to 'mock' if simulation is enabled
        self.bustype = bustype
        self.bus = None  # Placeholder for the CAN-Bus interface

    def connect(self):
        """
        Establishes a connection to the CAN-Bus.

        Tries to connect to the specified CAN-Bus channel. If simulation is enabled,
        it uses a mock backend. On failure, it prints an error message.
        """
        try:
            # Creating a CAN bus interface instance
            self.bus = can.interface.Bus(channel=self.channel, bustype=self.bustype)
            print("Connected to " + ("simulated " if self.channel == 'mock' else "") + "CAN-Bus")
        except Exception as e:
            # Prints an error message if the connection fails
            print(f"Failed to connect to CAN-Bus: {e}")

    def disconnect(self):
        """
        Disconnects from the CAN-Bus.

        Safely shuts down the CAN-Bus interface if it is active.
        """
        if self.bus:
            # Shutting down the CAN-Bus interface
            self.bus.shutdown()
            print("Disconnected from CAN-Bus")
