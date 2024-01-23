# Loop through each row (multiplier)
for row in range(1, 11):
    # Loop through each column (multiplicand)
    for col in range(1, 11):
        # Multiply the row and column values
        product = row * col
        # Pad the product with spaces to align columns
        print(f"{product:3}", end=" ") # adjust number of spaces and align right
    # Newline after each row
    print("")