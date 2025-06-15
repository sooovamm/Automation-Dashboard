def video_ipwebcam():
        import cv2
        cap = cv2.VideoCapture("http://100.112.173.51:8080/video")
        while True:
            status1, photo = cap.read()
            cv2.imshow("", photo)
            if cv2.waitKey(8) == 13:
                break
        cv2.destroyAllWindows()

def rainbow_text(text):
        from termcolor import colored
        import colorama
        # Initialize colorama for Windows support
        colorama.init()

        # Define the text and the colors
        #text = input()
        colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']

        # Print each letter in a different color
        for i, letter in enumerate(text):
            color = colors[i % len(colors)]
            print(colored(letter, color), end='')

        # Print a newline at the end
        print()
