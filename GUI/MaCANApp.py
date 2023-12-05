class MaCANApp(MaCANAppGui):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title(f"{app_name} - v{version}")

        self.can_connector = CANBusConnector()
        self.can_processor = CANBusProcessor(self.can_connector)

        # Connect to CAN-Bus when the application starts
        self.can_connector.connect()

        # Example of sending a CAN-Bus message
        # self.can_processor.send_message(msg_id=0x123, data=[0x11, 0x22, 0x33])

        # Example of receiving a CAN-Bus message
        # message = self.can_processor.receive_message()

    # Make sure to disconnect when the application closes
    def on_close(self):
        self.can_connector.disconnect()
        self.master.destroy()
