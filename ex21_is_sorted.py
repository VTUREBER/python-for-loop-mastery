def is_sorted(numbers):
    """
    คำอธิบาย:
    ตรวจสอบว่าตัวเลขในลิสต์ numbers เรียงลำดับจากน้อยไปมากหรือไม่ (Ascending Order)
    
    พารามิเตอร์:
    numbers (list): ลิสต์ของตัวเลข
    
    ผลลัพธ์:
    bool: True ถ้าเรียงลำดับจากน้อยไปมาก, False ถ้าไม่ใช่
    
    ตัวอย่าง:
    is_sorted([1, 2, 3, 5]) -> True
    is_sorted([1, 3, 2, 5]) -> False
    is_sorted([5, 4, 3, 2]) -> False
    """
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    raise NotImplementedError("ลบไลน์นี้แล้วเขียนโค้ดของคุณที่นี่")
    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    # ทดสอบด้วยตัวเอง
    try:
        result = is_sorted([1, 2, 3, 5])
        print(f"Test Case 1: is_sorted([1, 2, 3, 5]) = {result} (คาดหวัง: {repr(True)})")
    except NotImplementedError:
        print(f"Test Case 1: is_sorted([1, 2, 3, 5]) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 1: is_sorted([1, 2, 3, 5]) = 💥 เกิดข้อผิดพลาด: {e}")
    try:
        result = is_sorted([1, 3, 2, 5])
        print(f"Test Case 2: is_sorted([1, 3, 2, 5]) = {result} (คาดหวัง: {repr(False)})")
    except NotImplementedError:
        print(f"Test Case 2: is_sorted([1, 3, 2, 5]) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 2: is_sorted([1, 3, 2, 5]) = 💥 เกิดข้อผิดพลาด: {e}")
