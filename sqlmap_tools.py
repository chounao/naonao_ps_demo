import subprocess
import os
import sys






# 获取包下所有文件的路径
class tools_sqlmap:
    def __init__(self):
        self.txt_file = 'C:/Users/86185/Desktop/mimt/sqlmap/batchDeleteShippingAddress.txt'
        self.package_path = os.getcwd()+'/save_txt'
    def get_package_files(self):
        file_paths = []
        for root, dirs, files in os.walk(self.package_path):
            for file in files:
                file_paths.append(os.path.join(root, file))
        return file_paths

    def execute_sqlmap(self):

        cmd = f"sqlmap -r {self.txt_file} -dbs"
        print(cmd)
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        print(p)
        output, error = p.communicate()
        print(output.decode())
        print(error.decode())

    def sqlmap_Tools(self):
        file_paths = self.get_package_files()
        # new_paths = [path.replace("/", "\\") for path in file_paths]

        targets = []
        for line in sys.stdin:
            target = line.strip()
            targets.append(target)


        # 在CMD中打印提示消息
        print("Using 'STDIN' for parsing targets list.")

        # 调用函数从STDIN解析目标列表
        target_list = targets

        # 打印解析后的目标列表
        print("Parsed Targets:")
        for target in target_list:
            print(target)


        command = f"sqlmap -r {self.txt_file} --dbs"


        try:
            # 执行CMD命令
            process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,text=True)
            # process.stdin.write('y')
            # process.stdin.flush()

            # if process.returncode is None
            output = process.stdout.readline()
            if output == '' and process.poll() is not  None:
                print("CMD command is still running.")

            if output:
                print(output)
                if 'Y/N' and 'token' in output:
                    # process.stdin.write(b'y\n')  # 输入 Y
                    process.stdin.write('n\n')
                elif 'Yes/No' in output and 'token' not in output:
                    process.stdin.write('y\n')  # 输入 Yes
                elif 'Continue?' in output:
                    process.stdin.write('C\n')  # 输入 C
                else:
                    # 其他情况下可以自定义输入
                    process.stdin.write('Control+c\n')
                    print("CMD command has finished with return code:", process.returncode)
                process.stdin.flush()

                # 获取CMD的输出
                output, error = process.communicate()

                # 输出命令的标准输出和标准错误
                print("Command Output:")
                print(output)
                print("Command Error:")
                print(error)

        except subprocess.CalledProcessError as e:
            print("Command execution failed with exit code", e.returncode)
            print("Command Error:")
            print(e.stderr)



if __name__ == '__main__':
    a = tools_sqlmap()
    a.execute_sqlmap()