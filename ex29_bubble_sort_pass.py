def bubble_sort_pass(numbers):
    """
    คำอธิบาย:
    ทำการสลับที่ข้อมูล (Swap) แบบ Bubble Sort เพียง 1 รอบ (Pass) 
    เพื่อนำค่าที่มากที่สุดไปไว้ท้ายลิสต์
    (ลิสต์จะถูกแก้ไขในตัว หรือจะคืนค่าลิสต์ใหม่ก็ได้ ในที่นี้ให้คืนค่าลิสต์ใหม่)
    
    พารามิเตอร์:
    numbers (list): ลิสต์ของตัวเลข
    
    ผลลัพธ์:
    list: ลิสต์หลังจากผ่านการ swap 1 รอบ
    
    ตัวอย่าง:
    bubble_sort_pass([4, 3, 1, 5, 2]) -> [3, 1, 4, 2, 5]
    # (4 > 3 -> swap -> [3, 4, 1, 5, 2])
    # (4 > 1 -> swap -> [3, 1, 4, 5, 2])
    # (4 < 5 -> no swap)
    # (5 > 2 -> swap -> [3, 1, 4, 2, 5])
    """
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    raise NotImplementedError("ลบไลน์นี้แล้วเขียนโค้ดของคุณที่นี่")
    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    # ทดสอบด้วยตัวเอง
    try:
        result = bubble_sort_pass([4, 3, 1, 5, 2])
        print(f"Test Case 1: bubble_sort_pass([4, 3, 1, 5, 2]) = {result} (คาดหวัง: {repr([3, 1, 4, 2, 5])})")
    except NotImplementedError:
        print(f"Test Case 1: bubble_sort_pass([4, 3, 1, 5, 2]) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 1: bubble_sort_pass([4, 3, 1, 5, 2]) = 💥 เกิดข้อผิดพลาด: {e}")
    try:
        result = bubble_sort_pass([1, 2, 3])
        print(f"Test Case 2: bubble_sort_pass([1, 2, 3]) = {result} (คาดหวัง: {repr([1, 2, 3])})")
    except NotImplementedError:
        print(f"Test Case 2: bubble_sort_pass([1, 2, 3]) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 2: bubble_sort_pass([1, 2, 3]) = 💥 เกิดข้อผิดพลาด: {e}")
