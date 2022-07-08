import requests


def send_message(phone_number, message):
    requests.get(
        f"http://ws3584.isms.ir/sendWS?username=7bluesky&password=@7BS123456&mobiles[]={phone_number}&body={message}"
    )
