import subprocess

def run_sqlmap_with_stdin(file_path):
    # cmd = f'sqlmap -r {file_path} --dbs'
    cmd = 'python sqlmapapi.py -s'
    #cmd = 'python -version'
    print(cmd)
    # with open(file_path, 'r') as f:
    #     request_content = f.read()
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = proc.communicate()

    return stdout, stderr

# 示例用法
file_path = 'C:/Users/86185/Desktop/post.txt'
stdout, stderr = run_sqlmap_with_stdin(file_path)
print(stdout)


