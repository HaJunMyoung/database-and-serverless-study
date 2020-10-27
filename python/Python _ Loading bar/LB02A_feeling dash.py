import time

for i in range(0, 51): 
    print('\r'+'['+'#'*i+'-'*(50-i)+"]"+" "+str(i*2)+"%", end='')
    time.sleep(0.02)