def sum_range(n):
    """
    คำอธิบาย:
    หาผลรวมของตัวเลขตั้งแต่ 1 ถึง n โดยใช้ for loop
    
    พารามิเตอร์:
    n (int): จำนวนเต็มที่เป็นจุดสิ้นสุด (รวม n ด้วย)
    
    ผลลัพธ์:
    int: ผลรวมของตัวเลข
    
    ตัวอย่าง:
    sum_range(5) -> 1 + 2 + 3 + 4 + 5 = 15
    sum_range(10) -> 55
    """
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    raise NotImplementedError("ลบไลน์นี้แล้วเขียนโค้ดของคุณที่นี่")
    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    # ทดสอบด้วยตัวเอง
    try:
        result = sum_range(5)
        print(f"Test Case 1: sum_range(5) = {result} (คาดหวัง: {repr(15)})")
    except NotImplementedError:
        print(f"Test Case 1: sum_range(5) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 1: sum_range(5) = 💥 เกิดข้อผิดพลาด: {e}")
    try:
        result = sum_range(10)
        print(f"Test Case 2: sum_range(10) = {result} (คาดหวัง: {repr(55)})")
    except NotImplementedError:
        print(f"Test Case 2: sum_range(10) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 2: sum_range(10) = 💥 เกิดข้อผิดพลาด: {e}")
