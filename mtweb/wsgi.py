#from HaCRSUI import app
#app.run(host="0.0.0.0", port=8182)

import sys

ADMIN = 1
USER = 0
MODE = USER
def main(mode=0):
	if mode == USER:
		from mtweb.HaCRSUI import app
		#print("USER Mode")
		#app.run(port=8182)
		app.run(host="0.0.0.0", port=8182)
	elif mode == ADMIN:
		from mtweb.HaCRSAdmin import app
		print("ADMIN Mode")
		#app.run(port=8989)
		app.run(host="0.0.0.0", port=8989)

if __name__ == "__main__":
	arguments = sys.argv
	print(arguments)
	for arg in arguments:
		if arg in ["-a", "--admin"]:
			main(ADMIN)
		else:
			main(USER)

    #app.run(port=8182)
