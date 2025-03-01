
from global_var import links
def update_git():
    for link in links:
        r = requests.get(link)
        with open(link.split('/')[-1], 'wb') as f:
            f.write(r.content)