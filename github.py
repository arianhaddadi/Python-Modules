from bs4 import BeautifulSoup
import requests
import webbrowser


class Github:

    def __init__(self, username):
        self.username = username
        self.base_url = f"https://github.com/{username}"
        self.followers = set()
        self.following = set()

    def get_not_following_back(self, open_browser=True):
        self.get_followers()
        self.get_following()

        an_o_goh = []
        for following in self.following:
            if following not in self.followers:
                an_o_goh.append(f"https://github.com/{following}")

        if open_browser:
            for an in an_o_goh:
                webbrowser.open(an)
        else:
            print(an_o_goh)

    def get_users(self, set, tab):
        i = 1
        while True:
            url = f"{self.base_url}?page={i}&tab={tab}"
            users = BeautifulSoup(requests.get(url).text, "lxml").findAll("a", {"data-hovercard-type": "user"})
            if len(users) == 0:  # No More Pages of Following/Followers
                break
            for user in users:
                if len(user["class"]) == 3:
                    set.add(user["href"][1:])
            i += 1

    def get_followers(self):
        if len(self.followers) > 0:
            return
        self.get_users(self.followers, "followers")

    def get_following(self):
        if len(self.following) > 0:
            return
        self.get_users(self.following, "following")

if __name__ == "__main__":
    Github(username="arianhaddadi").get_not_following_back(open_browser=True)
