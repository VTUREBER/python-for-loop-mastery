import importlib
import sys

def run_tests():
    # รายการแบบฝึกหัด: (ชื่อไฟล์/โมดูล, ชื่อฟังก์ชัน, รายการเคสทดสอบ)
    # เคสทดสอบ: ((พารามิเตอร์,), ผลลัพธ์ที่คาดหวัง)
    all_tests = [
        (
            "ex01_sum_range", 
            "sum_range", 
            [
                ((5,), 15),
                ((10,), 55),
                ((1,), 1),
                ((0,), 0)
            ]
        ),
        (
            "ex02_step_sum", 
            "step_sum", 
            [
                ((1, 10, 2), 25),
                ((2, 10, 3), 15),
                ((5, 5, 1), 5),
                ((10, 5, 1), 0)
            ]
        ),
        (
            "ex03_countdown", 
            "countdown", 
            [
                ((5,), [5, 4, 3, 2, 1]),
                ((3,), [3, 2, 1]),
                ((1,), [1]),
                ((0,), [])
            ]
        ),
        (
            "ex04_count_even", 
            "count_even", 
            [
                (([1, 2, 3, 4, 5],), 2),
                (([2, 4, 6, 8],), 4),
                (([1, 3, 5],), 0),
                (([],), 0)
            ]
        ),
        (
            "ex05_find_max", 
            "find_max", 
            [
                (([1, 5, 3, 9, 2],), 9),
                (([-1, -5, -2],), -1),
                (([10],), 10),
                (([0, 0, 0],), 0)
            ]
        ),
        (
            "ex06_multiplication_table", 
            "multiplication_table", 
            [
                ((2,), [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]),
                ((5,), [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])
            ]
        ),
        (
            "ex07_reverse_string", 
            "reverse_string", 
            [
                (("hello",), "olleh"),
                (("Python",), "nohtyP"),
                (("",), ""),
                (("a",), "a")
            ]
        ),
        (
            "ex08_vowel_count", 
            "vowel_count", 
            [
                (("hello world",), 3),
                (("Python is fun",), 3),
                (("AEIOU",), 5),
                (("bcdfg",), 0)
            ]
        ),
        (
            "ex09_factorial", 
            "calculate_factorial", 
            [
                ((5,), 120),
                ((3,), 6),
                ((1,), 1),
                ((0,), 1)
            ]
        ),
        (
            "ex10_fibonacci_list", 
            "fibonacci_list", 
            [
                ((5,), [0, 1, 1, 2, 3]),
                ((1,), [0]),
                ((8,), [0, 1, 1, 2, 3, 5, 8, 13])
            ]
        ),
        (
            "ex11_star_triangle", 
            "star_triangle", 
            [
                ((3,), "*\n**\n***"),
                ((1,), "*"),
                ((5,), "*\n**\n***\n****\n*****")
            ]
        ),
        (
            "ex12_inverted_triangle", 
            "inverted_triangle", 
            [
                ((3,), "***\n**\n*"),
                ((1,), "*"),
                ((5,), "*****\n****\n***\n**\n*")
            ]
        ),
        (
            "ex13_pyramid", 
            "pyramid", 
            [
                ((3,), "  *\n ***\n*****"),
                ((1,), "*"),
                ((4,), "   *\n  ***\n *****\n*******")
            ]
        ),
        (
            "ex14_prime_check", 
            "is_prime", 
            [
                ((7,), True),
                ((4,), False),
                ((1,), False),
                ((2,), True),
                ((13,), True),
                ((15,), False)
            ]
        ),
        (
            "ex15_fizz_buzz", 
            "fizz_buzz", 
            [
                ((5,), [1, 2, "Fizz", 4, "Buzz"]),
                ((3,), [1, 2, "Fizz"]),
                ((15,), [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"])
            ]
        ),
        (
            "ex16_sum_multiples", 
            "sum_multiples", 
            [
                ((10,), 33),
                ((15,), 60),
                ((5,), 8),
                ((2,), 0)
            ]
        ),
        (
            "ex17_filter_even_positive", 
            "filter_even_positive", 
            [
                (([1, -2, 2, 0, 4, 5],), [2, 4]),
                (([-4, -2, 0, 1, 3],), []),
                (([2, 4, 6],), [2, 4, 6]),
                (([],), [])
            ]
        ),
        (
            "ex18_count_char_in_list", 
            "count_char_in_list", 
            [
                ((["apple", "banana", "cherry"], "a"), 4),
                ((["hello", "world"], "o"), 2),
                ((["A", "a", "B"], "A"), 1),
                (([], "z"), 0)
            ]
        ),
        (
            "ex19_all_above_threshold", 
            "all_above_threshold", 
            [
                (([10, 20, 30], 5), True),
                (([10, 4, 30], 5), False),
                (([5, 6, 7], 5), False),
                (([], 100), True)
            ]
        ),
    ]

    total_passed = 0
    total_exercises = len(all_tests)

    print("\n" + "="*40)
    print("🎯 Python For Loop Mastery - Test Runner")
    print("="*40 + "\n")

    for module_name, function_name, tests in all_tests:
        print(f"📌 กำลังตรวจ: {module_name}.py ...", end=" ")
        try:
            # โหลดโมดูลแบบไดนามิก
            module = importlib.import_module(module_name)
            func = getattr(module, function_name)
            
            passed_cases = 0
            for args, expected in tests:
                try:
                    result = func(*args)
                    if result == expected:
                        passed_cases += 1
                    else:
                        print(f"\n   ❌ เคส {args} ล้มเหลว: คาดหวัง {expected} แต่ได้ {result}")
                except Exception as e:
                    print(f"\n   ⚠️ เกิดข้อผิดพลาดขณะรันเคส {args}: {e}")

            if passed_cases == len(tests):
                print("✅ ผ่าน!")
                total_passed += 1
            else:
                print(f"❌ ไม่ผ่าน ({passed_cases}/{len(tests)})")

        except ImportError:
            print("🚫 ไม่พบไฟล์ (ยังไม่ได้เริ่มทำ)")
        except AttributeError:
            print(f"🚫 ไม่พบฟังก์ชัน '{function_name}'")
        except NotImplementedError:
            print("🚧 ยังไม่ได้เริ่มเขียนโค้ด (NotImplementedError)")
        except Exception as e:
            print(f"💥 เกิดข้อผิดพลาดร้ายแรง: {e}")

    print("\n" + "="*40)
    score = (total_passed / total_exercises) * 100
    print(f"📊 สรุปผล: ผ่าน {total_passed}/{total_exercises} ข้อ ({score:.1f}%)")
    print("="*40 + "\n")

if __name__ == "__main__":
    run_tests()
