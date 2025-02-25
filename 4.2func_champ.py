def calculate_fare(distance):
    # ค่าโดยสารเริ่มต้น
    base_fare = 10
    
    # กำหนดระยะทางและค่าโดยสารเพิ่ม
    if distance <= 5:
        fare = base_fare
    elif 6 <= distance <= 10:
        fare = base_fare + 2
    elif 11 <= distance <= 15:
        fare = base_fare + 4  # 2 บาทสำหรับช่วง 6-10 กม. + 2 บาทสำหรับช่วง 11-15 กม.
    elif 16 <= distance <= 20:
        fare = base_fare + 6  # 2 บาทสำหรับช่วง 6-10 กม. + 2 บาทสำหรับช่วง 11-15 กม. + 2 บาทสำหรับช่วง 16-20 กม.
    elif 21 <= distance <= 25:
        fare = base_fare + 8
    elif 26 <= distance <= 30:
        fare = base_fare + 10
    elif 31 <= distance <= 36:
        fare = base_fare + 12
    else:
        fare = "ไม่รองรับระยะทางเกิน 36 กม."

    return fare

# ทดสอบการคำนวณค่าโดยสาร
distance = float(input("ระบุระยะทางที่โดยสาร (กิโลเมตร): "))
fare = calculate_fare(distance)

print(f"ค่าโดยสารสำหรับ {distance} กม. คือ {fare} บาท")
