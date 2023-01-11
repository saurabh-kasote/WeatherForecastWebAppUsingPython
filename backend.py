API_Key = "141710af2113bab9f55ef73e1bcd33d5"
import requests

def get_data(city,days=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_Key}&units=metric"
    response = requests.get(url=url)
    data = response.json()
    filtered_data = data["list"]
    filtered_data = filtered_data[:8*days]
    return filtered_data

if __name__=="__main__":
    print(get_data("kolhapur",5))