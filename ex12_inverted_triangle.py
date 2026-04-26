def inverted_triangle(n):
    """
    คำอธิบาย:
    สร้างรูปสามเหลี่ยมกลับหัวด้วยดอกจัน (*) จำนวน n แถว 
    โดยแถวที่ 1 มี n อัน, แถวที่ 2 มี n-1 อัน, ... จนถึงแถวสุดท้ายมี 1 อัน
    คืนค่าเป็น string โดยใช้ \n เพื่อขึ้นบรรทัดใหม่
    
    พารามิเตอร์:
    n (int): จำนวนแถวเริ่มต้น
    
    ผลลัพธ์:
    str: ข้อความรูปสามเหลี่ยมกลับหัว
    
    ตัวอย่าง:
    inverted_triangle(3) -> "***\n**\n*"
    """
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    raise NotImplementedError("ลบไลน์นี้แล้วเขียนโค้ดของคุณที่นี่")
    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    # ทดสอบด้วยตัวเอง
    try:
        result = inverted_triangle(3)
        print(f"Test Case 1: inverted_triangle(3) = {result} (คาดหวัง: {repr(***
**
*)})")
    except NotImplementedError:
        print(f"Test Case 1: inverted_triangle(3) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 1: inverted_triangle(3) = 💥 เกิดข้อผิดพลาด: {e}")
    try:
        result = inverted_triangle(1)
        print(f"Test Case 2: inverted_triangle(1) = {result} (คาดหวัง: {repr(*)})")
    except NotImplementedError:
        print(f"Test Case 2: inverted_triangle(1) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 2: inverted_triangle(1) = 💥 เกิดข้อผิดพลาด: {e}")
