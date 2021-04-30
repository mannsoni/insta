from instaloader import *
dp = input("Enter Insagram Username: ")
ig = instaloader.Instaloader()
ig.download_profile(dp, profile_pic_only = True)
