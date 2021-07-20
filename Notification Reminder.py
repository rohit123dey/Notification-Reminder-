
from plyer import notification
import time

def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = 'C:\\Users\\Rohit\\Downloads\\Paomedia-Small-N-Flat-Clock.ico',
        timeout = 10
    )

if __name__ == '__main__':
    while True:
        notifyMe('Hey Rohit,Take a break now !!!','You should follow the 20-20-20 rule to keep your eyes healthy.')
        time.sleep(2400)