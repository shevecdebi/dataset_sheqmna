import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_images(url, output_folder='downloaded_images'):    # output_folder='ფოლდერის_სახელი'
    # შეიქმნას ახალი ფოლდერი თუ არ არსებობდა
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # GET რექვესთის გაგზავნა
    response = requests.get(url)

    # ამოწმებს რექვესთის წარმატებას (status code 200)
    if response.status_code == 200:
        # HTML-ს გაპარსვა
        soup = BeautifulSoup(response.text, 'html.parser')

        # ყველა image tag-ის პოვნა 
        img_tags = soup.find_all('img')

        # ყოველი ფოტოს გადმოწერა და შენახვა
        for i, img_tag in enumerate(img_tags, start=1):
            img_url = img_tag.get('src')
            if img_url:
                img_url = urljoin(url, img_url)
                img_data = requests.get(img_url).content

                # ფოტოს შენახვა კონკრეტული სახელით
                img_filename = os.path.join(output_folder, f"{i}.jpg")  # შეგიძლია i+15
                # დაწერო თუ გინდა რომ 16 ით დაიწყოს სახელების ათვლა

                # ფოტოს ლოკალურად შენახვა
                with open(img_filename, 'wb') as img_file:
                    img_file.write(img_data)
                    print(f"Downloaded: {img_filename}")
    else:
        print(f"პრობლემა შეიქმნა. Status code: {response.status_code}")

# შეცვალე raime.ge
url_to_scrape = 'raime.ge'
download_images(url_to_scrape)
