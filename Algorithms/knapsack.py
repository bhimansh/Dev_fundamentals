def zero_one_knapsack(w, val, capacity):
    hashmap = {x:y for x,y in zip(w,val)}
    stack = []
    for w in sorted(hashmap.keys()):
        if capacity - w >= 0:
            stack.append((w, hashmap.get(w)))
            capacity -= w
        else:
            last_w = stack[-1][0]
            last_v = stack[-1][1]
            if capacity + last_w - w >=0:
                stack.pop()
                stack.append((w, hashmap.get(w)))
                capacity -= w
    print(stack)

def zero_one_knapsack_dp(w, val, capacity):
    hashmap = {(0): 0}
    for i in range(len(val)):
        curr = hashmap.copy()
        for wt in hashmap:
            if wt + w[i] <= capacity:
                new_w = wt + w[i]
                new_v = val[i] + hashmap[wt]
                if new_w not in curr or new_v > curr[new_w]:
                    curr[new_w] = new_v
        print(hashmap)
        hashmap = curr
    print(hashmap)
    print(max(hashmap.values()))


if __name__ == "__main__":
    weights = [10, 20, 40]
    values = [100, 120, 200]
    capacity = 50
    print(zero_one_knapsack(weights, values, capacity))
    # print(zero_one_knapsack_dp(weights, values, capacity))