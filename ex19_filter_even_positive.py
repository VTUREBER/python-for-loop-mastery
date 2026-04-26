def filter_even_positive(numbers):
    """
    คำอธิบาย:
    คัดเลือกเฉพาะตัวเลขที่เป็น "เลขคู่" และ "มากกว่า 0" จากลิสต์ที่กำหนดให้
    
    พารามิเตอร์:
    numbers (list): ลิสต์ของจำนวนเต็ม
    
    ผลลัพธ์:
    list: ลิสต์ของตัวเลขที่ผ่านเงื่อนไข
    
    ตัวอย่าง:
    filter_even_positive([1, -2, 2, 0, 4, 5]) -> [2, 4]
    filter_even_positive([-4, -2, 0, 1, 3]) -> []
    """
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    raise NotImplementedError("ลบไลน์นี้แล้วเขียนโค้ดของคุณที่นี่")
    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    # ทดสอบด้วยตัวเอง
    try:
        result = filter_even_positive([1, -2, 2, 0, 4, 5])
        print(f"Test Case 1: filter_even_positive([1, -2, 2, 0, 4, 5]) = {result} (คาดหวัง: {repr([2, 4])})")
    except NotImplementedError:
        print(f"Test Case 1: filter_even_positive([1, -2, 2, 0, 4, 5]) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 1: filter_even_positive([1, -2, 2, 0, 4, 5]) = 💥 เกิดข้อผิดพลาด: {e}")
    try:
        result = filter_even_positive([-4, -2, 0, 1, 3])
        print(f"Test Case 2: filter_even_positive([-4, -2, 0, 1, 3]) = {result} (คาดหวัง: {repr([])})")
    except NotImplementedError:
        print(f"Test Case 2: filter_even_positive([-4, -2, 0, 1, 3]) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 2: filter_even_positive([-4, -2, 0, 1, 3]) = 💥 เกิดข้อผิดพลาด: {e}")
