###########################################################################
#Логи
def fLogs(file_path: str) -> list[dict]:
    logs = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            log_entry = {}
            parts = line.split(', ')#ключи-значения
            for part in parts:
                key, value = part.split(': ', 1)
                log_entry[key] = value
            logs.append(log_entry)
    return logs


##############################################################
#1 - статистика, период
def date(logs: list[dict]) -> list[str]:
    dates = [log['date_connected'].split(' ')[0] for log in logs]
    min_date = min(dates, key=lambda d: list(map(int, d.split('/')[::-1])))
    max_date = max(dates, key=lambda d: list(map(int, d.split('/')[::-1])))
    return [min_date, max_date]


########################################################################
#2. Новые юзеры
def uniqueUser_num(logs: list[dict]) -> int:
    usernames = {log['username'] for log in logs}
    return len(usernames)


##########################################################################
#3. Кол-во подключений для юзера
def connect_num(logs: list[dict]) -> dict:
    connections = {}
    for log in logs:
        user = log['username']
        connections[user] = connections.get(user, 0) + 1
    return connections


##################################################################################
#4. Уникальные IP
def uniqueIP(logs: list[dict]) -> dict:
    user_ips = {}
    for log in logs:
        user = log['username']
        ip = log['ip']
        if user not in user_ips:
            user_ips[user] = set()
        user_ips[user].add(ip)
    return {user: list(ips) for user, ips in user_ips.items()}


#######################################################################################
#5. Кол-во уникальных IP
def uniqueIP_num(logs: list[dict]) -> dict:
    unique_ips = uniqueIP(logs)
    return {user: len(ips) for user, ips in unique_ips.items()}

#Якщо треба вивести відповіді на завдання розкоментувати
# if __name__ == '__main__':
#     logs = fLogs('test_logs.txt')
#
#     #1
#     print(date(logs))
#     #2
#     print(uniqueUser_num(logs))
#     #3
#     print(connect_num(logs))
#     #4
#     print(uniqueIP(logs))
#     #5
#     print(uniqueIP_num(logs))