from collections import deque


def list_manipulator(initial_list, *args):
    second, third, *res = args
    if second == "add" and third == "beginning":
        initial_list = res + initial_list
        return initial_list

    elif second == "remove" and third == "end":
        if res:
            n = int(res[0])
            for i in range(n):
                initial_list.pop()
        else:
            initial_list.pop()
        return initial_list

    elif second == "remove" and third == "beginning":
        initial_list = deque(initial_list)
        if res:
            n = int(res[0])
            for i in range(n):
                initial_list.popleft()
        else:
            initial_list.popleft()
        initial_list = list(initial_list)
        return initial_list

    elif second == "add" and third == "end":
        initial_list += res
        return initial_list


print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))

