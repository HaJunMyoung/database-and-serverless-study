#This code written by HajunMyoung
#이 코드의 작성자는 명하준입니다

import time

# □ ■
print("Loading start\n")
time.sleep(1)

for i in range(0, 101):
    print("\r"+"■"*i+"□"*(100-i), end='')
    time.sleep(0.05)

print("\n\nDone!!!")