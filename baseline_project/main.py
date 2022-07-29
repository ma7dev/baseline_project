import os

def cmd_run(input_cmd):
    os.system(f'ping -c2 {input_cmd}')

if __name__ == "__main__":
    input_user = input('Enter a website: ')
    print(cmd_run(input_user))