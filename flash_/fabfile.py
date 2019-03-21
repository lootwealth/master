# apt install fabric
# fab -H node100,node102,node104,node106 flash:"-a"
# fab -H node100,node102,node104,node106 flash:"-b -g 0"


from fabric.api import *

env.user = 'mos'
env.password = 'mos'

@task
def flash(param="-a"):
	local("test -f nvflash_linux || wget http://cdn.mineros.cn/tmp/nvflash_linux; chmod +x nvflash_linux")
	local("test -f nvflash.sh || wget http://cdn.mineros.cn/tools/nvflash10.sh -O nvflash.sh; chmod +x nvflash.sh")
	
	with cd("/home/mos"):
		if param.find('-a') >=0:
			local("test -f 11.rom || wget http://update.mineros.cn/targets/bios/11.rom")
			put("11.rom", "./")
		if param.find('-b') >=0:
			local("test -f 11.rom || wget http://update.mineros.cn/targets/bios/22.rom")
			put("22.rom", "./")

		put("nvflash_linux", "./")
		put("nvflash.sh", "./")
		
		sudo('cat nvflash.sh | bash -s -- {}'.format(param))
		sudo('echo "* * * * * sudo reboot" | crontab -')
