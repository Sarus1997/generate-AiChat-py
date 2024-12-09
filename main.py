import requests

API_KEY = "AIzaSyCsIn3X8MsQb1eI_8EfFT10dsjFrlIp2J4"
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"

headers = {
    "Content-Type": "application/json"
}

data = {
    "contents": [
        {
            "parts": [
                {"text": "รู้จักณัชนน เจียรมาศไหม"}
            ]
        }
    ]
}

def generate_content():
    try:
        # ส่งคำขอ POST
        response = requests.post(f"{url}?key={API_KEY}", headers=headers, json=data)
        
        # แสดงข้อมูลการตอบกลับทั้งหมด
        print("Status Code:", response.status_code)
        print("Response Text:", response.text)
        
        # ตรวจสอบสถานะคำขอ
        if response.status_code == 200:
            print("Response JSON:", response.json())
        else:
            print(f"Error {response.status_code}: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

# เรียกใช้งานฟังก์ชัน
generate_content()
