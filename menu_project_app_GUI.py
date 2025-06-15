from flask import Flask, render_template, request, redirect, url_for, jsonify, send_file
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


#import pywhatkit as kit
import time

#import pywhatkit as w
import pyautogui
import keyboard as k

from twilio.rest import Client

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule

import os
import subprocess
import docker

import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

from googlesearch import search

import geocoder

from instagrapi import Client
from datetime import datetime, timedelta
import threading

from telethon import TelegramClient
import asyncio

from email.mime.application import MIMEApplication

import cv2
import mediapipe as mp

from gtts import gTTS
import playsound

import pyfiglet

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/whatsapp')
def whatsapp():
    return render_template('whatsapp.html')

@app.route('/sms')
def sms():
    return render_template('sms.html')

@app.route('/email')
def email():
    return render_template('email.html')

@app.route('/phone_call')
def phone_call():
    return render_template('phone_call.html')

@app.route('/docker_pull')
def docker_pull():
    return render_template('docker_pull.html')

@app.route('/docker_launch')
def docker_launch():
    return render_template('docker_launch.html')

@app.route('/docker_start')
def docker_start():
    return render_template('docker_start.html')

@app.route('/docker_stop')
def docker_stop():
    return render_template('docker_stop.html')

@app.route('/docker_remove_c')
def docker_remove_c():
    return render_template('docker_remove_c.html')

@app.route('/docker_status')
def docker_status():
    return render_template('docker_status.html')

@app.route('/docker_logs')
def docker_logs():
    return render_template('docker_logs.html')

@app.route('/docker_remove_i')
def docker_remove_i():
    return render_template('docker_remove_i.html')

@app.route('/aws_s3')
def aws_s3():
    return render_template('aws_s3.html')

@app.route('/aws_ec2')
def aws_ec2():
    return render_template('aws_ec2.html')

@app.route('/google')
def google():
    return render_template('google_search.html')

@app.route('/google_results')
def google_results():
    return render_template('google_search_results.html')

@app.route('/jsvid')
def jsvid():
    return render_template('jsvid.html')

@app.route('/location')
def location():
    return render_template('location.html')

@app.route('/instagram')
def instagram():
    return render_template('instagram.html')

@app.route('/telegram')
def telegram():
    return render_template('telegram.html')

@app.route('/email_with_image')
def email_with_image():
    return render_template('/email_with_image.html')

@app.route('/secure_your_laptop')
def secure_your_laptop():
    return render_template('secure_your_laptop.html')

@app.route('/tts_m1')
def tts_m1():
    return render_template('tts_m1.html')

@app.route('/tts_m2')
def tts_m2():
    return render_template('tts_m2.html')

@app.route('/ascii_art')
def ascii_art():
    return render_template('ascii_art.html')

@app.route('/processing_dataset')
def processing_dataset():
    return render_template('processing_dataset.html')


@app.route('/send_whatsapp_message', methods=['GET', 'POST'])
def send_whatsapp_message():
    if request.method == 'POST':
        group_msg = request.form.get('group_msg')
        if group_msg == 'n':
            monumb = request.form.get('monumb')
            msg = request.form.get('msg')
            time_h = request.form.get('time_h')
            time_m = request.form.get('time_m')
            if time_h and time_m:
                kit.sendwhatmsg(monumb, msg, int(time_h), int(time_m))
            else:
                kit.sendwhatmsg_instantly(monumb, msg)
            pyautogui.click(1134, 1020)
            time.sleep(45)
            k.press_and_release('enter')
            k.press_and_release('enter')
            k.press_and_release('enter')
        else:
            numbers = request.form.get('numbers').split(',')
            msg = request.form.get('msg')
            time_h = request.form.get('time_h')
            time_m = request.form.get('time_m')

            def send_whatsapp_message(number, message):
                try:
                    if time_h and time_m:
                        kit.sendwhatmsg(number, message, int(time_h), int(time_m))
                    else:
                        kit.sendwhatmsg_instantly(number, message)
                    print(f"Message sent to {number}")
                except Exception as e:
                    print(f"Failed to send message to {number}: {e}")

            for number in numbers:
                send_whatsapp_message(number.strip(), msg)
                time.sleep(40)
            pyautogui.click(1134, 1009)
            time.sleep(2)
            k.press_and_release('enter')

        #return redirect(url_for('home'))

    return render_template('index.html')

@app.route('/send_sms', methods=['GET', 'POST'])
def send_sms():
    if request.method == 'POST':
        # Get form data
        account_sid = request.form.get('account_sid')
        auth_token = request.form.get('auth_token')
        twilio_number = request.form.get('twilio_number')
        to_number = request.form.get('to_number')
        message_body = request.form.get('message_body')

        # Initialize the Twilio Client
        client = Client(account_sid, auth_token)

        # Send the message
        try:
            message = client.messages.create(
                body=message_body,
                from_=twilio_number,
                to=to_number
            )
            return f"Message sent: {message.body}"
        except Exception as e:
            return f"Failed to send message: {e}"

    return render_template('index.html')

def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject if subject else "No Subject"
        message.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())
        server.close()

        return "Email sent successfully!"
    except Exception as e:
        return f"Failed to send email: {e}"

def schedule_email(sender_email, sender_password, recipient_email, subject, body, send_time):
    schedule.every().day.at(send_time).do(send_email, sender_email, sender_password, recipient_email, subject, body)
    while True:
        schedule.run_pending()
        time.sleep(1)

@app.route('/send_email', methods=['GET', 'POST'])
def send_email_flask():
    print(request.method) # This will print the method used to access the route
    if request.method == 'POST':
        sender_email = request.form.get('sender_email')
        sender_password = request.form.get('sender_password')
        recipient_email = request.form.get('recipient_email')
        subject = request.form.get('subject')
        body = request.form.get('body')
        schedule_time = request.form.get('schedule_time')

        if schedule_time:
            # Schedule the email
            schedule_email(sender_email, sender_password, recipient_email, subject, body, schedule_time)
            return f"Email scheduled to be sent at {schedule_time}!"
        else:
            # Send the email immediately
            result = send_email(sender_email, sender_password, recipient_email, subject, body)
            return result

    print(request.method)
    return render_template('index.html')

@app.route('/make_phone_call', methods=['GET', 'POST'])
def make_phone_call():
    # Get form data
    account_sid = request.form.get('account_sid')
    auth_token = request.form.get('auth_token')
    twilio_number = request.form.get('twilio_number')
    receiver_number = request.form.get('receiver_number')
    message = request.form.get('message')

    try:
        # Initialize Twilio client
        client = Client(account_sid, auth_token)

        # Make a call using the Twilio API
        call = client.calls.create(
            twiml=f'<Response><Say>{message}</Say></Response>',
            to=receiver_number,
            from_=twilio_number
        )

        return f"Call initiated successfully! Call SID: {call.sid}"

    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/docker_pull_image', methods=['POST'])
def pull_image():
    # Initialize Docker client
    client = docker.from_env()
    image_name = request.form.get('image_name')
    
    try:
        # Pull the image from Docker Hub
        image = client.images.pull(image_name)
        return f"Successfully pulled Docker image: {image_name}"
    
    except Exception as e:
        return f"Failed to pull image. Error: {str(e)}"

@app.route('/docker_launch_container', methods=['POST'])
def launch_container():
    image_name = request.form['image_name']
    container_name = request.form['container_name']
    detach_mode = request.form['detach']

    if not container_name:
        # Use a random name if the user didn't provide one
        container_name_option = ""
    else:
        container_name_option = f'--name {container_name}'

    if detach_mode == 'yes':
        # Launch the container in detached mode
        command = f'docker run -d {container_name_option} {image_name}'
        subprocess.run(command, shell=True)
        return f"Container '{container_name or '[Auto-generated Name]'}' launched in detached mode!"
    else:
        # Launch the container interactively
        command = f'docker run -it {container_name_option} {image_name}'
        subprocess.run(['gnome-terminal', '--', 'bash', '-c', command])
        return f"Container '{container_name or '[Auto-generated Name]'}' launched in interactive mode!"

@app.route('/docker_start_container', methods=['POST'])
def start_container():
    container_name = request.form['container_name']
    
    if not container_name:
        return "Container name is required to start a container."

    # Start the Docker container
    try:
        # Start the container in detached mode
        start_command = f'docker start {container_name}'
        start_result = subprocess.run(start_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        start_output = start_result.stdout.decode('utf-8')
        start_error = start_result.stderr.decode('utf-8')

        if start_error:
            return f"Error starting container: {start_error}"

        # Open a new terminal and attach to the container
        attach_command = f'gnome-terminal -- bash -c "docker exec -it {container_name} /bin/bash; exec bash"'
        subprocess.run(attach_command, shell=True)

        return f"Container '{container_name}' started successfully and terminal opened."
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/docker_stop_container', methods=['GET', 'POST'])
def stop_container():
    if request.method == 'POST':
        # Initialize Docker client
        client = docker.from_env()
        container_id = request.form['container_id']
        try:
            # Find and stop the container by ID or name
            container = client.containers.get(container_id)
            container.stop()
            return f"Container {container_id} stopped successfully."
        except Exception as e:
            return f"Error: {str(e)}"
    return render_template('index.html')

@app.route('/docker_remove_container', methods=['GET', 'POST'])
def remove_container():
    # Initialize Docker client
    client = docker.from_env()
    if request.method == 'POST':
        container_id = request.form['container_id']
        try:
            # Find and remove the container by ID or name
            container = client.containers.get(container_id)
            container.remove(force=True)
            return f"Container {container_id} removed successfully."
        except Exception as e:
            return f"Error: {str(e)}"
    return render_template('index.html')

@app.route('/docker_status_check', methods=['POST'])
def check_status():
    client = docker.from_env()
    container_id = request.form['container_id']
    try:
        if container_id:
            # Get a specific container
            container = client.containers.get(container_id)
            status = container.status
            return jsonify({'status': status, 'id': container_id})
        else:
            # Get all containers
            containers = client.containers.list(all=True)
            container_status = [{'id': container.short_id, 'name': container.name, 'status': container.status} for container in containers]
            return jsonify({'containers': container_status})
    except Exception as e:
        # Return the error message in JSON format
        return jsonify({'error': str(e)})

@app.route('/docker_logs_check', methods=['POST'])
def check_logs():
    client = docker.from_env()
    container_id = request.form['container_id']
    try:
        container = client.containers.get(container_id)
        logs = container.logs().decode('utf-8')
        return jsonify({'status': 'success', 'logs': logs})
    except docker.errors.NotFound:
        return jsonify({'status': 'error', 'message': 'Container not found'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/docker_remove_image', methods=['POST'])
def remove_image():
    client = docker.from_env()
    image_id = request.form['image_id']
    try:
        client.images.remove(image=image_id)
        return jsonify({'status': 'success', 'message': f'Docker image {image_id} removed successfully.'})
    except docker.errors.ImageNotFound:
        return jsonify({'status': 'error', 'message': 'Image not found'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/aws_s3_upload', methods=['POST'])
def upload_file():
    aws_access_key_id = request.form.get('aws_access_key_id')
    aws_secret_access_key = request.form.get('aws_secret_access_key')
    bucket_name = request.form.get('bucket_name')
    file = request.files.get('file')

    if not file:
        result = 'No file selected.'
        return render_template('aws_s3.html', result=result)

    try:
        # Initialize S3 client
        s3 = boto3.client('s3', 
                          aws_access_key_id=aws_access_key_id, 
                          aws_secret_access_key=aws_secret_access_key)

        # Upload the file
        s3.upload_fileobj(file, bucket_name, file.filename)
        result = 'File uploaded successfully!'
    
    except NoCredentialsError:
        result = 'Credentials not available.'
    
    except PartialCredentialsError:
        result = 'Incomplete credentials provided.'
    
    except Exception as e:
        result = f'Error: {str(e)}'
    
    return result

# AWS EC2 instance launch route
@app.route('/aws_ec2_launch', methods=['GET', 'POST'])
def launch_ec2():
    if request.method == 'POST':
        # Collect AWS credentials and other form data
        aws_access_key_id = request.form['aws_access_key_id']
        aws_secret_access_key = request.form['aws_secret_access_key']
        region = request.form['region'] or request.form['custom_region']
        instance_type = request.form.get('custom_instance_type') or request.form['instance_type']
        security_group = request.form.get('custom_security_group') or request.form['security_group']
        ami_id = request.form.get('custom_ami_id') or request.form['ami_id']
        instance_count = int(request.form['instance_count'])

        # Create EC2 client using the provided AWS credentials and region
        ec2 = boto3.client(
            'ec2',
            region_name=region,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )

        try:
            # Launch EC2 instances
            instances = ec2.run_instances(
                ImageId=ami_id,
                MinCount=1,
                MaxCount=instance_count,
                InstanceType=instance_type,
                SecurityGroupIds=[security_group]
            )
            instance_ids = [instance['InstanceId'] for instance in instances['Instances']]
            return f"Successfully launched EC2 instance(s): {', '.join(instance_ids)}"
        
        except Exception as e:
            return f"Error: {str(e)}"

# Global variables to manage pagination
SEARCH_RESULTS = []
START_INDEX = 0
RESULTS_PER_PAGE = 5

@app.route('/google_search', methods=['GET', 'POST'])
def google_search():
    global SEARCH_RESULTS, START_INDEX
    if request.method == 'POST':
        query = request.form['query']
        # Perform Google search
        SEARCH_RESULTS = list(search(query, num_results=100))  # Fetching more results for pagination
        START_INDEX = 0
        return redirect(url_for('google_search_results'))

    return render_template('index.html')

@app.route('/google_search_results', methods=['GET'])
def google_search_results():
    global SEARCH_RESULTS, START_INDEX

    # Get the current page's results
    end_index = START_INDEX + RESULTS_PER_PAGE
    current_results = SEARCH_RESULTS[START_INDEX:end_index]

    # Determine if there are previous/next pages
    has_prev = START_INDEX > 0
    has_next = end_index < len(SEARCH_RESULTS)

    return render_template('google_search_results.html', results=current_results, has_prev=has_prev, has_next=has_next)

@app.route('/google_search_prev')
def google_search_prev_page():
    global START_INDEX
    if START_INDEX > 0:
        START_INDEX -= RESULTS_PER_PAGE
    return redirect(url_for('google_search_results'))

@app.route('/google_search_next')
def google_search_next_page():
    global START_INDEX
    if START_INDEX + RESULTS_PER_PAGE < len(SEARCH_RESULTS):
        START_INDEX += RESULTS_PER_PAGE
    return redirect(url_for('google_search_results'))

# Save video route
@app.route('/save_video', methods=['POST'])
def save_video():
    if 'video_data' in request.files:
        video = request.files['video_data']
        video.save(os.path.join('static', video.filename))
        return jsonify({"message": "Video saved successfully!", "video_path": f'static/{video.filename}'})
    return jsonify({"message": "No video received"}), 400

@app.route('/location_get')
def get_location():
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
    return jsonify(location_info)

@app.route('/instagram_post', methods=['POST'])
def post_to_instagram():
    username = request.form.get('username')
    password = request.form.get('password')
    media_type = request.form.get('media_type')
    media_path = request.form.get('media_path')
    caption = request.form.get('caption')
    post_now = request.form.get('post_now') == 'yes'
    schedule_time = request.form.get('schedule_time')

    def upload_media(username, password, media_type, media_path, caption, scheduled_time=None):
        # Log in to Instagram using user credentials
        client = Client()
        client.login(username, password)
    
        # Function to post immediately or after a delay (for scheduling)
        def post_now():
            if media_type == 'image':
                client.photo_upload(media_path, caption)
            elif media_type == 'video':
                client.video_upload(media_path, caption)
            elif media_type == 'carousel':
                media_paths = media_path.split(',')
                client.album_upload(media_paths, caption)
    
        # If scheduled, wait until the scheduled time to post
        if scheduled_time:
            time_diff = scheduled_time - datetime.now()
            delay = time_diff.total_seconds()
            threading.Timer(delay, post_now).start()
        else:
            post_now()

    if not post_now and schedule_time:
        schedule_time = datetime.strptime(schedule_time, '%Y-%m-%dT%H:%M')
    else:
        schedule_time = None

    upload_media(username, password, media_type, media_path, caption, schedule_time)
    
    return jsonify({"message": "Post scheduled successfully!" if schedule_time else "Post uploaded successfully!"})

@app.route('/telegram_post', methods=['POST'])
async def post_to_telegram():
    api_id = request.form.get('api_id')
    api_hash = request.form.get('api_hash')
    phone_number = request.form.get('phone_number')
    recipient = request.form.get('recipient')
    message_text = request.form.get('message_text')
    media_type = request.form.get('media_type')
    media_path = request.form.get('media_path')
    post_now = request.form.get('post_now') == 'yes'
    schedule_time = request.form.get('schedule_time')

    # Function to send the Telegram message or media asynchronously
    async def send_telegram_message(api_id, api_hash, phone_number, recipient, message_text=None, media_path=None, delay=None):
        client = TelegramClient('session_name', api_id, api_hash)

        await client.start(phone=phone_number)

        if delay:
            await asyncio.sleep(delay)

        if media_path:
            if isinstance(media_path, list):  # for multiple media (like images or videos)
                await client.send_file(recipient, media_path, caption=message_text)
            else:
                await client.send_file(recipient, media_path, caption=message_text)
        else:
            await client.send_message(recipient, message_text)

        await client.disconnect()

    if not post_now and schedule_time:
        schedule_time = datetime.strptime(schedule_time, '%Y-%m-%dT%H:%M')
        time_diff = (schedule_time - datetime.now()).total_seconds()
    else:
        time_diff = 0  # Post immediately if post_now is true

    media_files = None
    if media_type in ['image', 'video', 'multiple']:
        media_files = media_path.split(',') if media_type == 'multiple' else media_path

    # Call the asynchronous function to send the message
    await send_telegram_message(api_id, api_hash, phone_number, recipient, message_text, media_files, time_diff)

    return jsonify({"message": "Post scheduled successfully!" if time_diff > 0 else "Post uploaded successfully!"})

@app.route('/email_with_image_send', methods=['POST'])
def send_email():
    sender_email = request.form['sender_email']
    receiver_email = request.form['receiver_email']
    email_password = request.form['email_password']
    subject = request.form['subject']
    message_body = request.form['message_body']
    image = request.files['image']

    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message_body, 'plain'))

        # Attach image
        if image:
            attachment = MIMEApplication(image.read())
            attachment.add_header('Content-Disposition', 'attachment', filename=image.filename)
            msg.attach(attachment)

        # Send email
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, email_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        
        return "Email sent successfully!"

    except Exception as e:
        return f"Failed to send email: {str(e)}"


# Initialize global variable to control the camera
stop_capture = False
# Route to handle form submission
@app.route('/secure_your_laptop_run', methods=['POST'])
def secure_your_laptop_run():
    #Function to capture and save photo when a new person is detected
    def capture_photos_continuously(save_path):
        global stop_capture
        # Initialize the webcam
        cap = cv2.VideoCapture(0)
        # Initialize the MediaPipe Face Detection
        mp_face_detection = mp.solutions.face_detection
        face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)
        
        # Variable to hold previous detection result for comparison
        previous_faces = None
        photo_counter = 0

        while not stop_capture:
            success, frame = cap.read()
            if success:
                # Convert the frame to RGB
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # Perform face detection
                results = face_detection.process(rgb_frame)

                # Check if a face is detected
                current_faces = results.detections if results.detections else None

                # If a new face is detected, save the image
                if current_faces and current_faces != previous_faces:
                    previous_faces = current_faces
                    photo_counter += 1
                    filename = os.path.join(save_path, f'intruder_{photo_counter}.jpg')
                    cv2.imwrite(filename, frame)
                    print(f"Photo saved as {filename}")

                # If no face is detected, reset the previous face detection
                elif not current_faces:
                    previous_faces = None
            else:
                print("Failed to capture image.")
                break

        cap.release()

    global stop_capture
    stop_capture = False
    save_path = request.form['save_path']
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    # Start capturing photos continuously
    capture_photos_continuously(save_path)
    
    return "Monitoring started. Close the window to stop."

# Route to stop the capture
@app.route('/secure_your_laptop_stop', methods=['POST'])
def stop_capture_route():
    global stop_capture
    stop_capture = True
    return "Monitoring stopped, camera released."

@app.route('/tts_m1_speak', methods=['POST'])
def speak():
    # Get user input from the form
    text = request.form['text']
    language = request.form['language']
    action = request.form['action']

    # Function to convert text to speech
    def convert_text_to_speech(text, language, save_path):
        tts = gTTS(text=text, lang=language)
        tts.save(save_path)

    # Filepath to save the TTS output
    save_path = os.path.join('static', 'audio/output.mp3')
    
    # Convert text to speech and save the file
    convert_text_to_speech(text, language, save_path)

    # Preview the speech output
    if action == 'preview':
        # Pass the audio file path to the template
        return render_template('tts_m1.html', audio_file=url_for('static', filename='audio/output.mp3'))

    # Save the speech output
    elif action == 'save':
        return send_file(save_path, as_attachment=True)

@app.route('/ascii_art_convert', methods=['POST'])
def convert():
    # Get user input from the form
    text = request.form['text']

    # Function to convert text to ASCII art
    def convert_to_ascii(text):
        return pyfiglet.figlet_format(text)

    # Convert text to ASCII art
    ascii_art = convert_to_ascii(text)

    # Render the ASCII art in the frontend
    return render_template('ascii_art.html', ascii_art=ascii_art)

@app.route('/processing_dataset_test', methods=['POST'])
def processing_dataset_test():
    if request.method == 'POST':
        file = request.files['file']
        target_column = request.form.get('target')
        
        if file and file.filename.endswith('.csv'):
            # Setup folder to save uploaded files
            upload_folder = 'uploads'
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)
            file_path = os.path.join(upload_folder, file.filename)
            file.save(file_path)
            
            # Load dataset
            df = pd.read_csv(file_path)
            
            # Check if target column exists
            if target_column not in df.columns:
                return "Error: Target column not found in the dataset", 400
            
            # Split features and target
            X = df.drop(target_column, axis=1)
            y = df[target_column]
            
            # Handle categorical variables if any
            if not all(pd.api.types.is_numeric_dtype(X[col]) for col in X.columns):
                X = pd.get_dummies(X)
            
            # Train-test split
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
            
            # Scale the features
            scaler = StandardScaler()
            X_train = scaler.fit_transform(X_train)
            X_test = scaler.transform(X_test)
            
            # Use RandomForestRegressor for continuous target variable
            model = RandomForestRegressor(n_estimators=100, random_state=42)
            model.fit(X_train, y_train)
            
            # Predict and calculate performance
            y_pred = model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            
            return f'Mean Squared Error of the model: {mse:.2f}'
    
    return 'Please upload a CSV file and specify the target column.'


if __name__ == '__main__':
    app.run(debug=True)

