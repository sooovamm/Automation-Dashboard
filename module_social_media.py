def whatsapp(monumb, msg, time_h, time_m):
        import pywhatkit
        pywhatkit.sendwhatmsg(monumb, msg, int(time_h), int(time_m))

def whatsapp_tui():
        import pywhatkit
        from datetime import datetime
        import pyautogui
        import keyboard as k
        import time

        # Get user inputs
        monumb = input("Enter the phone number (with country code, e.g., +1234567890): ")
        msg = input("Enter the message you want to send: ")

        # Ask the user if they want to send the message instantly or schedule it
        choice = input("Do you want to send the message instantly? (yes/no): ").strip().lower()
    
        if choice == 'yes':
            try:
                # Send the message instantly
                pywhatkit.sendwhatmsg_instantly(monumb, msg)
                pyautogui.click(1134, 1009)
                time.sleep(45)
                k.press_and_release('enter')
                print("Message sent instantly!")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            # Get the time to schedule the message
            time_h = input("Enter the hour (in 24-hour format) you want to send the message: ")
            time_m = input("Enter the minute you want to send the message: ")
            try:
                # Schedule the message
                pywhatkit.sendwhatmsg(monumb, msg, int(time_h), int(time_m))
                pyautogui.click(1134, 1009)
                time.sleep(45)
                k.press_and_release('enter')
                print("Message scheduled successfully!")
            except Exception as e:
                print(f"An error occurred: {e}")

def email():
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    # Email account credentials
    sender_email = input("Enter your email address: ")
    sender_password = input("Enter your email password: ")

    # Ask the user for email details
    recipient_email = input("Enter the recipient's email address: ")
    subject = input("Enter the subject of the email: ")
    body = input("Enter the body of the email: ")

    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        # Connect to Gmail's SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            text = message.as_string()
            server.sendmail(sender_email, recipient_email, text)
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def email_schedule():
    import smtplib
    import schedule
    import time
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # Ask the user for input
    sender_email = input("Enter your email address: ")
    password = input("Enter your email password: ")
    receiver_email = input("Enter the recipient's email address: ")
    subject = input("Enter the subject of the email: ")
    body = input("Enter the body of the email: ")
    schedule_time = input("Enter the scheduled time (format: 'YYYY-MM-DD HH:MM'): ")

    def send_email():
        try:
            # Set up the MIME
            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = receiver_email
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))

            # Connect to the server
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            # Send the email
            server.sendmail(sender_email, receiver_email, message.as_string())
            server.close()
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")

    # Convert the schedule time to the correct format
    schedule_time_struct = time.strptime(schedule_time, "%Y-%m-%d %H:%M")
    schedule_time_seconds = time.mktime(schedule_time_struct)

    # Schedule the email
    schedule.every().day.at(time.strftime("%H:%M", schedule_time_struct)).do(send_email)
    print(f"Email scheduled to be sent at {schedule_time}")

    # Keep the script running to execute the scheduled task
    while True:
        schedule.run_pending()
        time.sleep(1)

def insta():
        from instagrapi import Client

        # Ask for the required inputs
        username = input("Enter your Instagram username: ")
        password = input("Enter your Instagram password: ")
        image_path = input("Enter the path to the image you want to upload: ")
        caption = input("Enter the caption for your post: ")

        # Initialize the client
        client = Client()
        client.login(username, password)

        # Upload the photo
        client.photo_upload(image_path, caption)
        print("Photo uploaded successfully!")

def whatsapp_multi_msg():
    import pywhatkit as kit
    import time

    # Ask user for mobile numbers of recipients
    numbers_input = input("Enter recipient mobile numbers separated by commas: ")
    whatsapp_numbers = [num.strip() for num in numbers_input.split(',')]

    # Message to be sent
    message = input("Enter the message to send: ")

    # Function to send messages
    def send_whatsapp_message(number, message):
        try:
            # Send a message to the specified number
            kit.sendwhatmsg_instantly(number, message)
            print(f"Message sent to {number}")
        except Exception as e:
            print(f"Failed to send message to {number}: {e}")

    # Loop through each number and send the message
    for number in whatsapp_numbers:
        send_whatsapp_message(number, message)
        # Wait for 5 seconds to avoid triggering WhatsApp's rate limits
        time.sleep(5)

def purpose():
    import numpy as np

    # Ask for the number of entries
    num_entries = int(input("Enter the number of entries: "))

    # Initialize an empty list to store data
    data_list = []

    # Collect details for each entry
    for _ in range(num_entries):
        name = input("Enter name: ")
        city = input("Enter city: ")
        college = input("Enter college: ")
        phone_number = input("Enter phone number: ")
        life_purpose = input("Enter life purpose: ")
        data_list.append((name, city, college, phone_number, life_purpose))

    # Convert list to numpy array
    data = np.array(data_list)

    # Function to search by college name and retrieve life purposes
    def get_life_purpose_by_college(college_name):
        # Filter rows where college name matches
        filtered_data = data[data[:, 2] == college_name]

        # Extract life purposes from filtered data
        life_purposes = filtered_data[:, 4]

        # Return life purposes
        return life_purposes

    # Ask for the college name to search
    college_name = input('Enter college name to search: ')
    life_purposes = get_life_purpose_by_college(college_name)

    # Print results
    print(f"Life purposes of students from '{college_name}' college:")
    if life_purposes.size > 0:
        for purpose in life_purposes:
            print(purpose)
    else:
        print("No entries found for the provided college name.")

def msg_to_not_in_city():
    import numpy as np
    from twilio.rest import Client
    from twilio.base.exceptions import TwilioRestException

    # Your Twilio account SID and auth token
    account_sid = input("Enter your Twilio account SID: ")
    auth_token = input("Enter your Twilio auth token: ")
    twilio_phone_number = input("Enter your Twilio phone number (e.g., +1234567890): ")

    # Initialize Twilio client
    client = Client(account_sid, auth_token)

    # Ask for the number of entries
    num_entries = int(input("Enter the number of entries: "))

    # Initialize an empty list to store data
    data_list = []

    # Collect details for each entry
    for _ in range(num_entries):
        name = input("Enter name: ")
        city = input("Enter city: ")
        college = input("Enter college: ")
        phone_number = input("Enter phone number: ")
        life_purpose = input("Enter life purpose: ")
        data_list.append((name, city, college, phone_number, life_purpose))

    # Convert list to numpy array
    data = np.array(data_list)

    # Ask for the city to exclude
    exclude_city = input("Enter the city to exclude: ")

    # Message to be sent
    message_text = input("Enter the message to send: ")

    # Function to send SMS
    def send_sms(to_number, message):
        try:
            client.messages.create(
                body=message,
                from_=twilio_phone_number,
                to=to_number
            )
            print(f"Message sent to {to_number}")
        except TwilioRestException as e:
            print(f"Failed to send message to {to_number}: {e}")

    # Loop through each person in the data and send SMS if they are not from the excluded city
    for person in data:
        name, city, college, phone_number, life_purpose = person
        if city.lower() != exclude_city.lower():
            send_sms(phone_number, message_text)


