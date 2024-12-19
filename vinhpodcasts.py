import requests
import os

def download_podcast(url, output_file):
    response = requests.get(url)

    if response.status_code == 200:
        abs_path = os.path.abspath(output_file)
        with open(abs_path, "wb") as file:
            file.write(response.content)
        
        if os.path.getsize(abs_path) > 0:
            print(f"File {abs_path} downloaded successfully.")
        else:
            print(f"File {abs_path} is empty after download.")
    else:
        print(f"Failed to download file. HTTP Status Code: {response.status_code}")


# Main
if __name__ == '__main__':
    NUMBER_OF_EPISODES = 7
    for i in range(1, NUMBER_OF_EPISODES + 1):
        url = f"https://vinhgiang.s3.ap-southeast-2.amazonaws.com/Private+podcast+ep{i}.mp3"
        output_file = f"Private_podcast_ep{i}.mp3"

        download_podcast(url, output_file)

    print("\nFiles in current directory:")
    print(os.listdir())
