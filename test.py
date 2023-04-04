import os, subprocess

TEST_DIR = "."
CODE_FILE = "main.c"
COMPILER_TIMEOUT = 10.0
RUN_TIMEOUT = 10.0

code_path = os.path.join(TEST_DIR, CODE_FILE)
app_path = os.path.join(TEST_DIR, "app")

print("Building...")
try:
	ret = subprocess.run(['gcc', code_path, '-o', app_path],
							stdout=subprocess.PIPE, stderr=subprocess.PIPE,
							timeout=COMPILER_TIMEOUT)

except Exception as e:
	print("ERROR: Compilation failed.", str(e))
	exit(1)
	
output = ret.stdout.decode('utf-8')
print(output)
output = ret.stderr.decode('utf-8')
print(output)

if ret.returncode != 0:
	print('Compilation failed.')
	exit(1)

print("Running...")
try:
	ret = subprocess.run([app_path],
		      stdout=subprocess.PIPE,
			  timeout=RUN_TIMEOUT)
	
except Exception as e:
	print("ERROR: Runtime failed.", str(e))
	exit(1)

output = ret.stdout.decode('utf-8')
print(output)

print("All tests passed !!!")
exit(0)