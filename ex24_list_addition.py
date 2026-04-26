def list_addition(list_a, list_b):
    """
    คำอธิบาย:
    มีลิสต์ A และ B ที่มีความยาวเท่ากัน ให้สร้างลิสต์ใหม่ C 
    ที่เกิดจากผลบวกของสมาชิกในตำแหน่งเดียวกัน (C[i] = A[i] + B[i])
    
    พารามิเตอร์:
    list_a (list): ลิสต์ของตัวเลข
    list_b (list): ลิสต์ของตัวเลข (ยาวเท่ากับ list_a)
    
    ผลลัพธ์:
    list: ลิสต์ผลรวม
    
    ตัวอย่าง:
    list_addition([1, 2, 3], [10, 20, 30]) -> [11, 22, 33]
    """
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    raise NotImplementedError("ลบไลน์นี้แล้วเขียนโค้ดของคุณที่นี่")
    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    # ทดสอบด้วยตัวเอง
    try:
        result = list_addition([1, 2, 3], [10, 20, 30])
        print(f"Test Case 1: list_addition([1, 2, 3], [10, 20, 30]) = {result} (คาดหวัง: {repr([11, 22, 33])})")
    except NotImplementedError:
        print(f"Test Case 1: list_addition([1, 2, 3], [10, 20, 30]) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 1: list_addition([1, 2, 3], [10, 20, 30]) = 💥 เกิดข้อผิดพลาด: {e}")
    try:
        result = list_addition([0, 0], [1, 1])
        print(f"Test Case 2: list_addition([0, 0], [1, 1]) = {result} (คาดหวัง: {repr([1, 1])})")
    except NotImplementedError:
        print(f"Test Case 2: list_addition([0, 0], [1, 1]) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 2: list_addition([0, 0], [1, 1]) = 💥 เกิดข้อผิดพลาด: {e}")
