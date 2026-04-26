def sum_multiples(n):
    """
    คำอธิบาย:
    หาผลรวมของตัวเลขตั้งแต่ 1 ถึง n ที่หารด้วย 3 หรือ 5 ลงตัว
    
    พารามิเตอร์:
    n (int): จำนวนเต็มบวก
    
    ผลลัพธ์:
    int: ผลรวมของตัวเลข
    
    ตัวอย่าง:
    sum_multiples(10) -> 33 (3+5+6+9+10)
    sum_multiples(15) -> 60 (3+5+6+9+10+12+15)
    """
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    raise NotImplementedError("ลบไลน์นี้แล้วเขียนโค้ดของคุณที่นี่")
    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    # ทดสอบด้วยตัวเอง
    try:
        result = sum_multiples(10)
        print(f"Test Case 1: sum_multiples(10) = {result} (คาดหวัง: {repr(33)})")
    except NotImplementedError:
        print(f"Test Case 1: sum_multiples(10) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 1: sum_multiples(10) = 💥 เกิดข้อผิดพลาด: {e}")
    try:
        result = sum_multiples(15)
        print(f"Test Case 2: sum_multiples(15) = {result} (คาดหวัง: {repr(60)})")
    except NotImplementedError:
        print(f"Test Case 2: sum_multiples(15) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 2: sum_multiples(15) = 💥 เกิดข้อผิดพลาด: {e}")
