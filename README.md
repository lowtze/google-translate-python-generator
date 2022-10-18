## Why
Inspired by the [Google Translated Pokémon Emerald Romhack](https://simplyblgdev.github.io/Pokemon/GoogleTranslatedEmerald) which I originally discovered in [this thread on Reddit](https://simplyblgdev.github.io/Pokemon/GoogleTranslatedEmerald), I decided to make a tool for evil.

The `csvTrans()` code will take an input.csv containing a single column of text rows and run it through several translations before translating to English (or whatever language with modifications) and saving the original and translated text to two columns in an output.csv when placed in the same directory.

The `transPrompt()` code will do the same but directly in console with a prompt.

## Setup

First install googletrans `pip install googletrans`.

Then download the code.

If you have the issue "googletrans AttributeError: ‘NoneType’ object has no attribute ‘group’", try this version: `pip install googletrans==4.0.0-rc1`
