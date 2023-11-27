import os

def rename_images(folder_path='resized_images', start_index=1012):    # start_index რომელი ინდექსიდან დაიწყება გადარქმევა
    # ყველა ფაილის ლისტის მიღება
    files = os.listdir(folder_path)

    # ყველა ფაილზე ჩამოვლა
    for i, filename in enumerate(files, start=start_index):
        # ახალი ფაილის სახელი
        new_filename = f"{i}.jpg"

        # ახალი ადგილის შექმნა ძველი და ახალი ფაილების სახელებისთვის 
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)

        # ფაილის გადარქმევა
        os.rename(old_path, new_path)

        print(f"გადაერქვა: {old_path} დაერქვა {new_path}")


rename_images()
