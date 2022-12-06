import pandas as pd
import pexpect.popen_spawn as psp

class WinPexpect():
    def __init__(self):
        self.process = psp.PopenSpawn("cmd.exe")
        self.prompt = ">"
        self.process.expect(self.prompt, timeout=10)
        lines = self.cmd_readlines()
        if lines != None:
            print(lines)

    def cmd_readlines(self):
        res = self.process.before.decode("shift-jis", errors="ignore") + self.process.after.decode("shift-jis", errors="ignore")
        return res

    def cmd_sendline(self, cmd, timeout=10):
        self.process.sendline(cmd)
        self.process.expect(self.prompt, timeout=timeout)


if __name__ == '__main__':
    df = pd.read_csv('test.csv')

    proc = WinPexpect()
    for index, row in df.iterrows():
        cmd = f"echo {row['param1']} {row['param2']}"
        proc.cmd_sendline(cmd)
        print(proc.cmd_readlines(), end='')

