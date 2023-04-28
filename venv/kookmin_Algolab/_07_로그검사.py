t = int(input())

for _ in range(t):
    n = int(input())
    errors = {'line_name': set(), 'product_name': set(), 'error_level': set(), 'message': set()}
    count = 0

    for _ in range(n):
        log = input().strip().split()
        log_dict = {}

        for field in log:
            key, value = field.split(':')
            log_dict[key.strip()] = value.strip()

        valid = True
        for key in errors:
            if key not in log_dict:
                errors[key].add('')
            elif len(log_dict[key]) == 0:
                errors[key].add('')
                valid = False
            elif not log_dict[key].isalnum():
                errors[key].add(log_dict[key])
                valid = False

        if not valid:
            count += 1

    print(count)
