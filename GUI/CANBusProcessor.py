class CANBusProcessor:
    def __init__(self, connector: CANBusConnector):
        self.connector = connector

    def send_message(self, msg_id, data):
        message = can.Message(arbitration_id=msg_id, data=data, is_extended_id=False)
        try:
            self.connector.bus.send(message)
            print("Message sent on CAN-Bus")
        except Exception as e:
            print(f"Failed to send message: {e}")

    def receive_message(self):
        try:
            message = self.connector.bus.recv()  # Blocking call
            print(f"Received message: {message}")
            return message
        except Exception as e:
            print(f"Failed to receive message: {e}")
            return None
