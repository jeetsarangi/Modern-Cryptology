import pexpect

input = open("plaintexts.txt", 'r')
output = open("ciphertexts.txt",'w')

temp = input.readlines()

for line in temp:
    li = line.split()

    child = pexpect.spawn('/usr/bin/ssh students@172.27.26.188')
    child.expect('students@172.27.26.188\'s password:')
    child.sendline('cs641a')
    child.expect('Enter your group name: ', timeout=100) 
    child.sendline("Goldfish")

    child.expect('Enter password: ', timeout=50)
    child.sendline("alok21111008")

    child.expect('\r\n\r\n\r\nYou have solved 5 levels so far.\r\nLevel you want to start at: ', timeout=50)
    child.sendline("5")

    child.expect('.*')
    child.sendline("go")

    child.expect('.*')
    child.sendline("wave")

    child.expect('.*')
    child.sendline("dive")

    child.expect('.*')
    child.sendline("go")

    child.expect('.*')
    child.sendline("read")

    child.expect('.*')

    child.sendline("ffffffffffffffff")
    child.expect("Slowly, a new text starts*")
    child.sendline("c")
    child.expect('The text in the screen vanishes!')
    
    
    for i in range(len(li)-1):
        
        child.sendline(li[i+1])
        s = str(child.before)[48:64]
        print(s)
        output.write(s)
        output.write(" ")
        child.expect("Slowly, a new text starts*")
        child.sendline("c")
        child.expect('The text in the screen vanishes!')

    child.sendline("ffffffffffffffff")
    s = str(child.before)[48:64]
    print(s)
    output.write(s)
    output.write(" ")
    child.expect("Slowly, a new text starts*")
    child.sendline("c")
    child.expect('The text in the screen vanishes!')

    output.write("\n")
    child.close()


input.close()
output.close()