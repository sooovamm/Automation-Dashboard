print("\t\tWelcome, tell us what action you want to perform")
print("\t\t------------------------------------------------")
print("\n\n")

ch = None

while ch != "exit":
    ch = input(":-")




    if "menu" in ch.lower():
        print("""following commands are available to execute:-
        NOTE:- "+" indicates that those all words should be included in the command.
               "/" indicates that you can use any of the commands written there to perform the given operation.
         0. menu :-
                show all the commands available in menu project

         1. whatsapp + send :-
                send whatsapp msg to a single person or group of people

         2. not live in jaipur / not from jaipur :-
                send whatsapp msg to those who don't live in jaipur

         3. sms / msg :-
                send sms to someone

         4. email :-
                send email to someone

         5. search / google :-
                search over google and show top 6 results as output

         6. call / phone / phone call :-
                give a phone call to someone

         7. insta :-
                to post over your instagram account

         8. purpose :-
                show the purpose section from collected data

         9. video by ipwebcam / ipwebcam / video :-
                to start a video capture from your mobile camera

        10. remote login / ssh :-
                to remote login in any OS by SSH protocol

        11. rainbow + text :-
                to convert any text in RAINBOW colors

        12. change firefox name and icon :-
                to change firefox name and logo
 
        13. launch firefox :- 
                launch firefox

        14. linear regression :-
                linear regression

        15. launch EC2 :-
                launch EC2 instances

        16. insert data in mongoDb database :-
                insert data in mongoDb database

        17. email with attached image :-
                email with attached image

        18. gemini text-to-text :-
                Gemini text-to-text

        19. click photo of whoever sit infront of the system or laptop :-
                click photo of whoever sit infront of the system or laptop

        20. speak :-
                text will get spoken by speaker

        21. telegram :-
                send msg on telegram

        22. user + add :-
                helps you to create new user and set password

        23. ascii :-
                On your cmd you print something and it will be converted to ASCII art

        24. location :-
                Find the current geo coordinates and Location

        25. docker + pull :-
                pull  docker image

        26. docker + launch :-
                launch docker container

        27. docker + start :-
                start docker container

        28. docker + stop :-
                stop docker container

        29. docker + status :-
                check status of docker container

        30. docker + remove + container :-
                remove docker container

        31. docker + logs :-
                retrieves the logs of a Docker container

        32. docker + remove + image :-
                remove docker image

        33. dataset + processing :-
                automatically does data processing on giving the dataset

        34. upload + s3 :-
                Uploading any object to s3

        35. exit :-
                to exit the program""")


    elif "send" in ch.lower() and "whatsapp" in ch.lower():
        group_msg = input("Do you want to send msg to group [y/n]:")
        if group_msg == "n":
            from module_social_media import whatsapp_tui
            whatsapp_tui()
        else:
            from module_social_media import whatsapp_multi_msg
            whatsapp_multi_msg()

    elif "call" in ch.lower() or "phone call" in ch.lower() or "phone" in ch.lower():
        from module_sim import call
        call()

    elif "sms" in ch.lower() or "msg" in ch.lower():
        from module_sim import msg
        msg()

    elif "email" in ch.lower():
        choice = input("do you want to schedule it for a specific time [y/n]:")
        if choice == "n":
            from module_social_media import email
            email()
        elif choice == "y":
            from module_social_media import email_schedule
            email_schedule()

    elif "search" in ch.lower() or "google" in ch.lower():
        from module_internet import google_search
        google_search()

    elif "insta" in ch.lower():
        from module_social_media import insta
        insta()

    elif "send" in ch.lower() and (("whatsapp" in ch.lower() and "group" in ch.lower()) or ("whatsapp" in ch.lower() and "bulk" in ch.lower())):
        from module_social_media import whatsapp_multi_msg
        whatsapp_multi_msg()

    elif "purpose" in ch.lower():
        from module_social_media import purpose
        purpose()

    elif "not live in jaipur" in ch.lower() or "not from jaipur" in ch.lower():
        from module_social_media import msg_to_not_in_city
        msg_to_not_in_city()

    elif "video by ipwebcam" in ch.lower() or "video" in ch.lower() or "ipwebcam" in ch.lower():
        from module_os import video_ipwebcam
        video_ipwebcam()

    elif ("remote login" in ch.lower() or "ssh" in ch.lower()) and not("send" in ch.lower() or "transfer" in ch.lower()):
        hostname = input("enter hostname or IP:")
        port = input("enter port number [default port 22]:")
        username = input("enter username:")
        password = input("enter password:") 
        command = input("enter command you want to run:")

        from module_remote_os import ssh_login
        ssh_login(hostname, port, username, password, command)

    elif "rainbow" in ch.lower() and "text" in ch.lower():
        text = input("enter the text:")
        from module_os import rainbow_text
        rainbow_text(text)

    elif "change firefox name and icon" in ch.lower():
        import os

        # Define the file path
        file_path = "/usr/share/applications/firefox.desktop"

        # Ensure the script is running as root
        if os.geteuid() != 0:
            raise PermissionError("This script must be run as root.")

        # Read the content of the file
        with open(file_path, "r") as file:
            lines = file.readlines()

        # Modify the lines
        with open(file_path, "w") as file:
            for line in lines:
                if line.startswith("Name="):
                    file.write("Name=Google\n")
                elif line.startswith("Icon="):
                    file.write("Icon=/root/Downloads/levi.jpg\n")
                else:
                    file.write(line)

        print("Changes have been made successfully.")
 
    elif "launch firefox" in ch.lower():
        import subprocess
        url="https://www.google.com"
        subprocess.Popen(["firefox",url])

    elif "linear regression" in ch.lower():
        import pandas 
        db=pandas.read_csv("Markx.txt")
        y=db["marks"]
        x=db["hours"]
        x=x.values.reshape(-1,1)
        from sklearn.linear_model import LinearRegression
        #model create 
        model=LinearRegression()
        #model train
        model.fit(x,y)
        model.predict([[8]])

    elif "launch EC2" in ch.lower():
        import boto3

        # Get AWS credentials and region from the user
        aws_access_key_id = input("Enter your AWS Access Key ID: ")
        aws_secret_access_key = input("Enter your AWS Secret Access Key: ")
        region_name = input("Enter the AWS Region (e.g., 'ap-south-1'): ")
    
        # Get EC2 instance details from the user
        instance_type = input("Enter the EC2 Instance Type (e.g., 't2.micro'): ")
        image_id = input("Enter the AMI ID (e.g., 'ami-0ec0e125bb6c6e8ec'): ")

        # Create EC2 resource
        myec2 = boto3.resource(
            service_name="ec2",
            region_name=region_name,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )

        # Launch the EC2 instance
        myec2.create_instances(
            InstanceType=instance_type,
            ImageId=image_id,
            MaxCount=1,
            MinCount=1
        )    
        print("EC2 instance launched successfully!")

    elif "insert data in mongoDb database" in ch.lower():
        import pymongo
        connection=pymongo.MongoClient("mongodb://localhost:27017/") #connection stablished
        dbname=connection["komal"]
        nnn=dbname["haq"]
        nnn.insert_many([{"name":"jack"},{"name":"rock"},{"phone":"6789"}])
        for data in nnn.find():
            print(data)

    elif "email with attached image" in ch.lower():
        def sendingEmailWithAttach():
            import smtplib
            from email.mime.text import MIMEText 
            from email.mime.application import MIMEApplication
            from email.mime.multipart import MIMEMultipart

            # Get user inputs
            sender_email = input("Enter the sender's email: ")
            sender_password = input("Enter the sender's email password: ")
            receiver_email = input("Enter the receiver's email: ")
            subject = input("Enter the subject of the email: ")
            message_body = input("Enter the message body of the email: ")
            attachment_file = input("Enter the path of the file to attach: ")

            # Set up the server
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()

            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message_body, 'plain'))
    
            # Attach the file
            try:
                with open(attachment_file, 'rb') as f:
                    attachment = MIMEApplication(f.read())
                    attachment.add_header('Content-Disposition', 'attachment', filename=attachment_file)
                    msg.attach(attachment)
            except FileNotFoundError:
                print("Attachment file not found. Please check the path and try again.")
                return

            # Login to the server and send the email
            try:
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
                print("-------------Email Sent with Attachment------------")
            except smtplib.SMTPAuthenticationError:
                print("Failed to login. Please check your email and password.")
            except Exception as e:
                print(f"Failed to send email: {e}")
            finally:
                server.quit()

        # Call the function to send the email with attachment
        sendingEmailWithAttach()


    elif "gemini text-to-text" in ch.lower():
        import os  
        import google.generativeai as gemai

        def generate_content():
            # Get user inputs
            api_key = input("Enter your Google Generative AI API key: ")
            model_name = input("Enter the model name (e.g., 'gemini-1.5-flash'): ")
            prompt = input("Enter the prompt for content generation: ")

            # Configure the API
            gemai.configure(api_key=api_key)

            # Initialize the model
            model = gemai.GenerativeModel(model_name=model_name)

            # Generate content
            response = model.generate_content(prompt)

            # Print the generated response
            print(f"Generated Content: {response}")

        # Call the function
        generate_content()


    elif "click photo of whoever sit infront of the system or laptop" in ch.lower():
        import cv2
        import mediapipe as mp
        import time

        # Initialize the webcam
        cap = cv2.VideoCapture(0)

        # Initialize the MediaPipe Face Detection
        mp_face_detection = mp.solutions.face_detection
        mp_drawing = mp.solutions.drawing_utils

        face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)

        # Initialize a counter and a flag
        photo_counter = 0
        face_detected = False

        # Flag to control the visibility of the window
        show_window = False

        # Function to save the captured image
        def save_photo(frame, counter):
            filename = f'photo_{counter}.jpg'
            cv2.imwrite(filename, frame)
            print(f"Photo saved as {filename}")

        # Mouse callback function to show the window
        def on_mouse(event, x, y, flags, param):
            global show_window
            if event == cv2.EVENT_LBUTTONDOWN:
                show_window = not show_window

        # Create a named window and set the mouse callback
        cv2.namedWindow("Webcam", cv2.WINDOW_NORMAL)
        cv2.setMouseCallback("Webcam", on_mouse)

        # Main loop
        while True:
            success, frame = cap.read()
            if not success:
                break

            # Convert the frame to RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Perform face detection
            results = face_detection.process(rgb_frame)

            # Check if a face is detected
            if results.detections:
                if not face_detected:
                    face_detected = True
                    photo_counter += 1
                    save_photo(frame, photo_counter)

                # Draw face detections
                for detection in results.detections:
                    mp_drawing.draw_detection(frame, detection)
            else:
                face_detected = False

            # Display the frame if the window is supposed to be shown
            if show_window:
                cv2.imshow("Webcam", frame)

            # Check if 'q' is pressed to break the loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the webcam and close the window
        cap.release()
        cv2.destroyAllWindows()


    elif (("remote login" in ch.lower() or "ssh" in ch.lower()) and ("transfer" in ch.lower() or "send" in ch.lower())):
        hostname = input("enter hostname or IP:")
        port = input("enter port number [default port 22]:")
        username = input("enter username:")
        password = input("enter password:")

        send_file_to_remote(hostname, port, username, password)

    elif "speak" in ch.lower():
        import os
        from gtts import gTTS
        import playsound

        def speak(text):
            """Function to convert text to speech."""
            tts = gTTS(text)
            tts.save("output.mp3")
            playsound.playsound("output.mp3")
        
        text = input("enter your text:")
        speak(text)

    elif "telegram" in ch.lower() :
        from telethon import TelegramClient  

        def send_telegram_message():
            # Ask for the required inputs
            api_id = input("Enter your API ID: ")
            api_hash = input("Enter your API Hash: ")
            phone_number = input("Enter your phone number: ")
    
            # Initialize the Telegram client
            client = TelegramClient('session_name', api_id, api_hash)

            async def send_message(recipient, message_text):
                """
                Sends a message to a specified recipient.

                Parameters:
                recipient (str): The username (with @), user ID, or phone number of the recipient.
                message_text (str): The text of the message to send.
                """
                # Connect to the Telegram server
                await client.start(phone=phone_number)

                # Send a message to the specified recipient
                await client.send_message(recipient, message_text)
        
                # Disconnect the client
                await client.disconnect()

            # Run the script
            with client:
                recipient = input("Enter the @username or phone number of the recipient: ")
                msg = input("Enter the message: ")
                client.loop.run_until_complete(send_message(recipient, msg))

        # Call the function
        send_telegram_message()


    elif "user" in ch.lower() and "add" in ch.lower():
        import subprocess

        def create_user(username, password):
            """
            Creates a new user and sets a password for the user on a Linux system.

            Parameters:
            username (str): The username of the new user.
            password (str): The password to be set for the new user.
            """
            try:
                # Create the user
                subprocess.run(['sudo', 'useradd', '-m', '-s', '/bin/bash', username], check=True)

                # Set the user's password
                subprocess.run(['sudo', 'chpasswd'], input=f'{username}:{password}'.encode(), check=True)

                print(f"User '{username}' created and password set successfully.")
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")
                print("Failed to create the user or set the password.")
        # Example usage:
        create_user('newusername', 'newpassword')
    
    elif "ascii" in ch.lower():
        import pyfiglet
        def print_ascii_art(text):
            # Create an ASCII art object
            ascii_art = pyfiglet.figlet_format(text)
        
            # Print the ASCII art
            print(ascii_art)

        text_to_convert = input("Enter the text to convert to ASCII art: ")
        print_ascii_art(text_to_convert)

    elif "location" in ch.lower():
        import geocoder

        def get_current_location():
            # Get the current location using geocoder's IP method
            g = geocoder.ip('me')

            if g.ok:
                latitude = g.latlng[0]
                longitude = g.latlng[1]
                location = g.city + ", " + g.state + ", " + g.country
                return {
                    'latitude': latitude,
                    'longitude': longitude,
                    'location': location
                }
            else:
                return {
                    'error': 'Unable to get location.'
                }

        location_info = get_current_location()
        if 'error' in location_info:
            print(location_info['error'])
        else:
            print(f"Latitude: {location_info['latitude']}")
            print(f"Longitude: {location_info['longitude']}")
            print(f"Location: {location_info['location']}")

    elif "docker" in ch.lower() and "pull" in ch.lower():
        import docker

        def pull_docker_image(image_name):
            """
            Pull a Docker image from a Docker registry.
        
            :param image_name: The name of the Docker image to pull (e.g., 'ubuntu:latest').
            """
            try:
                # Initialize a Docker client
                client = docker.from_env()
        
                # Pull the specified Docker image
                print(f"Pulling image: {image_name}")
                image = client.images.pull(image_name)
            
                # Output the image ID to confirm successful pull
                print(f"Image '{image_name}' pulled successfully: {image.id}")
            except docker.errors.APIError as e:
                print(f"An error occurred while pulling the image: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

        # Example usage
        image = input("enter image name:")
        pull_docker_image(image)  # Replace with any image name

    elif "docker" in ch.lower() and "launch" in ch.lower():
        import docker

        def launch_docker_container(image_name, container_name=None, ports=None, detach=True):
            """
            Launches a Docker container.

            Parameters:
            - image_name (str): The name of the Docker image to use.
            - container_name (str, optional): The name to assign to the container.
            - ports (dict, optional): A dictionary to map container ports to host ports (e.g., {'80/tcp': 8080}).
            - detach (bool, optional): Whether to run the container in detached mode (default is True).
            """
            try:
                # Initialize the Docker client
                client = docker.from_env()
        
                # Run the container
                container = client.containers.run(
                    image=image_name,
                    name=container_name,
                    ports=ports,
                    detach=detach
                )

                print(f"Container '{container_name or container.id}' launched successfully.")
                return container

            except docker.errors.ContainerError as e:
                print(f"Error: Container exited with code {e.exit_status}.")
            except docker.errors.ImageNotFound as e:
                print(f"Error: The specified image '{image_name}' was not found.")
            except docker.errors.APIError as e:
                print(f"Error: Docker API error occurred: {str(e)}")
            except Exception as e:
                print(f"An unexpected error occurred: {str(e)}")

        # Example usage
        # Example: Launch an Nginx container with port 80 mapped to host port 8080
        image_name = input("enter image name:")
        container_name = input("enter container name:")
        launch_docker_container(image_name, container_name, ports={'80/tcp': 8080})

    elif "docker" in ch.lower() and "start" in ch.lower():
        import docker

        def start_docker_container(container_name_or_id):
            """
            Starts a Docker container that is currently stopped.

            Parameters:
            - container_name_or_id (str): The name or ID of the Docker container to start.
            """
            try:
                # Initialize the Docker client
                client = docker.from_env()

                # Get the container by name or ID
                container = client.containers.get(container_name_or_id)

                # Start the container
                container.start()

                print(f"Container '{container_name_or_id}' started successfully.")

            except docker.errors.NotFound as e:
                print(f"Error: The specified container '{container_name_or_id}' was not found.")
            except docker.errors.APIError as e:
                print(f"Error: Docker API error occurred: {str(e)}")
            except Exception as e:
                print(f"An unexpected error occurred: {str(e)}")

        # Example usage
        # Example: Start a container by name or ID
        container_name_or_id = input("enter container name or id:")
        start_docker_container(container_name_or_id)

    elif "docker" in ch.lower() and "stop" in ch.lower():
        import docker

        def stop_docker_container(container_name_or_id):
            """
            Stops a running Docker container.

            Parameters:
            - container_name_or_id (str): The name or ID of the Docker container to stop.
            """
            try:
                # Initialize the Docker client
                client = docker.from_env()

                # Get the container by name or ID
                container = client.containers.get(container_name_or_id)

                # Stop the container
                container.stop()

                print(f"Container '{container_name_or_id}' stopped successfully.")

            except docker.errors.NotFound as e:
                print(f"Error: The specified container '{container_name_or_id}' was not found.")
            except docker.errors.APIError as e:
                print(f"Error: Docker API error occurred: {str(e)}")
            except Exception as e:
                print(f"An unexpected error occurred: {str(e)}")

        # Example usage
        # Example: Stop a container by name or ID
        container_name_or_id = input("enter container name or id:")
        stop_docker_container(container_name_or_id)

    elif "docker" in ch.lower() and "status" in ch.lower():
        import docker

        def get_docker_container_status(container_name_or_id):
            """
            Retrieves the status of a Docker container.

            Parameters:
            - container_name_or_id (str): The name or ID of the Docker container.

            Returns:
            - str: The status of the container (e.g., 'running', 'exited', etc.).
            """
            try:
                # Initialize the Docker client
                client = docker.from_env()

                # Get the container by name or ID
                container = client.containers.get(container_name_or_id)

                # Retrieve the container's status
                status = container.status

                print(f"Container '{container_name_or_id}' status: {status}")
                return status

            except docker.errors.NotFound as e:
                print(f"Error: The specified container '{container_name_or_id}' was not found.")
                return None
            except docker.errors.APIError as e:
                print(f"Error: Docker API error occurred: {str(e)}")
                return None
            except Exception as e:
                print(f"An unexpected error occurred: {str(e)}")
                return None

        # Example usage
        # Example: Get the status of a container by name or ID
        container_name_or_id = input("enter container name or id:")
        get_docker_container_status(container_name_or_id)

    elif ("docker" in ch.lower() and "remove" in ch.lower()) and "container" in ch.lower():
        import docker

        def remove_docker_container(container_name_or_id, force=False):
            """
            Removes a Docker container.

            Parameters:
            - container_name_or_id (str): The name or ID of the Docker container to remove.
            - force (bool): If True, force remove a running container (defaults to False).

            Returns:
            - bool: True if the container was removed successfully, False otherwise.
            """
            try:
                # Initialize the Docker client
                client = docker.from_env()
        
                # Get the container by name or ID
                container = client.containers.get(container_name_or_id)
    
                # Remove the container
                container.remove(force=force)
    
                print(f"Container '{container_name_or_id}' has been removed successfully.")
                return True

            except docker.errors.NotFound:
                print(f"Error: The specified container '{container_name_or_id}' was not found.")
                return False
            except docker.errors.APIError as e:
                print(f"Error: Docker API error occurred: {str(e)}")
                return False
            except Exception as e:
                print(f"An unexpected error occurred: {str(e)}")
                return False

        # Example usage
        #Example: Remove a container by name or ID
        container_name_or_id = input("enter container name or id:")
        remove_docker_container(container_name_or_id, force=True)

    elif "docker" in ch.lower() and "logs" in ch.lower():
        import docker

        def get_docker_logs(container_name_or_id, tail=10):
            """
            Retrieves the logs of a Docker container.
    
            Parameters:
            - container_name_or_id (str): The name or ID of the Docker container.
            - tail (int): The number of lines from the end of the logs to retrieve (default is 10).

            Returns:
            - str: The logs of the container.
            """
            try:
                # Initialize the Docker client
                client = docker.from_env()
        
                # Get the container by name or ID
                container = client.containers.get(container_name_or_id)
        
                # Retrieve the logs
                logs = container.logs(tail=tail).decode('utf-8')

                return logs
        
            except docker.errors.NotFound:
                return f"Error: The specified container '{container_name_or_id}' was not found."
            except docker.errors.APIError as e:
                return f"Error: Docker API error occurred: {str(e)}"
            except Exception as e:
                return f"An unexpected error occurred: {str(e)}"

        # Example usage
        # Example: Get the last 20 lines of logs from the container named 'my_nginx'
        container_name_or_id = input("enter container name or id:")
        logs = get_docker_logs(container_name_or_id, tail=20)
        print(logs)

    elif ("docker" in ch.lower() and "remove" in ch.lower()) and "image" in ch.lower():
        import docker

        def remove_docker_image(image_name_or_id):
            """
            Removes a Docker image.

            Parameters:
            - image_name_or_id (str): The name or ID of the Docker image to remove.
    
            Returns:
            - str: A message indicating the result of the operation.
            """
            try:
                # Initialize the Docker client
                client = docker.from_env()

                # Remove the Docker image
                client.images.remove(image=image_name_or_id)
                return f"Image '{image_name_or_id}' has been successfully removed."

            except docker.errors.ImageNotFound:
                return f"Error: The specified image '{image_name_or_id}' was not found."
            except docker.errors.APIError as e:
                return f"Error: Docker API error occurred: {str(e)}"
            except Exception as e:
                return f"An unexpected error occurred: {str(e)}"

        # Example usage
        # Example: Remove the Docker image named 'my_image'
        container_name_or_id = input("enter container name or id:")
        result = remove_docker_image(container_name_or_id)
        print(result)

    elif "dataset" in ch.lower() and "processing" in ch.lower():
        import os
        import pandas as pd
        from sklearn.model_selection import train_test_split
        from sklearn.preprocessing import StandardScaler
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.metrics import accuracy_score

        def train_random_forest(file_path, target_column):
            """
            Train a RandomForest model on a CSV dataset and return the accuracy.
    
            Parameters:
            - file_path (str): The path to the CSV file.
            - target_column (str): The name of the target column.

            Returns:
            - str: The accuracy of the model or an error message.
            """
            if not os.path.exists(file_path):
                return "Error: The specified file does not exist."

            if not file_path.endswith('.csv'):
                return "Error: The file is not a CSV file."

            df = pd.read_csv(file_path)
            
            if target_column not in df.columns:
                return "Error: Target column not found in the dataset"

            X = df.drop(target_column, axis=1)
            y = df[target_column]

            # Check if all columns are numeric
            if not all(pd.api.types.is_numeric_dtype(X[col]) for col in X.columns):
                X = pd.get_dummies(X)

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

            scaler = StandardScaler()
            X_train = scaler.fit_transform(X_train)
            X_test = scaler.transform(X_test)

            model = RandomForestClassifier(n_estimators=100, random_state=42)
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            accuracy = accuracy_score(y_test, y_pred)
    
            return f'Accuracy of the model: {accuracy:.2f}'

        # Example usage:
        file_path = input("file(.csv) path:")
        target_column = input('your_target_column:')
        result = train_random_forest(file_path, target_column)
        print(result)

    elif "upload" in ch.lower() and "s3" in ch.lower():
        import boto3
        from botocore.exceptions import NoCredentialsError, PartialCredentialsError

        def upload_to_s3(file_name, bucket_name, aws_access_key_id, aws_secret_access_key, region_name='us-east-1', s3_file_name=None):
            """
            Uploads a file to an S3 bucket.

            :param file_name: Path to the file to upload.
            :param bucket_name: Name of the S3 bucket.
            :param aws_access_key_id: AWS Access Key ID.
            :param aws_secret_access_key: AWS Secret Access Key.
            :param region_name: AWS region where the bucket is located (default: us-east-1).
            :param s3_file_name: Name of the file in the S3 bucket. If not provided, file_name is used.
            :return: True if file was uploaded, else False.
            """
            # Use file_name as s3_file_name if not provided
            if s3_file_name is None:
                s3_file_name = file_name
        
            # Create an S3 client with provided credentials
            s3 = boto3.client(
                's3',
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_secret_access_key,
                region_name=region_name
            )

            try:
                # Upload the file to the specified S3 bucket
                s3.upload_file(file_name, bucket_name, s3_file_name)
                print(f"File {file_name} uploaded to {bucket_name}/{s3_file_name}")
                return True
            except FileNotFoundError:
                print(f"The file {file_name} was not found.")
                return False
            except NoCredentialsError:
                print("Credentials not available.")
                return False
            except PartialCredentialsError:
                print("Incomplete credentials provided.")
                return False
            except Exception as e:
                print(f"An error occurred: {e}")
                return False

        file_name = input('path/to/your/file.txt :- ')
        bucket_name = input('your-s3-bucket-name :- ')
        aws_access_key_id = input('your-aws-access-key-id :- ')
        aws_secret_access_key = input('your-aws-secret-access-key :- ')
        region_name = input('your-region :- ')  # Optional, default is 'us-east-1'

        # Call the upload function
        upload_to_s3(file_name, bucket_name, aws_access_key_id, aws_secret_access_key, region_name)

    elif "exit" in ch.lower():
        break

    else:
        print("""don't know this command, following commands are available to execute:-
        NOTE:- "+" indicates that those all words should be included in the command.
               "/" indicates that you can use any of the commands written there to perform the given operation.
         0. menu :-
                show all the commands available in menu project

         1. whatsapp + send :-
                send whatsapp msg to a single person or group of people

         2. not live in jaipur / not from jaipur :-
                send whatsapp msg to those who don't live in jaipur

         3. sms / msg :-
                send sms to someone

         4. email :-
                send email to someone

         5. search / google :-
                search over google and show top 6 results as output

         6. call / phone / phone call :-
                give a phone call to someone

         7. insta :-
                to post over your instagram account

         8. purpose :-
                show the purpose section from collected data

         9. video by ipwebcam / ipwebcam / video :-
                to start a video capture from your mobile camera

        10. remote login / ssh :-
                to remote login in any OS by SSH protocol

        11. rainbow + text :-
                to convert any text in RAINBOW colors

        12. change firefox name and icon :-
                to change firefox name and logo
 
        13. launch firefox :- 
                launch firefox

        14. linear regression :-
                linear regression

        15. launch EC2 :-
                launch EC2 instances

        16. insert data in mongoDb database :-
                insert data in mongoDb database

        17. email with attached image :-
                email with attached image

        18. gemini text-to-text :-
                Gemini text-to-text

        19. click photo of whoever sit infront of the system or laptop :-
                click photo of whoever sit infront of the system or laptop

        20. speak :-
                text will get spoken by speaker

        21. telegram :-
                send msg on telegram

        22. user + add :-
                helps you to create new user and set password

        23. ascii :-
                On your cmd you print something and it will be converted to ASCII art

        24. location :-
                Find the current geo coordinates and Location

        25. docker + pull :-
                pull  docker image

        26. docker + launch :-
                launch docker container

        27. docker + start :-
                start docker container

        28. docker + stop :-
                stop docker container

        29. docker + status :-
                check status of docker container

        30. docker + remove + container :-
                remove docker container

        31. docker + logs :-
                retrieves the logs of a Docker container

        32. docker + remove + image :-
                remove docker image

        33. dataset + processing :-
                automatically does data processing on giving the dataset

        34. upload + s3 :-
                Uploading any object to s3

        35. exit :-
                to exit the program""")
