def is_palindrome(s):
    # Convert to lowercase and remove non-alphanumeric characters
    cleaned_string = ''.join(c.lower() for c in s if c.isalnum())

    # Check if the cleaned string is a palindrome
    left, right = 0, len(cleaned_string) - 1
    while left < right:
        if cleaned_string[left] != cleaned_string[right]:
            return False
        left += 1
        right -= 1
    return True
