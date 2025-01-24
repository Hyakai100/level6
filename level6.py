def is_integer(value):
    """値が整数かどうかを判定する"""
    try:
        int(value)
        return True
    except ValueError:
        return False

def binary_search(arr, target):
    """二部探索を行う関数"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# カンマ区切りの整数をリストに追加
int_list = []
while True:
    inputs = input("カンマ区切りの整数を入力してください: ").split(',')
    valid = True
    for item in inputs:
        if not is_integer(item.strip()):
            print("整数のみを入力してください。")
            valid = False
            break
    if valid:
        int_list.extend([int(item.strip()) for item in inputs])
        break

# リストを昇順にソート
int_list.sort()
print(f"昇順にソートされたリスト: {int_list}")

# 整数Nを入力
while True:
    n_input = input("整数Nを入力してください: ")
    if is_integer(n_input):
        n = int(n_input)
        break
    else:
        print("整数を入力してください。")

# 二部探索を実行
index = binary_search(int_list, n)
print(index)
