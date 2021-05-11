# Blurplefier Standalone

A standalone version of the blurplefier part of the Blurplefier bot (from Project Blurple), in order to more easily convert an image to its blurple variant.

## Installation

**Python 3.8+ is required.** It's possible to make a fork that supports a Python version lower than that, but I won't support it.

This package currently isn't under PyPI because I'm not sure how comfortable I am with doing that, especially with this not being fully my code. There is still a way of installing this, however; simply do:

```sh
pip install -U git+https://github.com/Sonic4999/blurplefier-standalone.git
```

## Basic Example
```python
import blurplefier

input_file = open("input.png", "rb")
input_bytes = input_file.read()

extension, blurplefied_bytes = blurplefier.convert_image(input_bytes, "blurplefy")

with open(f"blurplefied_file.{extension}", "wb") as blurplefied_file:
    blurplefied_file.write(blurplefied_bytes)
```


## FAQ (or, well, possibly asked questions)
> Why?

Because I like the Burplefier bot and think its conversion tool is really neat. I believe it'll be of great help with [my Blurplefied Resource Pack for Minecraft](https://github.com/Sonic4999/Blurplefied-Resource-Pack), as I've previously had to use this really obscure program that has been removed from GitHub a while back.

> Why not make your own solution from scratch, then?

Because I don't want to re-invent the wheel. Simple as that.

> Isn't this stealing their code?

Guess you could say it is, but I'm not trying to say this is my own work. Just a modification of theirs. Plus, it's under the MIT license, I can technically do this just fine.
