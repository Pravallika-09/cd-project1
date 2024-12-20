from collections import defaultdict


def get_days_to_reach_k(num_employees, num_friends, connections, target_k):
    friends = defaultdict(list)
    for a, b in connections:
        friends[a].append(b)
        friends[b].append(a)

    status = [1] * num_employees  # 1 for WFO, 0 for WFH
    roster_value = num_employees
    days = 1

    while roster_value < target_k:
        new_status = [0] * num_employees
        roster_value = 0

        for emp in range(num_employees):
            wfo_count = sum(status[friend] for friend in friends[emp])
            if status[emp] == 1:  # WFO today
                new_status[emp] = 1 if wfo_count == 3 else 0
            else:  # WFH today
                new_status[emp] = 1 if wfo_count < 3 else 0

            roster_value += new_status[emp]

        status = new_status
        days += 1

    return days


# Taking user input
n, m = map(int, input("Enter number of employees and friendships (space-separated): ").split())
connections = []
print("Enter the friendships (space-separated pairs):")
for _ in range(m):
    a, b = map(int, input().split())
    connections.append((a, b))
k = int(input("Enter the target rostering value: "))

# Output the result
print(get_days_to_reach_k(n, m, connections, k))