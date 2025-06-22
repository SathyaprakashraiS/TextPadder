Simulates the classic mobile T9 keypad system — encode text to numberpad sequences and decode them back.

---

### ✅ Features
- Encode mode: `"hello"` → `"44 33 555 555 666"`
- Decode mode: `"2 22 222"` → `"a b c"`
- Interactive command-line tool
- Handles letters with spaces
- Fast mapping based on T9 keypad

---

### ⚠️ Known Limitation

If decoding input has no spaces (e.g., `"222"`), it assumes grouped keypresses (`"c"`), but this may conflict with intended interpretation (`"aaa"`).

> 🔧 **Work in progress** to handle this using optional separators like spaces or custom characters.

---

### 🚀 Roadmap

- [ ] Handle ambiguous decoding with user-defined separators (space, `_`, etc.)
- [ ] Add GUI using Tkinter or web UI using Flask/React
- [ ] Support dictionary-assisted smart decoding
- [Done] CLI options for encode/decode modes
- [ ] Save/load messages from files

---

### 📌 Status

**Currently working on separator-based decoding enhancement**.  
This is **Revision 1**, with plans for multiple future versions and UI improvements.
