

def print_msg(msg, error, *kwargs):
	print("Log : "+error+":" + msg)
	print(kwargs[1])

print_msg("Passing function", "file not found","1","2","3","4","5","6","7")


def print_msg1(msg, error, **kwargs):
	print("Log : "+error+":" + msg)
	print(kwargs)

print_msg1("Passing function", "file not found",key_1="1,2,2,3,4")
def print_msg3(msg, error,*args, **kwargs):
	print("Log : "+error+":" + msg)
	print(args)
	print(kwargs)

print_msg3("Passing function", "file not found","-12","-1","0",key_1="1,2,2,3,4", key_2="5,6,7")
