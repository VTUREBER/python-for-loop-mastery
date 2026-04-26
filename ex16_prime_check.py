def is_prime(n):
    """
    คำอธิบาย:
    ตรวจสอบว่าจำนวนเต็มบวก n เป็นจำนวนเฉพาะ (Prime Number) หรือไม่
    จำนวนเฉพาะคือจำนวนที่มากกว่า 1 และมีเพียง 1 และตัวมันเองเท่านั้นที่หารลงตัว
    
    พารามิเตอร์:
    n (int): จำนวนที่ต้องการตรวจสอบ
    
    ผลลัพธ์:
    bool: True ถ้าเป็นจำนวนเฉพาะ, False ถ้าไม่เป็น
    
    ตัวอย่าง:
    is_prime(7) -> True
    is_prime(4) -> False
    """
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    raise NotImplementedError("ลบไลน์นี้แล้วเขียนโค้ดของคุณที่นี่")
    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    # ทดสอบด้วยตัวเอง
    try:
        result = is_prime(7)
        print(f"Test Case 1: is_prime(7) = {result} (คาดหวัง: {repr(True)})")
    except NotImplementedError:
        print(f"Test Case 1: is_prime(7) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 1: is_prime(7) = 💥 เกิดข้อผิดพลาด: {e}")
    try:
        result = is_prime(4)
        print(f"Test Case 2: is_prime(4) = {result} (คาดหวัง: {repr(False)})")
    except NotImplementedError:
        print(f"Test Case 2: is_prime(4) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 2: is_prime(4) = 💥 เกิดข้อผิดพลาด: {e}")
