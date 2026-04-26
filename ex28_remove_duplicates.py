def remove_duplicates(numbers):
    """
    คำอธิบาย:
    สร้างลิสต์ใหม่ที่มีสมาชิกไม่ซ้ำกันจากลิสต์เดิม 
    โดยห้ามใช้ set() และให้คงลำดับเดิมไว้
    
    พารามิเตอร์:
    numbers (list): ลิสต์ของตัวเลข
    
    ผลลัพธ์:
    list: ลิสต์ใหม่ที่ไม่มีตัวซ้ำ
    
    ตัวอย่าง:
    remove_duplicates([1, 2, 2, 3, 1, 4]) -> [1, 2, 3, 4]
    remove_duplicates([5, 5, 5]) -> [5]
    """
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    raise NotImplementedError("ลบไลน์นี้แล้วเขียนโค้ดของคุณที่นี่")
    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    # ทดสอบด้วยตัวเอง
    try:
        result = remove_duplicates([1, 2, 2, 3, 1, 4])
        print(f"Test Case 1: remove_duplicates([1, 2, 2, 3, 1, 4]) = {result} (คาดหวัง: {repr([1, 2, 3, 4])})")
    except NotImplementedError:
        print(f"Test Case 1: remove_duplicates([1, 2, 2, 3, 1, 4]) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 1: remove_duplicates([1, 2, 2, 3, 1, 4]) = 💥 เกิดข้อผิดพลาด: {e}")
    try:
        result = remove_duplicates([5, 5, 5])
        print(f"Test Case 2: remove_duplicates([5, 5, 5]) = {result} (คาดหวัง: {repr([5])})")
    except NotImplementedError:
        print(f"Test Case 2: remove_duplicates([5, 5, 5]) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 2: remove_duplicates([5, 5, 5]) = 💥 เกิดข้อผิดพลาด: {e}")
