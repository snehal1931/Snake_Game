# 🐍 Snake-Water-Gun Game 🎮

A simple Python implementation of the classic **Snake-Water-Gun** game. Play against the computer and test your luck! This version reads user choices from a file (`choices.txt`), making it easy to simulate multiple games.

---

## 📌 Game Rules

- **Snake (1)** drinks **Water (2)** → Snake wins 🐍💧✅
- **Water (2)** douses **Gun (3)** → Water wins 💧🔫✅
- **Gun (3)** shoots **Snake (1)** → Gun wins 🔫🐍✅
- If both choices are the same → It's a draw ⚔️

---

## 📂 Project Structure

```
├── snake_water_gun.py      # Main game file
├── choices.txt             # File with user input choices (1, 2, or 3)
└── README.md               # Project documentation
```

---

## 📄 choices.txt Format

Each line in `choices.txt` should be a number:
```
1  # Snake
2  # Water
3  # Gun
```

Example:
```
1
2
3
1
```

---

## ▶️ How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/snake-water-gun.git
   cd snake-water-gun
   ```

2. **Add your inputs to `choices.txt`**

3. **Run the game**
   ```bash
   python snake_water_gun.py
   ```

---

## ✅ Features

- Simple terminal-based gameplay
- File-based input for batch simulation
- Clearly explained game results
- Handles invalid inputs in file

---

## 💡 Future Improvements

- Add scoring system
- GUI with `tkinter` or `pygame`
- Multiplayer support

---

## 📜 License

This project is licensed under the MIT License. Feel free to use and modify it.

---

## 👨‍💻 Author

**Your Name**  
GitHub: [@yourusername](https://github.com/yourusername)