
# import the necessary packages
import argparse
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True,
	help="name of the user")
args = vars(ap.parse_args())
 
# display a friendly message to the user
print("Hi there {}, it's nice to meet you!".format(args["name"]))

# Sometimes on this blog, my command line argument flags have a ‘-‘ (dash) in them
# such as --features-db. It’s a little bit confusing and a bit of a nuissance that 
# when grabbing the value contained by the argument, you need to use a ‘_’ (underscore).