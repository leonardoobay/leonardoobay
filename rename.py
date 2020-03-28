# Pythono3 code to rename multiple 
# files in a directory or folder 

# importing os module 
import os 

# Function to rename multiple files 
def main(): 
	i = 1
	path = os.getcwd() + "\\"
	for filename in os.listdir(os.getcwd()): 
		if i < 10:
		
			dst ="Naruto Shippuden - s01e0" + str(i) + ".mp4"
			src = path  +  filename 
			dst = path +  dst 
			
			# rename() function will 
			# rename all the files 
			os.rename(src, dst) 
			i += 1	

			
		else:
			dst ="Naruto Shippudennn - s01e" + str(i) + ".mp4"
			src = path  +  filename 
			dst = path +  dst 
			
			# rename() function will 
			# rename all the files 
			os.rename(src, dst) 
			i += 1

# Driver Code 
if __name__ == '__main__': 
	
	# Calling main() function 
	main() 
