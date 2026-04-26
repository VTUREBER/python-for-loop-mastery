def pyramid(n):
    """
    คำอธิบาย:
    สร้างรูปพีระมิดด้วยดอกจัน (*) จำนวน n แถว 
    แถวที่ 1 มี 1 อัน (เว้นวรรคข้างหน้า n-1 ช่อง)
    แถวที่ 2 มี 3 อัน (เว้นวรรคข้างหน้า n-2 ช่อง)
    แถวที่ i มี 2i-1 อัน (เว้นวรรคข้างหน้า n-i ช่อง)
    คืนค่าเป็น string โดยใช้ \n เพื่อขึ้นบรรทัดใหม่
    
    พารามิเตอร์:
    n (int): ความสูงของพีระมิด
    
    ผลลัพธ์:
    str: ข้อความรูปพีระมิด
    
    ตัวอย่าง:
    pyramid(3) -> "  *\n ***\n*****"
    """
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    raise NotImplementedError("ลบไลน์นี้แล้วเขียนโค้ดของคุณที่นี่")
    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    # ทดสอบด้วยตัวเอง
    try:
        result = pyramid(3)
        print(f"Test Case 1: pyramid(3) = {result} (คาดหวัง: {repr(  *
 ***
*****)})")
    except NotImplementedError:
        print(f"Test Case 1: pyramid(3) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 1: pyramid(3) = 💥 เกิดข้อผิดพลาด: {e}")
    try:
        result = pyramid(1)
        print(f"Test Case 2: pyramid(1) = {result} (คาดหวัง: {repr(*)})")
    except NotImplementedError:
        print(f"Test Case 2: pyramid(1) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 2: pyramid(1) = 💥 เกิดข้อผิดพลาด: {e}")
