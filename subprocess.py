#!/Library/Frameworks/Python.framework/Versions/3.8/bin
import subprocess
cmd="ls -lrt"
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
out,err=sp.communicate()
print(f"The return code is {rc}")
print(f"The output : \n {out.splitlines()}")
print(f"The error : \n {err.splitlines()}")
