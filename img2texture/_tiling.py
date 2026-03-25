# SPDX-FileCopyrightText: (c) 2021 Artsiom iG <github.com/rtmigo>
# SPDX-License-Identifier: MIT

from pathlib import Path

from ._common import Image  # importing with tweaked options


def tile(source, target, horizontal = 3, vertical = 3, return_result = False) -> Image:
    """Merges multiple copies of `source` image into the `target` image
    side-by-side."""
    if isinstance(source, Image.Image):
         image = source
    else:
         image = Image.open(source)

    w, h = image.size
    total_width = w * horizontal
    total_height = h * vertical

    new_im = Image.new('RGB', (total_width, total_height))

    for x in range(horizontal):
        for y in range(vertical):
            new_im.paste(image, (w * x, h * y))
    if return_result:
         return new_im
    else:
         new_im.save(target)
