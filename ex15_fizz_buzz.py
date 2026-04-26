def fizz_buzz(n):
    """
    คำอธิบาย:
    สร้างลิสต์ของผลลัพธ์ FizzBuzz ตั้งแต่ 1 ถึง n
    - ถ้าหาร 3 ลงตัว ให้ใส่ "Fizz"
    - ถ้าหาร 5 ลงตัว ให้ใส่ "Buzz"
    - ถ้าหารทั้ง 3 และ 5 ลงตัว ให้ใส่ "FizzBuzz"
    - ถ้าไม่เข้าเงื่อนไขใดเลย ให้ใส่ตัวเลขนั้นๆ
    
    พารามิเตอร์:
    n (int): จำนวนเต็มบวก
    
    ผลลัพธ์:
    list: ลิสต์ของผลลัพธ์
    
    ตัวอย่าง:
    fizz_buzz(5) -> [1, 2, "Fizz", 4, "Buzz"]
    fizz_buzz(15) -> [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]
    """
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    raise NotImplementedError("ลบไลน์นี้แล้วเขียนโค้ดของคุณที่นี่")
    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    # ทดสอบด้วยตัวเอง
    try:
        result = fizz_buzz(5)
        print(f"Test Case 1: fizz_buzz(5) = {result} (คาดหวัง: {repr([1, 2, 'Fizz', 4, 'Buzz'])})")
    except NotImplementedError:
        print(f"Test Case 1: fizz_buzz(5) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 1: fizz_buzz(5) = 💥 เกิดข้อผิดพลาด: {e}")
    try:
        result = fizz_buzz(3)
        print(f"Test Case 2: fizz_buzz(3) = {result} (คาดหวัง: {repr([1, 2, 'Fizz'])})")
    except NotImplementedError:
        print(f"Test Case 2: fizz_buzz(3) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 2: fizz_buzz(3) = 💥 เกิดข้อผิดพลาด: {e}")
