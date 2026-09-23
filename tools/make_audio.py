"""Create MP3 files from the dialogue scripts in audio-scripts/.
Usage: python tools/make_audio.py [--slow]
Needs: pip install gTTS (internet required)."""
import pathlib
import sys

from gtts import gTTS

slow = "--slow" in sys.argv
root = pathlib.Path(__file__).resolve().parent.parent
out = root / "audio"
out.mkdir(exist_ok=True)

for script in sorted((root / "audio-scripts").glob("*.txt")):
    target = out / (script.stem + ".mp3")
    with open(target, "wb") as fp:
        for line in script.read_text(encoding="utf-8").splitlines():
            if ":" not in line:
                continue
            text = line.split(":", 1)[1].strip()
            gTTS(text=text, lang="en", tld="com", slow=slow).write_to_fp(fp)
    print("created", target)
