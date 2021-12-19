#You have to install library pip3 install instaloader
import instaloader
ig= instaloader.Instaloader()
dp= input("Enter Insta username: ")
ig.download_profile(dp,profile_pic_only=True)
