import datetime
import os
import stat

SETTINGS = {'op1': 1, 'op2': 1, 'op3': 1, 'op4': 1, 'op5': 1}
PARAMS = {'precision': None, 'dest': None}


def load(file="params.ini"):
    global PARAMS, SETTINGS
    with open(file, mode='r', errors='ignore') as f:
        lines = f.readlines()
    for l in lines:
        key, val = l.strip().split('=')
        if key != 'dest':
            val = eval(val)
        if file == "params.ini":
            PARAMS[key] = val
        elif file == "settings.ini":
            SETTINGS[key] = val


def write_log(*args, action=None, result=None, file='calc-history.log.txt', full_blok=False):
    filename = 'newoutput.txt'
    filename2 = 'newoutput.txt.txt'
    new_permissions = stat.S_ENFMT
    try:
        os.chmod(filename, new_permissions)
        if full_blok:
            os.chmod(filename2, new_permissions)
    except FileNotFoundError:
        pass  # игнорируем отсутствие файла

    date = datetime.datetime.today()
    try:
        with open(file, mode='a', errors='ignore') as f:
            f.write(f'Run program\n')
            f.write(f'Date {date.strftime("%d/%m/%Y")}\n')
            f.write(f'Time {date.strftime("%H/%M/%S")}\n')
            f.write(f'Operation {action}: {args} = {result}\n')
    except PermissionError:
        file_new = file + '.txt'
        with open(file_new, mode='a', errors='ignore') as backup_file:
            backup_file.write(f"{action}: {args} = {result}\n")


def calculate(**kwargs):
    args = [arg for arg in kwargs.values()]
    res = sum(args)
    write_log(*args, action='sum', result=res)
    print(f'Операция sum: {args} = {res} \nРезультат: {res}')
    return res


def main():
    load("params.ini")
    load("settings.ini")
    calculate(**SETTINGS)
    print("\nДля изменения параметров суммирования измените значения в settings.ini\n")
