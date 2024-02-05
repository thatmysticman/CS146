def is_palindrome(input):
    # Check if the string is empty
    if input == "" or input == " ":
        print("Invalid Input!")
        return False
        
    # Convert to lowercase and remove non-alphanumeric characters
    newInput = ''.join(c.lower() for c in input if c.isalnum())

    # Check if the cleaned string is a palindrome
    left, right = 0, len(newInput) - 1
    while left < right:
        if newInput[left] != newInput[right]:
            return False
        left += 1
        right -= 1
    return True
