def ssh_login(hostname, port, username, password, command):
        import paramiko
        # Create an SSH client
        ssh = paramiko.SSHClient()

        # Automatically add the remote server's SSH key to known_hosts
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            # Connect to the remote server
            ssh.connect(hostname, port, username, password)
            print(f"Connected to {hostname}")

            # Execute the command
            stdin, stdout, stderr = ssh.exec_command(command)
            print(f"Command executed: {command}")

            # Read the output from stdout
            output = stdout.read().decode()
            print("Output:")
            print(output)

            # Read the output from stderr (if any)
            error = stderr.read().decode()
            if error:
                print("Error:")
                print(error)
        except Exception as e:
            print(f"Failed to connect to {hostname}: {e}")

        finally:
            # Close the connection
            ssh.close()
            print("Connection closed")

def send_file_to_remote(hostname, port, username, password):
        # Define the file paths
        local_file_path = input('path/to/local/file:')
        remote_file_path = input('path/to/remote/destination/file:')

        # Create a new SSH client
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            # Connect to the remote host
            client.connect(hostname, port, username, password)

            # Create an SFTP client from the existing SSH connection
            sftp = client.open_sftp()

            # Copy the local file to the remote host
            sftp.put(local_file_path, remote_file_path)

            print(f"File {local_file_path} successfully copied to {remote_file_path}")

        finally:
            # Close the SFTP client and SSH connection
            sftp.close()
            client.close()


