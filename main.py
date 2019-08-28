# Future updates:
# 1. Encrypt password when saving into the info.txt
# 2. Decrypt password on get request
# 3. Add more relation between chrome and script
# 4. To be continued...


import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from password.generate import Resources

# path to file with passwords
file = '/home/aibek/Programming/PyCharm/scripts/password/driver/info.txt'


# class that handles command
class Init:
    def __init__(self):
        self.valid = False
        # if there are arguments in command line
        if len(sys.argv) > 1:
            self.valid = True
            self.command = sys.argv[1]
        self.handle()

    def handle(self):
        # if command is GET, then no need to generate password using selenium
        if self.valid and str(self.command).lower() == 'get':
            res = self.GetPass(url=sys.argv[2])
            if len(res):
                for i in res:
                    print(i)
        else:
            # generate Password on init
            handle = Resources()
            # if there are commands
            if self.valid:
                # if command is UPDATE, then change password
                if str(self.command).lower() == 'update':
                    handle.UpdatePassword(url=sys.argv[2], username=sys.argv[3])
                # if command is INSERT, then add url, username and password to file
                elif str(self.command).lower() == 'insert':
                    handle.AddAccount(url=sys.argv[2], username=sys.argv[3])

    # method to get password from file
    @staticmethod
    def GetPass(url):
        res = []
        with open(file, 'r+') as f:
            for line in f:
                s = line.split(' ')
                if s[0] in url or url in s[0]:
                    val = s[1] + ' ' + s[2][:-1]
                    res.append(val)
        f.close()
        return res


if __name__ == '__main__':
    Init()
