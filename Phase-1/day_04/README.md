# Day 4 — Exception & Error Handling

## Topics Covered

### 1. Errors vs Exceptions
Learned the difference between syntax errors, runtime exceptions, and logical errors.
Understood that exceptions occur during program execution and can disrupt the normal flow.

### 2. `try` and `except`
Learned how `try` is used for code that may cause an exception and `except` is used to handle it.
Practiced handling specific exceptions such as `ValueError` and `ZeroDivisionError`.

### 3. Multiple `except` Blocks
Learned how a single `try` block can have multiple exception handlers.
Understood that Python executes the first matching `except` block.

### 4. Exception Hierarchy
Learned that built-in exceptions are organized in a hierarchy.
Understood that specific exceptions should be handled before general `Exception`.

### 5. `else` and `finally`
Learned that `else` runs only when the `try` block completes successfully.
Learned that `finally` normally runs whether an exception occurs or not and is useful for cleanup.

### 6. `raise`
Learned how to deliberately raise an exception using the `raise` keyword.
Practiced using `raise` to validate inputs and enforce program rules.

### 7. Custom Exceptions
Learned how to create application-specific exceptions by inheriting from `Exception`.
Practiced creating and handling custom exceptions such as `InvalidAgeError`.

### 8. Exception Propagation
Learned that an unhandled exception can travel upward through the function call stack.
Understood how a higher-level function can handle an exception raised by a lower-level function.

### 9. Tracebacks
Learned how to read Python tracebacks to identify the exception type, cause, and location.
Practiced finding the actual problematic line and understanding the function call path.

### 10. Exception Handling Best Practices
Learned to catch specific exceptions instead of using overly broad exception handlers.
Practiced keeping `try` blocks focused and avoiding silently ignoring errors.

## Hands-on Practice

- Practiced `try` and `except`
- Handled multiple exception types
- Used `else` and `finally`
- Used `raise` for input validation
- Created custom exceptions
- Practiced exception propagation
- Learned to read tracebacks
- Built a Bank Account program with custom exceptions
- Practiced handling invalid withdrawals and insufficient balances

## Key Takeaways

- Syntax errors prevent Python from understanding the code.
- Exceptions occur during program execution.
- `try` → attempts risky code.
- `except` → handles an exception.
- `else` → runs when no exception occurs.
- `finally` → normally runs regardless of success or failure.
- `raise` → deliberately creates an exception.
- Custom exceptions → allow application-specific error handling.
- Exceptions can propagate through function calls.
- Tracebacks help identify where and why an exception occurred.
- Specific exceptions should generally be handled before general exceptions.

## Final Practice

### Bank Account Exception Handling

Implemented:
- `BankAccount` class
- Custom `InvalidAmountError`
- Custom `InsufficientBalanceError`
- Withdrawal validation
- `raise` and `try/except`
- Successful and failed withdrawal handling

