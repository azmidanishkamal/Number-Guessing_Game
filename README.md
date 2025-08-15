# Number Guessing Game - React App

A beautiful, modern React web application that brings the classic number guessing game to life with stunning UI, animations, and responsive design.

## Features

- **Beautiful UI**: Modern glassmorphism design with gradient backgrounds
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Interactive Feedback**: Real-time feedback on your guesses
- **Game Statistics**: Track attempts and best scores
- **Animations**: Smooth animations and hover effects
- **Local Storage**: Saves your best score between sessions
- **Keyboard Support**: ESC key to close modals

## Getting Started

### Prerequisites

Make sure you have Node.js installed on your system. You can download it from [nodejs.org](https://nodejs.org/).

### Installation

1. **Clone or download the project files** to your local machine

2. **Open a terminal/command prompt** in the project directory

3. **Install dependencies** by running:
   ```bash
   npm install
   ```

### Running the App

1. **Start the development server**:
   ```bash
   npm start
   ```

2. **Open your browser** and navigate to:
   ```
   http://localhost:3000
   ```

3. **Enjoy the game!** 

## How to Play

1. The app will automatically generate a random number between 1 and 100
2. Enter your guess in the input field
3. Click "Guess!" or press Enter
4. Get feedback on whether your guess is too high or too low
5. Keep guessing until you find the correct number!
6. Try to beat your best score

## Available Scripts

- `npm start` - Runs the app in development mode
- `npm build` - Builds the app for production
- `npm test` - Launches the test runner
- `npm eject` - Ejects from Create React App (not recommended)

## Browser Compatibility

- Chrome (recommended)
- Firefox
- Safari
- Edge

## Technologies Used

- **React 18** - Modern React with hooks
- **CSS3** - Custom animations and responsive design
- **HTML5** - Semantic markup
- **JavaScript ES6+** - Modern JavaScript features

## Project Structure

```
src/
├── components/          # React components
│   ├── GameHeader.js   # Game title and subtitle
│   ├── GameBoard.js    # Main game logic and input
│   ├── GameStats.js    # Statistics display
│   └── GameModal.js    # Win celebration modal
├── App.js              # Main app component
├── App.css             # Main app styles
├── index.js            # App entry point
└── index.css           # Global styles
```

##  Troubleshooting

### Port Already in Use
If you get an error about port 3000 being in use:
```bash
# On Windows
netstat -ano | findstr :3000
taskkill /PID <PID> /F

# On Mac/Linux
lsof -ti:3000 | xargs kill -9
```

### Dependencies Issues
If you encounter dependency issues:
```bash
rm -rf node_modules package-lock.json
npm install
```

##  Game Features

- **Random Number Generation**: Uses JavaScript's Math.random() for fair gameplay
- **Input Validation**: Ensures only valid numbers between 1-100 are accepted
- **Score Tracking**: Keeps track of current attempts and best score
- **Responsive Feedback**: Clear visual feedback for each guess
- **Game State Management**: Proper React state management for game flow

##  Future Enhancements

- Sound effects
- Multiple difficulty levels
- Leaderboard system
- Dark/light theme toggle
- Multiplayer support

---

**Happy Guessing!**

If you have any questions or issues, feel free to reach out!

