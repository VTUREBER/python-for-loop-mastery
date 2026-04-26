def identity_matrix(n):
    """
    คำอธิบาย:
    สร้าง Matrix ขนาด n x n ที่มีเลข 1 อยู่ในแนวทแยงมุม (i == j) 
    นอกนั้นเป็นเลข 0 (Identity Matrix)
    
    พารามิเตอร์:
    n (int): ขนาดของ Matrix
    
    ผลลัพธ์:
    list of list: Matrix ขนาด n x n
    
    ตัวอย่าง:
    identity_matrix(2) -> [[1, 0], [0, 1]]
    identity_matrix(3) -> [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    """
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    raise NotImplementedError("ลบไลน์นี้แล้วเขียนโค้ดของคุณที่นี่")
    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    # ทดสอบด้วยตัวเอง
    try:
        result = identity_matrix(2)
        print(f"Test Case 1: identity_matrix(2) = {result} (คาดหวัง: {repr([[1, 0], [0, 1]])})")
    except NotImplementedError:
        print(f"Test Case 1: identity_matrix(2) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 1: identity_matrix(2) = 💥 เกิดข้อผิดพลาด: {e}")
    try:
        result = identity_matrix(3)
        print(f"Test Case 2: identity_matrix(3) = {result} (คาดหวัง: {repr([[1, 0, 0], [0, 1, 0], [0, 0, 1]])})")
    except NotImplementedError:
        print(f"Test Case 2: identity_matrix(3) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 2: identity_matrix(3) = 💥 เกิดข้อผิดพลาด: {e}")
