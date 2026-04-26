def sum_2d_list(matrix):
    """
    คำอธิบาย:
    หาผลรวมของตัวเลขทั้งหมดใน Matrix (ลิสต์ซ้อนลิสต์) โดยใช้ Nested Loop
    
    พารามิเตอร์:
    matrix (list of list): ลิสต์ 2 มิติที่เก็บตัวเลข
    
    ผลลัพธ์:
    int: ผลรวมทั้งหมด
    
    ตัวอย่าง:
    sum_2d_list([[1, 2], [3, 4]]) -> 10
    sum_2d_list([[1, 1, 1], [2, 2, 2]]) -> 9
    """
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    raise NotImplementedError("ลบไลน์นี้แล้วเขียนโค้ดของคุณที่นี่")
    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    # ทดสอบด้วยตัวเอง
    try:
        result = sum_2d_list([[1, 2], [3, 4]])
        print(f"Test Case 1: sum_2d_list([[1, 2], [3, 4]]) = {result} (คาดหวัง: {repr(10)})")
    except NotImplementedError:
        print(f"Test Case 1: sum_2d_list([[1, 2], [3, 4]]) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 1: sum_2d_list([[1, 2], [3, 4]]) = 💥 เกิดข้อผิดพลาด: {e}")
    try:
        result = sum_2d_list([[1, 1, 1], [2, 2, 2]])
        print(f"Test Case 2: sum_2d_list([[1, 1, 1], [2, 2, 2]]) = {result} (คาดหวัง: {repr(9)})")
    except NotImplementedError:
        print(f"Test Case 2: sum_2d_list([[1, 1, 1], [2, 2, 2]]) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 2: sum_2d_list([[1, 1, 1], [2, 2, 2]]) = 💥 เกิดข้อผิดพลาด: {e}")
