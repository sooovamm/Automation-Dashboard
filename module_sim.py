def call():
        from twilio.rest import Client  
        # Ask for the required inputs
        account_sid = input("Enter your Twilio Account SID: ")
        auth_token = input("Enter your Twilio Auth Token: ")
        recipient_number = input("Enter the recipient's phone number (e.g., +1234567890): ")
        twilio_number = input("Enter your Twilio phone number (e.g., +1234567890): ")
        message = input("Enter the message to say on the call: ")

        # Initialize the Twilio client
        client = Client(account_sid, auth_token)

        # Create and initiate the call
        call = client.calls.create(
            twiml=f'<Response><Say>{message}</Say></Response>',
            to=recipient_number,
            from_=twilio_number
        )
        print("Call initiated with SID:", call.sid)

def msg():
        from twilio.rest import Client

        # Ask for the required inputs
        account_sid = input("Enter your Twilio Account SID: ")
        auth_token = input("Enter your Twilio Auth Token: ")
        twilio_number = input("Enter your Twilio phone number (e.g., +1234567890): ")
        recipient_number = input("Enter the recipient's phone number (e.g., +1234567890): ")
        message_body = input("Enter the message to send: ")

        # Initialize the Twilio client
        client = Client(account_sid, auth_token)

        # Send the message
        message = client.messages.create(
            body=message_body,
            from_=twilio_number,
            to=recipient_number
        )
        print(f"Message sent with SID: {message.sid}")


