import requests
import tkinter as tk
from tkinter import messagebox, ttk

# API Configuration
API_KEY = "AIzaSyCsIn3X8MsQb1eI_8EfFT10dsjFrlIp2J4"
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"

headers = {
    "Content-Type": "application/json"
}

def generate_content():
    # รับข้อความจาก Input Field
    user_input = input_field.get()
    if not user_input.strip():
        messagebox.showerror("Error", "กรุณาป้อนข้อความ")
        return

    data = {
        "contents": [
            {
                "parts": [
                    {"text": user_input}
                ]
            }
        ]
    }

    try:
        # ส่งคำขอ POST
        response = requests.post(f"{url}?key={API_KEY}", headers=headers, json=data)
        
        # แสดงผลลัพธ์ใน GUI
        if response.status_code == 200:
            result = response.json()
            output_text.set(result)
        else:
            messagebox.showerror("Error", f"API Request Failed: {response.status_code}\n{response.text}")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Request failed: {e}")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("API Generator")
root.geometry("500x400")
root.configure(bg="#f2f2f2")

# ส่วนหัว
header_label = tk.Label(root, text="Generative Language API", font=("Helvetica", 16), bg="#f2f2f2", fg="#333")
header_label.pack(pady=10)

# Input Field
input_label = tk.Label(root, text="ป้อนข้อความ:", font=("Helvetica", 12), bg="#f2f2f2", fg="#333")
input_label.pack(anchor="w", padx=20)
input_field = tk.Entry(root, font=("Helvetica", 12), width=50)
input_field.pack(pady=5, padx=20)

# Button
generate_button = tk.Button(root, text="Generate", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=generate_content)
generate_button.pack(pady=10)

# Output Field
output_label = tk.Label(root, text="ผลลัพธ์:", font=("Helvetica", 12), bg="#f2f2f2", fg="#333")
output_label.pack(anchor="w", padx=20)
output_text = tk.StringVar()
output_box = ttk.Label(root, textvariable=output_text, font=("Helvetica", 12), background="white", anchor="w", relief="sunken")
output_box.pack(pady=5, padx=20, fill="x")

# เริ่มการทำงาน
root.mainloop()
