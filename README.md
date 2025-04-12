# 🎵 Audio Metadata Tools for Game Music Albums

This repository contains two Python scripts for editing and organizing metadata in `.mp3` files. They were designed with video game soundtracks in mind—especially those split into multiple discs or lacking complete metadata.

These tools help ensure your music library (e.g., in iTunes) displays album and track information correctly.
\n
---

## 🧰 Requirements

This script requires the `mutagen` Python library.
\n
---

## 📁 Contents

**Script 1:** `music.py`
Automatically fills in missing Title metadata for `.mp3` files using the filename.

**Script 2:** `itunesMetData.py`
Updates a set of `.mp3` files with consistent album-level metadata, including:

- Album name
- Main and contributing artists
- Disc number
- Grouping/Disc subtitle
\n
---

## 🚀 How to Use

### Prerequisites

1. [Python 3.6+](https://www.python.org/downloads/)
2. Install the required library:

```
pip install mutagen
```
\n
---

### 📝 Script 1 — `music.py`

**Purpose**: Fix missing `title` tags in `.mp3` files.
**Steps**:

1. Place the script (`music.py`) inside the album folder.
2. Run the script:

```
python music.py
```

3. It will:

- Scan the folder.
- Set the `title` tag for each `.mp3` to match its filename (excluding `.mp3`).
- Skip files where the `title` is already set.

**Great for**:

- Albums where files are named (e.g., `01 - The Forest.mp3`) but have no embedded `title` tag.
\n
---

### 🛠️ Script 2 — `itunesMetData.py`

**Purpose**: Apply uniform metadata to an album (or disc) folder.

**Steps**:

1. Open the script in a text editor (e.g., VS Code).
2. Scroll to the bottom and fill in the `album_metadata` dictionary (without the `{ }` blocks):

```
album_metadata = {
    "album_folder_path": r"{Path to album}",
    "album_name": "{album title}",
    "grouping_subtitle": "{Disc x title}",
    "main_artist_name": "{Main Artist}",
    "contri_artist_name": "{Contributing Artist}",
    "disc_number": 1,
    "total_discs": 2
}
```

3. Save the script and run it:

```
python itunesMetData.py
```

4. The script will:

- Set `album`, `artist`, `albumartist`, `grouping`, and `discnumber` tags for each `.mp3` file.
- Print progress to the console.

**Great for**:

- Splitting large soundtracks into multiple labelled discs.
- Ensuring consistent display in iTunes or other music software.
\n
---

## 🧠 Notes

- The `grouping` tag can be used to represent disc subtitles (e.g., "Acoustic Versions").
- Windows Explorer shows `discnumber` under the **"Part of Set"** column, not a column labelled "Disc."
- Use consistent metadata across all discs in a set to ensure correct sorting in music libraries.
\n
---

## 📚 License

MIT License

---
