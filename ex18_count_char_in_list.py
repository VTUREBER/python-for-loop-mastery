def count_char_in_list(strings, char):
    """
    คำอธิบาย:
    นับว่ามีตัวอักษร char ปรากฏอยู่ในลิสต์ของข้อความ strings ทั้งหมดกี่ครั้ง (case-sensitive)
    
    พารามิเตอร์:
    strings (list): ลิสต์ของข้อความ
    char (str): ตัวอักษรที่ต้องการนับ
    
    ผลลัพธ์:
    int: จำนวนครั้งที่พบ
    
    ตัวอย่าง:
    count_char_in_list(["apple", "banana", "cherry"], "a") -> 4
    count_char_in_list(["hello", "world"], "o") -> 2
    count_char_in_list(["A", "a", "B"], "A") -> 1
    """
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    raise NotImplementedError("ลบไลน์นี้แล้วเขียนโค้ดของคุณที่นี่")
    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    # ทดสอบด้วยตัวเอง
    try:
        result = count_char_in_list(['apple', 'banana', 'cherry'], 'a')
        print(f"Test Case 1: count_char_in_list(['apple', 'banana', 'cherry'], 'a') = {result} (คาดหวัง: {repr(4)})")
    except NotImplementedError:
        print(f"Test Case 1: count_char_in_list(['apple', 'banana', 'cherry'], 'a') = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 1: count_char_in_list(['apple', 'banana', 'cherry'], 'a') = 💥 เกิดข้อผิดพลาด: {e}")
    try:
        result = count_char_in_list(['hello', 'world'], 'o')
        print(f"Test Case 2: count_char_in_list(['hello', 'world'], 'o') = {result} (คาดหวัง: {repr(2)})")
    except NotImplementedError:
        print(f"Test Case 2: count_char_in_list(['hello', 'world'], 'o') = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 2: count_char_in_list(['hello', 'world'], 'o') = 💥 เกิดข้อผิดพลาด: {e}")
