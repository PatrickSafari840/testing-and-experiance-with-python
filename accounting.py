def accounting():
  """
  This function creates a basic accounting table with user-defined Assets and Liabilities
  and displays the totals at the end.
  """
  # Create empty dictionaries for Assets and Liabilities
  assets = {}
  liabilities = {}

  # Get user input for Assets
  print("Enter Assets (type 'done' when finished):")
  while True:
    item = input("\tName: ")
    if item.lower() == "done":
      break
    value = float(input("\tValue: "))
    assets[item] = value

  # Get user input for Liabilities
  print("\nEnter Liabilities (type 'done' when finished):")
  while True:
    item = input("\tName: ")
    if item.lower() == "done":
      break
    value = float(input("\tValue: "))
    liabilities[item] = value

  # Calculate the total Assets and Liabilities
  total_assets = sum(assets.values())
  total_liabilities = sum(liabilities.values())

  # Print the table header
  print("-" * 30)
  print("Accounting")
  print("-" * 30)

  # Print the Assets section
  print("Assets:")
  for item, value in assets.items():
    print(f"\t{item}: {value}")

  # Print the Liabilities section
  print("\nLiabilities:")
  for item, value in liabilities.items():
    print(f"\t{item}: {value}")

  # Print the totals
  print("\nTotal Assets:", total_assets)
  print("Total Liabilities:", total_liabilities)

  # Check if Assets and Liabilities are equal
  if total_assets == total_liabilities:
    print("-"*100)
    print("The accounting is balanced.")
    print("-"*100)
  else:
    lake = total_assets - total_liabilities
    print("-"*100)
    print("The accounting is not balanced.")
    print(f"the laking element is of {lake} valiu. ")
    print("-"*100)

# Call the accounting function
accounting()
