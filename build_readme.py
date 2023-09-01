import feedparser
import json
import pathlib
import re
import os

root = pathlib.Path(__file__).parent.resolve()



TOKEN = os.environ.get("READ_WRITE_TOKEN", "")


def replace_chunk(content, marker, chunk, inline=False):
    """Replace a section of content identified by marker comments.
    
    Parameters:
        content (str): Original content.
        marker (str): Marker identifying the section to replace.
        chunk (str): New content to insert between markers.
        inline (bool): Whether the chunk should be inline or not.
    
    Returns:
        str: Modified content.
    """
    pattern = r"<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->".format(marker, marker)
    r = re.compile(pattern, re.DOTALL)

    if not inline:
        chunk = "\n{}\n".format(chunk)

    replacement = "<!-- {} starts -->{}<!-- {} ends -->".format(marker, chunk, marker)
    
    # Debugging: Count occurrences of the marker
    occurrences = len(r.findall(content))
    print(f"Number of occurrences of marker {marker}: {occurrences}")

    if occurrences == 1:
        # If the marker is found once, replace it
        return r.sub(replacement, content)
    elif occurrences == 0:
        # If the marker is not found, append the chunk at the end
        return content + "\n" + replacement
    else:
        # If multiple markers exist, it's an issue.
        print(f"Multiple markers found for {marker}. Please resolve this manually.")
        return content




def fetch_blog_entries():
    entries = feedparser.parse("https://medium.com/feed/@neverforget-1975")["entries"]
    return [
        {
            "title": entry["title"],
            "url": entry["link"].split("?")[0],
            "published": entry["published"],
        }
        for entry in entries
    ]


if __name__ == "__main__":
    readme = root / "README.md"
    project_releases = root / "releases.md"

    entries = fetch_blog_entries()
    print(entries)
    entries_md = "\n\n".join(
        ["[{title}]({url}) - {published}".format(**entry) for entry in entries]
    )
    readme_contents = readme.open().read()
    rewritten = replace_chunk(readme_contents, "blog", entries_md)
    print(readme_contents)
    readme.open("w").write(rewritten)