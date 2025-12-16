# Generator side-quests 🏰 🛡️ ⚔️ 

This is basically my little playground for messing around with Python generators and seeing how far I can push them without my laptop crying. Each file is just a tiny demo or experiment—nothing fancy, just stuff I wanted to try out or remind myself how to do later.

## Setup

I'm using `uv` for quick installs:

```bash
uv add pillow
```

## What's in here

* **memory\_efficient\_file_processing.py** — Playing with line-by-line file reads so I don't slam RAM.
* **lazy\_squares_generator.py** — Seeing how generator expressions stack up against list comps for big ranges.
* **log\_error\_filter_generator.py** — Filtering log lines on the fly.
* **nested\_generator_flattening.py** — Using `yield from` to flatten nests without having a breakdown.
* **lazy\_image_loader.py** — Loading images lazily because they're huge and I'm tired.
* **one\_time\_generator_usage.py** — Quick reminder that generators are one-and-done.
* **generator\_object_printing.py** — What generator objects actually look like and how to poke at them.
* **lazy\_exception\_in_generator.py** — Notes on how exceptions behave during iteration.
* **async\_generator_example.py** — A small async generator thing because why not.

Run any file with:

```bash
python filename.py
```

## Why I'm Doing This

Generators let me work with big chunks of data without melting memory. They just vibe along, producing stuff as needed instead of hoarding everything upfront. Perfect for my sanity—and my RAM.

<br>
