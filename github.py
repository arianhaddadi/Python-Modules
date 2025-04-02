from bs4 import BeautifulSoup
import requests
import webbrowser
from typing import Set


class Github:
    def __init__(self, username: str) -> None:
        self.base_url = f"https://github.com/{username}"

    def get_not_following_back(self, open_browser: bool = True) -> None:
        """
        Finds users that are not following back. Afterward, if `open_browser`
        is true, it will open a browser tab with the GitHub profile of those
        users, otherwise, it will print their usernames.
        """
        followers = self.get_users("followers")
        followings = self.get_users("following")

        an_o_goh = []
        for following in followings:
            if following not in followers:
                an_o_goh.append(f"https://github.com/{following}")

        if open_browser:
            for an in an_o_goh:
                webbrowser.open(an)
        else:
            print(an_o_goh)

    def get_users(self, tab: str) -> Set[str]:
        """
        Returns a set of usernames of the users from the given `tab` of the
        GitHub profile specified by `self.base_url`.
        """
        users = set()
        page = 1
        while True:
            # Loop through all the available pages
            url = f"{self.base_url}?page={page}&tab={tab}"
            page_users = BeautifulSoup(requests.get(url).text, "lxml").findAll(
                "a", {"data-hovercard-type": "user"}
            )
            if len(page_users) == 0:
                # No more pages are available for this tab
                break
            for user in page_users:
                if len(user["class"]) == 3:
                    users.add(user["href"][1:])
            page += 1
        return users


if __name__ == "__main__":
    Github(username="arianhaddadi").get_not_following_back(open_browser=True)
