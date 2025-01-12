def is_palindrome_str(x: int) -> bool:
    number_string: str = str(x)
    return number_string ==  number_string[::-1]


if __name__ == '__main__':
    print(is_palindrome_str(121))
    print(is_palindrome_str(10))
