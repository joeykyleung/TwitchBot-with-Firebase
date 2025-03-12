# TwitchBot-with-Firebase

A sophisticated Twitch bot implementation that leverages Firebase Realtime Database to manage automated message scheduling and interactive minigames. This project demonstrates the integration of real-time data synchronization between a web-based control panel and a Twitch chat bot.

## 🚀 Features

- Real-time data synchronization using Firebase Realtime Database
- Interactive minigame system for user engagement
- Configurable message intervals for automated promotions
- Web-based control panel for easy management
- Persistent storage of promotion settings and game scores

## 📸 Screenshots

1. Minigame Interface:  
![Minigame Interface](https://user-images.githubusercontent.com/77413460/218004955-fa0f7a90-5878-4971-919c-054b9b140e3c.png)

2. Firebase Data Updates:  
![Firebase Updates](https://user-images.githubusercontent.com/77413460/218004964-9922bde7-5322-42b4-aa7f-22c3ce1b88e9.png)

3. Twitch Bot in Action:  
![Twitch Bot Promotion](https://user-images.githubusercontent.com/77413460/218005031-b966de38-9ff9-4047-9a1b-8945edbe7d5d.png)

## 🛠️ Technical Stack

- **Frontend**: JavaScript
- **Backend**: Python
- **Database**: Firebase Realtime Database
- **APIs**: Twitch IRC API
- **Real-time Communication**: Firebase WebSocket Connection

## 🔧 Technical Challenges & Solutions

### 1. Real-time Data Synchronization
**Challenge**: Maintaining consistent state between the web control panel and the Twitch bot while allowing for real-time updates.
**Solution**: Implemented Firebase Realtime Database listeners that automatically sync data changes across all connected clients, ensuring the bot always has the most current promotion settings.

### 2. Rate Limiting
**Challenge**: Managing Twitch's rate limiting requirements to prevent bot timeout/ban.
**Solution**: Implemented configurable message intervals and built-in cooldown mechanisms to ensure compliance with Twitch's chat limitations.

### 3. State Management
**Challenge**: Maintaining game state and promotion settings across sessions.
**Solution**: Utilized Firebase's persistent storage capabilities to maintain state even after system restarts or crashes.

## 📋 Setup Instructions

1. **Firebase Configuration**
   - Create a Firebase project
   - Enable Realtime Database
   - Add your Firebase configuration to `Firebase.js`

2. **Twitch Bot Setup**
   - Create a Twitch developer account
   - Register your bot application
   - Configure the following environment variables:
     ```
     TWITCH_TOKEN=your_oauth_token
     TWITCH_CHANNEL=your_channel_name
     ```

3. **Install Dependencies**
   ```bash
   # For Python bot
   pip install -r requirements.txt
   
   # For web interface
   npm install
   ```

4. **Running the Application**
   ```bash
   # Start the web interface
   node Firebase.js
   
   # Start the Twitch bot
   python Bot.py
   ```

## 🎮 Usage

1. Access the web control panel to set up your promotion message and interval
2. Play the minigame to set scores
3. The bot will automatically start promoting in your Twitch channel based on the configured settings