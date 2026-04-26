def find_min(numbers):
    """
    คำอธิบาย:
    หาค่าที่น้อยที่สุดในลิสต์ numbers โดยใช้ for loop ห้ามใช้ฟังก์ชัน min()
    
    พารามิเตอร์:
    numbers (list): ลิสต์ของจำนวนเต็ม (มีสมาชิกอย่างน้อย 1 ตัว)
    
    ผลลัพธ์:
    int: ค่าที่น้อยที่สุดในลิสต์
    
    ตัวอย่าง:
    find_min([1, 5, 3, 9, 2]) -> 1
    find_min([-1, -5, -2]) -> -5
    """
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    raise NotImplementedError("ลบไลน์นี้แล้วเขียนโค้ดของคุณที่นี่")
    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    # ทดสอบด้วยตัวเอง
    try:
        result = find_min([1, 5, 3, 9, 2])
        print(f"Test Case 1: find_min([1, 5, 3, 9, 2]) = {result} (คาดหวัง: {repr(1)})")
    except NotImplementedError:
        print(f"Test Case 1: find_min([1, 5, 3, 9, 2]) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 1: find_min([1, 5, 3, 9, 2]) = 💥 เกิดข้อผิดพลาด: {e}")
    try:
        result = find_min([-1, -5, -2])
        print(f"Test Case 2: find_min([-1, -5, -2]) = {result} (คาดหวัง: {repr(-5)})")
    except NotImplementedError:
        print(f"Test Case 2: find_min([-1, -5, -2]) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 2: find_min([-1, -5, -2]) = 💥 เกิดข้อผิดพลาด: {e}")
