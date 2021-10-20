def music(numbers):
    chorus = [
    "Never gonna give you up",
    "Never gonna let you down",
    "Never gonna run around and desert you",
    "Never gonna make you cry",
    "Never gonna say goodbye",
    "Never gonna tell a lie and hurt you",
    ]
    ans = []
    for i in range(len(numbers)):
        if i % 2 == 0:
            ans.append(chorus[numbers[i]])
        else:
            ans.append(chorus[numbers[i]].replace('Never gonna', 'NEVER GONNA'))
    return ans