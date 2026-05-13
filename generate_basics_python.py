from pathlib import Path
import textwrap


JAVA_ROOT = Path(r"c:\Users\Lenovo\OneDrive\Desktop\numpy\Java-Fundamentals\Basics")
PYTHON_ROOT = Path(r"c:\Users\Lenovo\OneDrive\Desktop\numpy\Python\Cooding_Ques\Basics")


BODIES = {
    "CheckSumOfFactorIs_Equal_To_Number.java": """
        n = int(input())
        sum_of_factors = 1
        temp = n

        for i in range(2, n):
            if temp % i == 0:
                sum_of_factors += i

        if sum_of_factors == n:
            print("Perfect Number")
        else:
            print("Not Perfect Number")
    """,
    "Check_Armstrong.java": """
        n = int(input())
        temp = n
        rem = 0
        res = 0
        count = 0

        while temp != 0:
            count += 1
            temp //= 10

        temp = n
        while temp != 0:
            rem = temp % 10
            res1 = 1
            for _ in range(count):
                res1 *= rem
            res += res1
            temp //= 10

        if n == res:
            print("Armstrong")
        else:
            print("Not Armstrong")
    """,
    "Fabonacci_Series_AND_SUM.java": """
        n = int(input())
        a = 0
        b = 1

        for _ in range(1, n + 1):
            print(a, end=" ")
            c = a + b
            a = b
            b = c

        print()
    """,
    "Factorial.java": """
        n = int(input())
        res = 1

        for i in range(1, n + 1):
            res *= i

        print(res)
    """,
    "GCD_HCF.java": """
        a = int(input())
        b = int(input())

        while b != 0:
            temp = b
            b = a % b
            a = temp

        print(a)
    """,
    "Happy_Number.java": """
        n = int(input())
        temp = n

        while True:
            res = 0

            while temp != 0:
                rem = temp % 10
                res += rem ** 2
                temp //= 10

            if res == 1:
                print("Success")
                break
            if res == 4:
                print("Failed")
                break

            temp = res
    """,
    "Prime_Number.java": """
        n = int(input())
        is_prime = n >= 2

        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break

        if is_prime:
            print("Prime Number")
        else:
            print("Not Prime Number")
    """,
    "Q1.java": """
        print("Enter Your Number :")
        n = int(input())
        print("Your Entered Number is " + str(n))
    """,
    "Q2UserInput.java": """
        a = int(input())
        print(a)
    """,
    "Q3_Multiply.java": """
        a = float(input())
        b = float(input())
        print("The Answer is :" + str(a * b))
    """,
    "Q4_Swap_Numbers.java": """
        a = int(input())
        b = int(input())
        c = a
        a = b
        b = c
        print("Numbers are Swaped :" + str(a) + " and " + str(b))
    """,
    "Q5_Add_Binary_Strings.java": """
        print("Enter first binary string: ", end="")
        bin1 = input().strip()

        print("Enter second binary string: ", end="")
        bin2 = input().strip()

        num1 = int(bin1, 2)
        num2 = int(bin2, 2)
        total = num1 + num2
        result = format(total, "b")

        print("Sum of binary strings: " + result)
    """,
    "Q7_Even_Odd.java": """
        a = int(input())

        if a % 2 == 0:
            print("Even")
        else:
            print("Odd")
    """,
    "Q8_Largest.java": """
        a = int(input())
        b = int(input())
        c = int(input())

        if a > b and a > c:
            print(str(a) + " is greater")
        elif b > c:
            print(str(b) + " is greater")
        else:
            print(str(c) + " is greater")
    """,
    "Q9_LCM.java": """
        def least(a, b):
            return a if a < b else b


        a = int(input())
        b = int(input())

        x = a
        y = b
        lcm = 1
        i = 2
        least_value = least(a, b)

        while i <= least_value:
            if x % i == 0 and y % i == 0:
                lcm *= i
                x //= i
                y //= i
            else:
                i += 1

        lcm = lcm * x * y
        print(lcm)
    """,
    "Q10_GCD.java": """
        a = int(input())
        b = int(input())

        while b != 0:
            rem = a % b
            a = b
            b = rem

        print("GCD = " + str(a))
    """,
    "Q11_Prime_1_to_N.java": """
        n = int(input())

        for i in range(2, n + 1):
            count = 0
            for j in range(2, i):
                if i % j == 0:
                    count += 1
                    break
            if count == 0:
                print(i, end="  ")

        print()
    """,
    "Q12_Leap_Year.java": """
        n = int(input())

        if (n % 100 != 0 and n % 4 == 0) or n % 400 == 0:
            print("Year is Leap Year")
        else:
            print("Not a Leap Year")
    """,
    "Q13_Check_Palindome.java": """
        n = int(input())
        b = n
        rev = 0

        while n != 0:
            a = n % 10
            rev = rev * 10 + a
            n //= 10

        if b == rev:
            print("it's palindrome")
        else:
            print("it's Not")
    """,
    "Q14_Armstrong.java": """
        print("Enter your first limit")
        limit1 = int(input())

        print("Enter your Second limit")
        limit2 = int(input())

        print("Armstrong number Between " + str(limit1) + " and " + str(limit2))

        for num in range(limit1, limit2 + 1):
            temp = num
            count_digit = 0

            while temp != 0:
                count_digit += 1
                temp //= 10

            temp = num
            arm = 0

            while temp != 0:
                rem = temp % 10
                arm += rem ** count_digit
                temp //= 10

            if arm == num:
                print(arm)
    """,
    "Q15_Neon_Number.java": """
        a = int(input())
        b = a * a
        res = 0

        while b != 0:
            res += b % 10
            b //= 10

        if res == a:
            print("Number is Neon Number")
        else:
            print("its Not")
    """,
    "Q16_Check_vowel.java": """
        print("Enter a single alphabet character: ", end="")
        ch = input().strip().lower()[0]

        if ch in ("a", "e", "i", "o", "u"):
            print("It's a vowel.")
        else:
            print("It's a consonant.")
    """,
    "Q17_Sum_Natural_Num.java": """
        n = int(input())

        if n > 0:
            total = 0
            for i in range(1, n + 1):
                total += i
            print("Sum of All Natural Number b/w 1 to N is :" + str(total))
        else:
            print("Number is Invalid")
    """,
    "Q18_Factorial.java": """
        n = int(input())
        fact = 1

        if n == 0:
            print("Factorial is :1")
        else:
            for i in range(n, 0, -1):
                fact *= i
            print("Factorial is :" + str(fact))
    """,
    "Q19EvenSumFibonacci.java": """
        n = int(input())
        a = 0
        b = 1
        total = 0

        for _ in range(1, n + 1):
            if a % 2 == 0:
                total += a
            next_value = a + b
            a = b
            b = next_value

        print(total)
    """,
    "Q20_Simple_Interest.java": """
        principle = float(input())
        rate = float(input())
        time = float(input())

        simple_interest = (principle * rate * time) / 100
        print("Simple Interest is :" + str(simple_interest))
    """,
    "Q21_Compound_Interest.java": """
        principle = float(input())
        rate = float(input())
        n = float(input())
        time = float(input())

        amount = principle * (1 + (rate / 100) / n) ** (n * time)
        compound_interest = amount - principle

        print(compound_interest)
    """,
    "Q22_Perimeter.java": """
        length = int(input())
        width = int(input())
        print("Perimeter of rectangle is :" + str(2 * (length + width)))
    """,
    "Q23_Quot_Rem.java": """
        dividend = int(input())
        divisor = int(input())

        if divisor == 0:
            print("Division by zero not allowed")
        else:
            quotient = dividend // divisor
            remainder = dividend % divisor
            print("Quotient: " + str(quotient))
            print("Remainder: " + str(remainder))
    """,
    "Q24_Calc_Power.java": """
        base = int(input())
        power = int(input())
        result = 1

        for _ in range(1, power + 1):
            result *= base

        print(result)
    """,
    "Q25_P&C.java": """
        def factorial(n):
            fact = 1
            for i in range(2, n + 1):
                fact *= i
            return fact


        n = int(input())
        r = int(input())

        if r > n or n < 0 or r < 0:
            print("Invalid Input")
        else:
            permutation = factorial(n) // factorial(n - r)
            combination = factorial(n) // (factorial(r) * factorial(n - r))
            print("Permutation (nPr): " + str(permutation))
            print("Combination (nCr): " + str(combination))
    """,
    "Q27_Reverse_Number.java": """
        num = int(input())
        rev = 0

        while num != 0:
            rem = num % 10
            rev = rev * 10 + rem
            num //= 10

        print(rev)
    """,
    "Q28_Print_ASCII.java": """
        ch = input().strip()[0]
        ascii_value = ord(ch)
        print(ascii_value)
    """,
    "Q29_Check_Perfect_Square.java": """
        print("Enter Your Number")
        num = int(input())
        sqrt = int(num ** 0.5)

        if sqrt * sqrt == num:
            print("perfect Square " + str(sqrt))
        else:
            print("The Number Not have perfect square root")
    """,
    "Q30_Pos_Neg_Zero.java": """
        n = int(input())

        if n < 0:
            print("Input is negative")
        elif n == 0:
            print("Input is zero")
        else:
            print("Input is Positive")
    """,
    "Q31_Table.java": """
        n = int(input())
        print("Table of n is :")

        for i in range(1, 11):
            print(str(n) + " * " + str(i) + " = " + str(n * i))
    """,
    "Q32_CountDigits.java": """
        n = abs(int(input()))
        count = 0

        if n == 0:
            count = 1
        else:
            while n != 0:
                count += 1
                n //= 10

        print(count)
    """,
    "Q33_Print_Digits.java": """
        n = abs(int(input()))

        if n == 0:
            print(0)
        else:
            while n != 0:
                print(n % 10)
                n //= 10
    """,
    "Q34_Particular_Digit.java": """
        print("Enter Your Number :")
        n = int(input())
        temp = abs(n)
        count = 0

        print("Enter position ")
        position = int(input())

        if temp == 0:
            count = 1
        else:
            while temp != 0:
                count += 1
                temp //= 10

        if position <= 0 or position > count:
            print("Invalid Position / Out Of Range ")
        else:
            number = abs(n)
            for _ in range(1, position):
                number //= 10
            digit = number % 10
            print(digit)
    """,
    "Q35_Circumference.java": """
        import math


        radius = float(input())
        perimeter = 2 * math.pi * radius
        area = math.pi * radius * radius

        print("Perimeter is = " + str(perimeter))
        print("Area is = " + str(area))
    """,
    "Q36_Average.java": """
        a = float(input())
        b = float(input())
        c = float(input())
        avg = (a + b + c) / 3
        print("The Average of all numbers is :" + str(avg))
    """,
    "Q37_Digit_Sum.java": """
        n = abs(int(input()))
        total = 0

        while n != 0:
            total += n % 10
            n //= 10

        print("The Sum of Digits is :" + str(total))
    """,
    "Q38_Divisible_BY_3_5_Both.java": """
        print("Number divisible by 3:")
        for i in range(1, 101):
            if i % 3 == 0:
                print(i, end=" ")

        print()
        print("Number divisible by 5:")
        for i in range(1, 101):
            if i % 5 == 0:
                print(i, end=" ")

        print()
        print("Number divisible by 3 and 5:")
        for i in range(1, 101):
            if i % 3 == 0 and i % 5 == 0:
                print(i, end=" ")

        print()
    """,
    "Q40_Weekday.java": """
        n = int(input())

        if n == 1:
            print("Monday")
        elif n == 2:
            print("Tuesday")
        elif n == 3:
            print("Wednesday")
        elif n == 4:
            print("Thursday")
        elif n == 5:
            print("Friday")
        elif n == 6:
            print("Saturday")
        elif n == 7:
            print("Sunday")
        else:
            print("Invalid Day")
    """,
    "Q41_Number_of_Days_in_a_Month.java": """
        print("Enter Your Year :")
        year = int(input())

        print("Enter Your Month :")
        month = int(input())

        if month == 1:
            print("January " + str(year) + " has :" + str(31) + " days")
        elif month == 2:
            if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
                feb = 29
            else:
                feb = 28
            print("February " + str(year) + " has :" + str(feb) + " days")
        elif month == 3:
            print("March " + str(year) + " has :" + str(31) + " days")
        elif month == 4:
            print("April " + str(year) + " has :" + str(30) + " days")
        elif month == 5:
            print("May " + str(year) + " has :" + str(31) + " days")
        elif month == 6:
            print("June " + str(year) + " has :" + str(30) + " days")
        elif month == 7:
            print("July " + str(year) + " has :" + str(31) + " days")
        elif month == 8:
            print("August " + str(year) + " has :" + str(31) + " days")
        elif month == 9:
            print("September " + str(year) + " has :" + str(30) + " days")
        elif month == 10:
            print("October " + str(year) + " has :" + str(31) + " days")
        elif month == 11:
            print("November " + str(year) + " has :" + str(30) + " days")
        elif month == 12:
            print("December " + str(year) + " has :" + str(31) + " days")
        else:
            print("Invalid Month")
    """,
    "Q42_Decimal_to_Octal.java": """
        print("Enter a decimal number: ", end="")
        decimal = int(input())

        if decimal == 0:
            print("Octal : 0")
        else:
            digits = []

            while decimal > 0:
                remainder = decimal % 8
                digits.append(str(remainder))
                decimal //= 8

            print("Octal : " + "".join(reversed(digits)))
    """,
    "Q43_Octal_to_Decimal.java": """
        n = input().strip()
        x = 1
        ans = 0

        for digit in reversed(n):
            ans += int(digit) * x
            x *= 8

        print(ans)
    """,
    "Q44_Binary_to_Octal.java": """
        n = input().strip()
        decimal = 0
        base = 1

        for digit in reversed(n):
            decimal += int(digit) * base
            base *= 2

        if decimal == 0:
            print(0)
        else:
            digits = []
            while decimal > 0:
                digits.append(str(decimal % 8))
                decimal //= 8
            print("".join(reversed(digits)))
    """,
    "Q45_Add_Two_Octal.java": """
        def octal_to_decimal(value):
            total = 0
            multiplier = 1
            while value > 0:
                total += (value % 10) * multiplier
                value //= 10
                multiplier *= 8
            return total


        def decimal_to_octal(value):
            if value == 0:
                return 0

            result = 0
            multiplier = 1
            while value > 0:
                result += (value % 8) * multiplier
                value //= 8
                multiplier *= 10
            return result


        a = int(input())
        b = int(input())
        total = octal_to_decimal(a) + octal_to_decimal(b)
        print(decimal_to_octal(total))
    """,
    "Q46_Octal_Substraction.java": """
        def octal_to_decimal(value):
            total = 0
            multiplier = 1
            while value > 0:
                total += (value % 10) * multiplier
                value //= 10
                multiplier *= 8
            return total


        def decimal_to_octal(value):
            if value == 0:
                return 0

            result = 0
            multiplier = 1
            while value > 0:
                result += (value % 8) * multiplier
                value //= 8
                multiplier *= 10
            return result


        a = int(input())
        b = int(input())
        decimal1 = octal_to_decimal(a)
        decimal2 = octal_to_decimal(b)

        if decimal1 >= decimal2:
            diff = decimal1 - decimal2
        else:
            diff = decimal2 - decimal1

        print(decimal_to_octal(diff))
    """,
    "Q47_Multiply_Two_Octal.java": """
        def octal_to_decimal(value):
            total = 0
            multiplier = 1
            while value > 0:
                total += (value % 10) * multiplier
                value //= 10
                multiplier *= 8
            return total


        def decimal_to_octal(value):
            if value == 0:
                return 0

            result = 0
            multiplier = 1
            while value > 0:
                result += (value % 8) * multiplier
                value //= 8
                multiplier *= 10
            return result


        a = int(input())
        b = int(input())
        mul = octal_to_decimal(a) * octal_to_decimal(b)
        print(decimal_to_octal(mul))
    """,
    "Strong_Number.java": """
        def fact(n):
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result


        n = int(input())
        temp = n
        res = 0

        while temp != 0:
            rem = temp % 10
            res += fact(rem)
            temp //= 10

        if n == res:
            print("Yes it's Strong Number ")
        else:
            print("No , not strong Number")
    """,
    "Sum_Digits.java": """
        n = int(input())
        total = 0

        while n != 0:
            total += n % 10
            n //= 10

        print(total)
    """,
    "Swap_number.java": """
        a = int(input())
        b = int(input())
        a = a + b
        b = a - b
        a = a - b
        print(str(a) + " " + str(b))
    """,
    "Pattern/Q48_Square.java": """
        for _ in range(5):
            for _ in range(5):
                print("*", end=" ")
            print()
    """,
    "Pattern/Q49_Left_aligned_triangle.java": """
        for i in range(1, 6):
            for _ in range(1, i + 1):
                print("*", end=" ")
            print()
    """,
    "Pattern/Q50_Num_Pyramid.java": """
        for i in range(1, 6):
            for j in range(1, i + 1):
                print(j, end="")
            print()
    """,
    "Pattern/Q51_Num_Pyramid2.java": """
        for i in range(1, 7):
            for _ in range(1, i + 1):
                print(i, end="")
            print()
    """,
    "Pattern/Q52_Inverted_Pyramid.java": """
        for i in range(6, 0, -1):
            for _ in range(i, 0, -1):
                print("*", end="")
            print()
    """,
    "Pattern/Q53_Num_Inverted_Pyramid.java": """
        for i in range(6, 0, -1):
            for j in range(1, i + 1):
                print(j, end="")
            print()
    """,
    "Pattern/Q54_Triangle.java": """
        for i in range(1, 6):
            for _ in range(5 - i, 0, -1):
                print(" ", end="")
            for _ in range(1, 2 * i):
                print("*", end="")
            print()
    """,
    "Pattern/Q55_Inverted_triangle.java": """
        n = int(input())

        for i in range(n, 0, -1):
            for _ in range(0, n - i):
                print(" ", end="")
            for _ in range(0, 2 * i - 1):
                print("*", end="")
            print()
    """,
    "Pattern/Q56_Diamond_Half.java": """
        n = 5

        for i in range(1, n + 1):
            for _ in range(1, i + 1):
                print("*", end=" ")
            print()

        for i in range(1, n):
            for _ in range(n - 1, i - 1, -1):
                print("*", end=" ")
            print()
    """,
    "Pattern/Q57_Triangle_0_1.java": """
        n = int(input())

        for i in range(1, n + 1):
            for j in range(1, i + 1):
                if (j + i) % 2 == 0:
                    print("1", end=" ")
                else:
                    print("0", end=" ")
            print()
    """,
    "Pattern/Q58_Num_Palindrome.java": """
        n = int(input())

        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, end="")
            for _ in range(1, 2 * (n - i) + 1):
                print(" ", end="")
            for k in range(i, 0, -1):
                print(k, end="")
            print()
    """,
    "Pattern/Q59_Floyd_Triangle.java": """
        n = int(input())
        count = 1

        for i in range(1, n + 1):
            for _ in range(1, i + 1):
                print(str(count) + " ", end="")
                count += 1
            print()
    """,
    "Pattern/Q60_Char_Pyramid.java": """
        for i in range(1, 7):
            value = ord("A")
            for _ in range(1, i + 1):
                print(chr(value), end=" ")
                value += 1
            print()
    """,
    "Pattern/Q61_Char_Inverted_Pyramid.java": """
        for i in range(6, 0, -1):
            value = ord("A")
            for _ in range(1, i + 1):
                print(chr(value), end=" ")
                value += 1
            print()
    """,
    "Pattern/Q62_Char_Inverted_Pyramid.java": """
        value = ord("A")

        for i in range(1, 7):
            for _ in range(1, i + 1):
                print(chr(value), end=" ")
            value += 1
            print()
    """,
    "Pattern/Q63_Num_Pyramid.java": """
        n = int(input())

        for i in range(n, 0, -1):
            for j in range(n, i - 1, -1):
                print(str(j) + " ", end="")
            print()
    """,
    "Pattern/Q64_Char_Pyramid.java": """
        n = int(input())
        arr = ["E", "F", "E", "D", "C"]

        for i in range(n):
            for j in range(i + 1):
                print(arr[j], end=" ")
            print()
    """,
    "Pattern/Q65_Char_Triangle.java": """
        for i in range(1, 6):
            for _ in range(5, i, -1):
                print(" ", end="")

            ch = ord("A")
            for _ in range(1, i + 1):
                print(chr(ch), end="")
                ch += 1

            ch -= 2
            for _ in range(1, i):
                print(chr(ch), end="")
                ch -= 1

            print()
    """,
    "Pattern/Q66_Hollow_Diamond.java": """
        n = int(input())

        for i in range(n, 0, -1):
            for _ in range(1, i + 1):
                print("*", end="")
            for _ in range(1, 2 * (n - i) + 1):
                print(" ", end="")
            for _ in range(1, i + 1):
                print("*", end="")
            print()

        for i in range(1, n + 1):
            for _ in range(1, i + 1):
                print("*", end="")
            for _ in range(1, 2 * (n - i) + 1):
                print(" ", end="")
            for _ in range(1, i + 1):
                print("*", end="")
            print()
    """,
    "Pattern/Q67_Butterfly.java": """
        n = int(input())

        for i in range(1, n + 1):
            for _ in range(1, i + 1):
                print("*", end=" ")
            for _ in range(2 * (n - i), 0, -1):
                print("  ", end="")
            for _ in range(1, i + 1):
                print("*", end=" ")
            print()

        for i in range(n, 0, -1):
            for _ in range(i, 0, -1):
                print("*", end=" ")
            for _ in range(2 * (n - i), 0, -1):
                print("  ", end="")
            for _ in range(i, 0, -1):
                print("*", end=" ")
            print()
    """,
    "Pattern/Q68_Hollow_Square.java": """
        n = int(input())
        m = int(input())

        for i in range(0, n + 1):
            for j in range(0, m + 1):
                if i == 0 or j == 0 or i == n or j == m:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    """,
}


def extract_comments(source_path: Path) -> str:
    comment_lines = []

    for line in source_path.read_text(encoding="utf-8", errors="ignore").splitlines():
        cleaned = line.replace("\xa0", " ").replace("Â", "")
        stripped = cleaned.lstrip()

        if stripped.startswith("//"):
            indent = cleaned[: len(cleaned) - len(stripped)]
            comment_lines.append(f"{indent}#{stripped[2:]}")

    return "\n".join(comment_lines).strip()


def build_file_content(source_path: Path, body: str) -> str:
    comments = extract_comments(source_path)
    python_body = textwrap.dedent(body).strip()

    if comments:
        return comments + "\n\n\n" + python_body + "\n"
    return python_body + "\n"


def main() -> None:
    for relative_path, body in BODIES.items():
        source_path = JAVA_ROOT / relative_path
        destination_path = PYTHON_ROOT / relative_path.replace(".java", ".py")
        destination_path.parent.mkdir(parents=True, exist_ok=True)
        destination_path.write_text(build_file_content(source_path, body), encoding="utf-8")


if __name__ == "__main__":
    main()
