

def print_msg(msg, error, *kwargs):
	print("Log : "+error+":" + msg)
	print(kwargs)

print_msg("Passing function", "file not found","1","2","3","4","5","6","7")
