def number_operations():
    numbers = []
    
    # Get 10 numbers from user
    print("Enter 10 numbers:")
    for i in range(10):
        numbers.append(int(input(f"Enter number [{i + 1}]: ")))
    
    # Display original list
    print(f"\nOriginal numbers: {numbers}")
    
    # Create filtered lists
    even_numbers = []
    odd_numbers = []
    
    # Calculate average
    average = sum(numbers) / len(numbers)
    
    # Numbers greater than average
    above_average = []
    
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

        if num > average:
            above_average.append(num)
    
    # Display results
    print("Even Numbers: ", even_numbers)
    print("Odd Numbers: ", odd_numbers)
    print("Numbers above average: ", above_average)
    print("Sum: ", sum(numbers))
    print("Average: ", average)
    print("Min: ", min(numbers))
    print("Max: ", max(numbers))

if __name__ == "__main__":
    number_operations()
