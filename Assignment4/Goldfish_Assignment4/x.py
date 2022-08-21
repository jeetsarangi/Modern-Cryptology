import pexpect

child = pexpect.spawn('/usr/bin/ssh students@172.27.26.188')
child.expect('students@172.27.26.188\'s password:')
child.sendline('cs641a')
child.expect('Enter your group name: ', timeout=50) 
child.sendline("Goldfish")

child.expect('Enter password: ', timeout=50)
child.sendline("alok21111008")

child.expect('\r\n\r\n\r\nYou have solved 4 levels so far.\r\nLevel you want to start at: ', timeout=50)
# Note: After clearing level 4 this needs to be changed to "solved 4 levels so far"
child.sendline("4")

# child.expect('\r\nThe rumbling sound is very loud here. It is coming from \r\n your right side. A cold blast of air hits you sending \r\n shivers up your spine. You look in that direction. \r\n There is a large opening on the right from where the \r\n\tsound and the air is coming from. There is a fair amount\r\n\tof light also coming from that direction (you realize that\r\n\tyou have not lighted a matchstick and still you can see).\r\n\tThere is another door, with a panel nearby, to your left \r\n\twhich is closed. The chamber is rocky and cold. Another \r\n\tblast of air hits you from your right and you shiver again. \r\n\r\n> ', timeout=120)
# child.sendline("read")

child.expect('.*')
child.sendline("go")

child.expect('.*')
child.sendline("dive")

child.expect('.*')
child.sendline("dive")

child.expect('.*')
child.sendline("back")

child.expect('.*')
child.sendline("pull")

child.expect('.*')
child.sendline("back")

child.expect('.*')
child.sendline("back")

child.expect('.*')
child.sendline("go")

child.expect('.*')
child.sendline("wave")

child.expect('.*')
child.sendline("back")

child.expect('.*')
child.sendline("back")

child.expect('.*')
child.sendline("thrnxxtzy")

child.expect('.*')
child.sendline("read")

child.expect('.*')
child.sendline("134721542097659029845273957")

child.expect('.*')
child.sendline("c")

child.expect('.*')
child.sendline("read")


f = open("dummyplain1.txt", 'r')
f1= open("dummycipher1.txt",'w')


i=1
for line in f.readlines():
	child.expect('.*')
	child.sendline(line)
	child.expect("Slowly, a new text starts*")
	child.sendline("c")
	child.expect('The text in the screen vanishes!')
	f1.writelines(str(child.before)[48:64]+"\n")
	print(str(child.before)[48:64])
	print(i)
	i +=1



child.close()
# print(child.before, child.after)

f.close()
f1.close()