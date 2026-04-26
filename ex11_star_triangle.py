def star_triangle(n):
    """
    คำอธิบาย:
    สร้างรูปสามเหลี่ยมมุมฉากด้วยดอกจัน (*) จำนวน n แถว 
    โดยแถวที่ 1 มี 1 อัน, แถวที่ 2 มี 2 อัน, ... จนถึงแถวที่ n
    คืนค่าเป็น string โดยใช้ \n เพื่อขึ้นบรรทัดใหม่
    
    พารามิเตอร์:
    n (int): จำนวนแถวที่ต้องการ
    
    ผลลัพธ์:
    str: ข้อความรูปสามเหลี่ยมดอกจัน
    
    ตัวอย่าง:
    star_triangle(3) -> "*\n**\n***"
    """
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    raise NotImplementedError("ลบไลน์นี้แล้วเขียนโค้ดของคุณที่นี่")
    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    # ทดสอบด้วยตัวเอง
    try:
        result = star_triangle(3)
        print(f"Test Case 1: star_triangle(3) = {result} (คาดหวัง: {repr(*
**
***)})")
    except NotImplementedError:
        print(f"Test Case 1: star_triangle(3) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 1: star_triangle(3) = 💥 เกิดข้อผิดพลาด: {e}")
    try:
        result = star_triangle(1)
        print(f"Test Case 2: star_triangle(1) = {result} (คาดหวัง: {repr(*)})")
    except NotImplementedError:
        print(f"Test Case 2: star_triangle(1) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 2: star_triangle(1) = 💥 เกิดข้อผิดพลาด: {e}")
