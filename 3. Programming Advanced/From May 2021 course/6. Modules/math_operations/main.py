from math_operations.mappper import operation_mapper


num_1, oper, num_2 = input().split()
num_1 = float(num_1)
num_2 = float(num_2)

print(operation_mapper[oper](num_1, num_2) if operation_mapper.get(oper) else "Invalid operator")

