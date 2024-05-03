import requests

def free_api_handling():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    
    # print(data)
    
    if data["success"] and "data" in data:
        # username = data['data']['content']
        user_data = data["data"]
        username = user_data['login']['username']
        country = user_data['location']['country']
        # joke = data.data.username
        return username, country
    else:
        raise Exception ("Unable to fetch data from api")

def main():
    try:
        username , country= free_api_handling()
        print(f"username: {username} \n country: {country}")
    except Exception as e:
        print(str(e))

       
if __name__ == "__main__":
    main()