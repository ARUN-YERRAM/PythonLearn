def is_palindrome(n):
    return str(n) == str(n)[::-1]

def find_closest_palindrome(num):
    smaller = int(num) - 1
    larger = int(num) + 1

    while True:
        if is_palindrome(str(smaller)) or is_palindrome(str(larger)):
            break
        smaller -= 1
        larger += 1

    diff_smaller = abs(int(num) - smaller)
    diff_larger = abs(int(num) - larger)

    if diff_smaller <= diff_larger:
        return smaller
    else:
        return larger

num=input()
if((int(num)<=9) and (int(num)>=0) or is_palindrome(str(num))):
    # print(is_palindrome(str(num)))
    print("Palindrome")
else:
    print(find_closest_palindrome(num))