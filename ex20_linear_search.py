def linear_search(numbers, target):
    """
    คำอธิบาย:
    ค้นหาตำแหน่ง (index) ของ target ในลิสต์ numbers 
    ถ้าพบให้คืนค่า index ที่พบ (ถ้ามีหลายที่ให้เอาที่แรก) 
    ถ้าไม่พบให้คืนค่า -1
    
    พารามิเตอร์:
    numbers (list): ลิสต์ของตัวเลข
    target (int): ตัวเลขที่ต้องการค้นหา
    
    ผลลัพธ์:
    int: index ที่พบ หรือ -1
    
    ตัวอย่าง:
    linear_search([10, 20, 30, 40], 30) -> 2
    linear_search([10, 20, 30, 40], 50) -> -1
    """
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    raise NotImplementedError("ลบไลน์นี้แล้วเขียนโค้ดของคุณที่นี่")
    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    # ทดสอบด้วยตัวเอง
    try:
        result = linear_search([10, 20, 30, 40], 30)
        print(f"Test Case 1: linear_search([10, 20, 30, 40], 30) = {result} (คาดหวัง: {repr(2)})")
    except NotImplementedError:
        print(f"Test Case 1: linear_search([10, 20, 30, 40], 30) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 1: linear_search([10, 20, 30, 40], 30) = 💥 เกิดข้อผิดพลาด: {e}")
    try:
        result = linear_search([10, 20, 30, 40], 50)
        print(f"Test Case 2: linear_search([10, 20, 30, 40], 50) = {result} (คาดหวัง: {repr(-1)})")
    except NotImplementedError:
        print(f"Test Case 2: linear_search([10, 20, 30, 40], 50) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 2: linear_search([10, 20, 30, 40], 50) = 💥 เกิดข้อผิดพลาด: {e}")
