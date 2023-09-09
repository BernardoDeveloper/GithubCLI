import requests
from convert_ascii import convert_image_to_ascii

def get_avatar(URL):
    response = requests.get(URL)
    if response.status_code == 200:
        # Download github avatar
        img_url = response.json().get("avatar_url")

        path_img = "image.jpg"
        fp = open(path_img, "wb")
        fp.write(requests.get(img_url).content)
        fp.close()

        print(convert_image_to_ascii(path_img))
    else:
        print("Failed to request")
        
