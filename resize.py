from PIL import Image
import os
                  # იმ ფოლდერის სახელი სადაც ფოტოებია   || output ის ფოლდერი
def resize_images(input_folder='downloaded_images', output_folder='resized_images', size=(200, 200)): # size=(რამდენი,რამდენზე)
    # output ისთვის ფოლდერის შექმნა თუ არ არსებობს
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # ყველა ფაილზე გადავლა
    for filename in os.listdir(input_folder):
        # ამოწმებს არის თუ არ ფაილი ფოტო (შეგიძლია მეტი გაფართოების დამატება)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # ფოტოს გახსნა
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)

            # RGB ში გადაყვანა
            img = img.convert('RGB')

            # ზომის შეცვლა
            img_resized = img.resize(size)

            # output ის ფაილის სახელის შექმნა
            output_path = os.path.join(output_folder, filename)

            # შეცვლილი ფოტოს შენახვა
            img_resized.save(output_path)
 
resize_images()
