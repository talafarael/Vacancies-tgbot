#### Project Plan: Telegram Bot for Job Vacancy Tracking  

#### 1. Project Description  

This project involves creating a **Telegram bot** that automatically scrapes job listings from popular platforms like **DOU** and **Djinni** and notifies users about new job postings that match their criteria. The bot helps IT professionals find relevant job opportunities faster without manually checking job boards.  

The core idea is to make the job search process as convenient, automated, and efficient as possible. Users specify their search preferences (**programming language, experience level, city, job type, etc.**), and the bot periodically scans job boards, finds new vacancies, and sends relevant updates via **Telegram**.  

#### 2. Features  

✅ **User registration via Telegram** – The bot supports authentication via Telegram, allowing each user to configure personal filters.  
✅ **Flexible search settings** – Users select **programming language, experience level, city, job type (onsite/remote/hybrid), salary range, etc.**  
✅ **Job scraping** – The bot periodically checks **DOU** and **Djinni**, extracts new job listings, and filters them based on user preferences.  
✅ **User data storage** – All search filter settings are stored in **MongoDB**.  
✅ **Automated notifications** – When new job listings matching the user's criteria appear, the bot sends them via private messages.  
✅ **Filter management** – Users can modify or disable notifications anytime.  
✅ **Logging and error handling** – The bot should operate stably, log all requests, and handle errors correctly (e.g., if a job board changes its HTML structure).  

#### 3. Tech Stack  

✅ **Programming Language**: Python 🐍  
✅ **Web Scraping**: `BeautifulSoup`, `requests`, `lxml`  
✅ **Database**: MongoDB (`motor` for async operations)  
✅ **Telegram API**: `telethon` or `pyrogram`  
✅ **Task Scheduling**: `apscheduler` (to run the scraper periodically)  
✅ **Deployment**: **Docker** + **VPS (DigitalOcean, Linode, AWS)**  
✅ **Logging**: `loguru` (for monitoring bot performance)  

#### 4. Workflow  

1️⃣ The user starts the bot with **/start**, and the bot welcomes them, offering search filter configuration.  
2️⃣ The user enters job search criteria (e.g., "Python, 2 years experience, remote work").  
3️⃣ These settings are stored in the database.  
4️⃣ The bot periodically (**e.g., every 30 minutes**) checks **DOU and Djinni** for new job postings.  
5️⃣ If matching job listings are found, the bot sends them to the user.  
6️⃣ The user can modify or delete filters via the **/settings** command.  

#### 5. Future Enhancements  

🔹 **Support for additional job platforms** – LinkedIn, Indeed, Work.ua, etc.  
🔹 **Salary-based filtering** (Djinni often includes salary details).  
🔹 **Web panel** for managing user settings.  
🔹 **Integration with ChatGPT for job description analysis** (automatic job requirement analysis).  

This project has great potential and can become a valuable assistant for IT job seekers! 🚀 Vacancies-tgbot

