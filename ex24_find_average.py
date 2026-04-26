def find_average(numbers):
    """
    คำอธิบาย:
    หาค่าเฉลี่ยของตัวเลขในลิสต์ numbers 
    โดยห้ามใช้ฟังก์ชัน sum() หรือ len()
    (ถ้าลิสต์ว่างให้คืนค่า 0)
    
    พารามิเตอร์:
    numbers (list): ลิสต์ของตัวเลข
    
    ผลลัพธ์:
    float: ค่าเฉลี่ย
    
    ตัวอย่าง:
    find_average([1, 2, 3, 4, 5]) -> 3.0
    find_average([10, 20]) -> 15.0
    """
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    raise NotImplementedError("ลบไลน์นี้แล้วเขียนโค้ดของคุณที่นี่")
    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    # ทดสอบด้วยตัวเอง
    try:
        result = find_average([1, 2, 3, 4, 5])
        print(f"Test Case 1: find_average([1, 2, 3, 4, 5]) = {result} (คาดหวัง: {repr(3.0)})")
    except NotImplementedError:
        print(f"Test Case 1: find_average([1, 2, 3, 4, 5]) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 1: find_average([1, 2, 3, 4, 5]) = 💥 เกิดข้อผิดพลาด: {e}")
    try:
        result = find_average([10, 20])
        print(f"Test Case 2: find_average([10, 20]) = {result} (คาดหวัง: {repr(15.0)})")
    except NotImplementedError:
        print(f"Test Case 2: find_average([10, 20]) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 2: find_average([10, 20]) = 💥 เกิดข้อผิดพลาด: {e}")
