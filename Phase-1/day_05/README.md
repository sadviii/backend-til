# Day 5 — Debugging & Stack Traces

## Topics Covered

### 1. Understanding Debugging
Learned that debugging is the process of finding, understanding, and fixing problems in a program.
Understood the difference between syntax errors, runtime errors, and logic errors, and why `print()` debugging alone is not always enough.

### 2. Stack Traces
Learned how to read Python tracebacks from the bottom upward to identify the exception and its cause.
Practiced finding the exact file, line, function, and call path where an error occurred.

### 3. VS Code Debugger
Learned how to use the VS Code debugger instead of relying only on `print()` statements.
Practiced setting breakpoints, starting a debugging session, and using the Debug Console.

### 4. Step-Through Debugging
Learned how to control program execution one step at a time.

- `Continue` → Continues execution until the next breakpoint.
- `Step Over` → Executes the current line without entering a called function.
- `Step Into` → Enters a function call and allows its execution to be inspected.
- `Step Out` → Finishes the current function and returns to the calling function.

### 5. Inspecting Program State
Learned how to inspect variables while the program is paused.
Practiced using the Variables panel, Call Stack, and Debug Console to evaluate expressions and observe how values change during execution.

### 6. Debugging Logic Errors
Learned that a program can run successfully while still producing an incorrect result.
Practiced using breakpoints and variable inspection to find logic errors instead of relying only on error messages.

### 7. Debugging Functions
Learned how to follow function calls using `Step Into` and `Step Out`.
Practiced inspecting function parameters, local variables, return values, and the Call Stack.

### 8. Debugging Loops and Conditions
Practiced stepping through a loop iteration by iteration.
Learned how variables change, how conditions evaluate to `True` or `False`, and how those conditions affect the execution of the loop.

### 9. Finding the Root Cause
Learned the difference between identifying a symptom and finding the actual root cause of a bug.
Practiced tracing an incorrect value backward through multiple functions to find where the wrong value was originally produced.

### 10. Blank File Test
Built a Task Manager console application from a blank Python file without copying a complete solution.

The application supports:

- Adding tasks
- Viewing tasks
- Completing tasks
- Handling invalid task numbers
- Handling invalid menu choices
- Repeating the menu using a `while` loop
- Exiting the application

Used the VS Code debugger to investigate a deliberately introduced bug in task completion.

### Debugging Challenge

The bug was:

```python
tasks[task_number]["completed"] = True