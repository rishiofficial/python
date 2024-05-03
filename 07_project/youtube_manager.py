import json

def load_data():
    try:
        with open("youtube.txt", 'r') as file:
         test = json.load(file)
         return test
    except FileNotFoundError:
       return []


def save_video_data(videos):
    with open("youtube.txt",'w') as file:
        json.dump(videos, file)

def list_all_video(videos):
    print('\n')
    for index, video in enumerate(videos, start=1):
        print(f"{index} .{video['name']} ,Duration: {video['time']}")

def add_video(videos):
    name =input('please add name of video: ')
    time= input('Enter a duration of video: ')
    videos.append({'name': name , 'time': time})
    save_video_data(videos)

def update_video(videos):
    list_all_video(videos)
    index = int(input("Enter the index of the video"))
    if 1<= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index - 1] = ({'name': name, "time": time})
        save_video_data(videos)
    else:
        print("Invalid syntax")


def delete_video(videos):
    list_all_video(videos)
    index = int(input("Enter the index of video to delete: "))
    if 1<= index <= len(videos):
        del videos[index-1]
        save_video_data(videos)
    else:
        print("Invalid index")
    

    

def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_video(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                "Invalid choice"

if __name__ == "__main__":
    main()