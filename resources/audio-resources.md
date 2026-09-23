# 🔊 Free Listening Resources with MP3 (American English)

These are well-known free sites. (I couldn't test them live while building this repo — websites change, so search the name if a link moves.)

| Site | Level | Why it's useful |
|---|---|---|
| **VOA Learning English** (learningenglish.voanews.com) | A1–B1 | Slow American English news and lessons, audio you can download |
| **Randall's ESL Cyber Listening Lab** (esl-lab.com) | A1–B2 | American voices, MP3 + quizzes, easy level available |
| **ELLLO** (elllo.org) | A1–B2 | Free audio interviews, transcripts, many accents |
| **Breaking News English** (breakingnewsenglish.com) | A1–C1 | Same story at several levels with MP3 |
| **LibriVox** (librivox.org) | B1+ | Free audiobooks — later levels |
| **YouTube: Rachel's English** | all | American pronunciation |

## How to practice (15 min/day at A1)
1. Choose the **easiest** level. 2. Listen once **without** text. 3. Listen again and read. 4. Repeat 3 sentences out loud (shadowing). 5. Write 5 new words in Anki.

## Make your own audio from this repo
```
pip install -r tools/requirements.txt
python tools/make_audio.py          # normal speed
python tools/make_audio.py --slow   # slow speed
```
This creates `audio/unit-01.mp3` … from the dialogue scripts (American voice, needs internet).
