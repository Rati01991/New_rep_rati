# #1.დაწერეთ პროგრამა, რომელიც ქმნის ორ ძაფს (Thread) 30-დან 50-ის ჩათვლით ლუწი და კენტი რიცხვების მოსაძებნად. 
# # შედეგი დაბეჭდეთ ეკრანზე
# import threading

# def print_even():
#     for i in range(30, 51):
#         if i % 2 == 0:
#             print("Even number:", i)

# def print_odd():
#     for i in range(30, 51):
#         if i % 2 != 0:
#             print("Odd number:", i)

# if __name__ == "__main__":
    
#     even_thread = threading.Thread(target=print_even)
#     odd_thread = threading.Thread(target=print_odd)

    
#     even_thread.start()
#     odd_thread.start()

    
#     even_thread.join()
#     odd_thread.join()

#     print("Done!")

##2.დაწერეთ პროგრამა, რომელიც ქმნის რამდენიმე ძაფს (Thread) და იწერს რამდენიმე mp3 ფაილს ინტერნეტიდან.

# import threading
# import requests
# import os

# def download_mp3(url, filename):
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             with open(filename, 'wb') as f:
#                 f.write(response.content)
#             print(f"Downloaded {filename}")
#         else:
#             print(f"Failed to download {filename}. Status code: {response.status_code}")
#     except Exception as e:
#         print(f"Error downloading {filename}: {str(e)}")

# if __name__ == "__main__":
#     mp3_urls = [
#         "https://example.com.mp3",
#     ]

#     if not os.path.exists("mp3_files"):
#         os.makedirs("mp3_files")

#     threads = []
#     for i, url in enumerate(mp3_urls):
#         filename = f"mp3_files/song{i+1}.mp3"
#         thread = threading.Thread(target=download_mp3, args=(url, filename))
#         thread.start()
#         threads.append(thread)

#     for thread in threads:
#         thread.join()

#     print("All downloads completed.")


