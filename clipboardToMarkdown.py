#!/usr/bin/env python3

import subprocess

def notify(msg):
    print(msg)

def main():
    import klembord
    import markdownify

    klembord.init()
    # get clipboard content
    targets = ["text/html", "TEXT", "STRING"]
    clipboard = klembord.get(targets)
    try:
        # prefer html, fallback to text or string
        content = next((clipboard[k] for k in clipboard if clipboard[k]))
    except StopIteration:
        notify("No clipboard content found")
        # no content found
        return

    # convert to markdown
    markdown = markdownify.markdownify(content)

    # put into clipboard (using xclip to persist the content after termination)
    subprocess.run(["xclip", "-i", "-selection", "clipboard"], input=markdown.encode())
    notify(f"Copied markdown to the clipboard: {markdown}")

if __name__ == "__main__":
    main()
