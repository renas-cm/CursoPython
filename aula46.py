try:
    a = 18
    b = 0
    print(a / b)
except ZeroDivisionError:
    print('Error: Division by zero is not allowed.')
except NameError as e:
    print(f'Error: Variable is not defined. Details: {e}')
except (TypeError, IndexError) as error:
    print(f'Error: Type or Index issue occurred. Details: {error}')
except Exception as e:
    print(f'Unexpected error occurred: {e}')
else:
    print('No errors occurred.')
finally:
    print('Execution completed.')