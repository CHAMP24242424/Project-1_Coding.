import tkinter as tk
from tkinter import messagebox

# ฟังก์ชันคำนวณค่าโดยสาร
def calculate_fare(distance):
    base_fare = 10
    try:
        distance = float(distance)
        if distance <= 5:
            fare = base_fare
        elif 6 <= distance <= 10:
            fare = base_fare + 2
        elif 11 <= distance <= 15:
            fare = base_fare + 4
        elif 16 <= distance <= 20:
            fare = base_fare + 6
        elif 21 <= distance <= 25:
            fare = base_fare + 8
        elif 26 <= distance <= 30:
            fare = base_fare + 10
        elif 31 <= distance <= 36:
            fare = base_fare + 12
        else:
            fare = "ไม่รองรับระยะทางเกิน 36 กม."
        return fare
    except ValueError:
        return "กรุณากรอกตัวเลขที่ถูกต้อง"

# ฟังก์ชันเมื่อกดปุ่มคำนวณ
def on_calculate():
    distance = entry_distance.get()
    fare = calculate_fare(distance)
    messagebox.showinfo("ค่าโดยสาร", f"ค่าโดยสารสำหรับ {distance} กม. คือ {fare} บาท")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("โปรแกรมคำนวณค่าโดยสาร")
root.geometry("450x400")
root.configure(bg="#2C3E50")

# พื้นหลัง Gradient
canvas = tk.Canvas(root, width=450, height=400)
canvas.pack(fill="both", expand=True)
for i in range(400):
    color = f"#{(44 + i // 10):02x}{(62 + i // 15):02x}{(80 + i // 20):02x}"
    canvas.create_line(0, i, 450, i, fill=color)

# ส่วนหัวโปรแกรม
header_label = tk.Label(root, text="🚍 โปรแกรมคำนวณค่าโดยสาร 🚍", font=("Helvetica", 18, "bold"), fg="#F1C40F", bg="#2C3E50")
header_label.place(x=50, y=10, width=350)

# ส่วนของ Label และ Entry
label = tk.Label(root, text="ระบุระยะทาง (กม.):", font=("Helvetica", 16, "bold"), fg="#ECF0F1", bg="#2C3E50")
label.place(x=50, y=80)

entry_distance = tk.Entry(root, font=("Helvetica", 16, "bold"), fg="#34495E", bg="#ECF0F1", justify="center", highlightbackground="#F1C40F", highlightcolor="#F1C40F", highlightthickness=3)
entry_distance.place(x=50, y=120, width=350, height=40)

# ปุ่มคำนวณ
btn_calculate = tk.Button(root, text="🚌 คำนวณค่าโดยสาร 🚌", font=("Helvetica", 16, "bold"), fg="#ECF0F1", bg="#27AE60", activebackground="#1E8449", activeforeground="#ECF0F1", relief="raised", bd=7, command=on_calculate, cursor="hand2")
btn_calculate.place(x=100, y=200, width=250, height=60)

# ป้ายท้าย
footer_label = tk.Label(root, text="พัฒนาโดย: นาย ปฏิภาณ สมเกียรติสกุล", font=("Helvetica", 12, "italic"), fg="#F1C40F", bg="#2C3E50")
footer_label.place(x=110, y=340)

# รัน GUI
root.mainloop()
