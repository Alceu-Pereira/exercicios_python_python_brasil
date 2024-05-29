ws = 0
unix = 0
linux = 0
netware = 0
macos = 0
other = 0

results = []
results_percentage = []
os_list = ['Windows Server', 'Unix', 'Linux', 'Netware','MacOS', 'Other']

while True:
    print('1 - Windows Server\n2 - Unix\n3 - Linux\n4 - Netware\n5 - Mac OS\n6 - Other')
    os_question = int(input('What is the best OS to use on servers? '))
    if os_question == 0:
        break
    elif 1 <= os_question <= 6:
        if os_question == 1:
            ws += 1
        elif os_question == 2:
            unix += 1
        elif os_question == 3:
            linux += 1
        elif os_question == 4:
            netware += 1
        elif os_question == 5:
            macos += 1
        else:
            other += 1
    else:
        print('Invalid command')
        continue

results.extend([ws, unix, linux, netware, macos, other])
total_results = sum(results)

more_votes = max(results)


for v in results:
    if total_results != 0:
        percentage = round(((v / total_results) * 100), 5)
        results_percentage.append(percentage)
    else:
        results_percentage.append(0)


print(f"{'Operational System':<30} {'Votes':<15} {'% ':<4}")
print(f"{(18 * '-'):<30} {'-----':<15} {'---':<4}")
print(f"{'Windows Server':<30} {f'{ws}':<15} {f'{results_percentage[0]}%':<4}")
print(f"{'Unix':<30} {f'{unix}':<15} {f'{results_percentage[1]}%':<4}")
print(f"{'Linux':<30} {f'{linux}':<15} {f'{results_percentage[2]}%':<4}")
print(f"{'Netware':<30} {f'{netware}':<15} {f'{results_percentage[3]}%':<4}")
print(f"{'Mac OS':<30} {f'{macos}':<15} {f'{results_percentage[4]}%':<4}")
print(f"{'Other':<30} {f'{other}':<15} {f'{results_percentage[5]}%':<4}")
print(f"{(18 * '-'):<30} {'-----':<15} {'---':<4}")
print(f"{'Total':<30} {sum(results):<15}")
try:
    print(f'The more voted OS was {os_list[results.index(max(results))]}, with {max(results)} votes, that correspondig to {results_percentage[results.index(max(results))]} % of the votes.')
except:
    print("Doesn't have any vote")