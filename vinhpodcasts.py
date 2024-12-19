import requests

def download_podcast(url, output_file):
    response = requests.get(url)

    if response.status_code == 200:
        with open(output_file, "wb") as file:
            file.write(response.content)
        print(f"File downloaded successfully as {output_file}")
    else:
        print(f"Failed to download file. HTTP Status Code: {response.status_code}")


# Main
if __name__ == '__main__':
    NUMBER_OF_EPISODES = 7
    for i in range(1, NUMBER_OF_EPISODES+1):
        url = f"https://vinhgiang.s3.ap-southeast-2.amazonaws.com/Private+podcast+ep{i}.mp3"
        output_file = f"Private_podcast_ep{i}.mp3"

        download_podcast(url, output_file)
