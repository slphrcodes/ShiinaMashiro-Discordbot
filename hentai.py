import os, random, requests, io

hentai_categories = {
    "erofeet", "meow", "erok", "poke", "eroyuri", "kiss", "fox_girl", "hug", "gecg", "pat", "smug",
    "kemonomimi", "neko", "gasm", "eron", "erokemo", "hololewd", "lewdk", "keta", "nsfw_neko_gif",
    "tits", "pussy_jpg", "pussy", "lewdkemo", "lewd", "cum", "spank", "Random_hentai_gif", "boobs",
    "solog", "yuri", "anal", "hentai", "solo", "pwankg"
}


class nekos_class:
    def __init__(self, choice, categories):
        if choice.lower() == "random":
            self.choice = random.choice(categories)

        else:
            self.choice = choice

    def get_url(self):
        base_url = f"https://www.nekos.life/api/v2/img/{self.choice}"
        resp = requests.get(base_url)
        url = resp.json()["url"]

        return url

    def show_image(self, url):
        GETimage = requests.get(url)
        image = io.BytesIO(GETimage.content)
        return image
