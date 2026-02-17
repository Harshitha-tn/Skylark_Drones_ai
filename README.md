The Skylark Drone Operations AI Agent is a web-based system designed to automate and assist in managing drone operations. It handles pilot assignments, drone fleet management, mission coordination, conflict detection, and urgent reassignments. The system integrates with Google Sheets for real-time 2-way data synchronization.
This project was developed as a technical assignment to demonstrate AI-based coordination for a fleet of drones and pilots.

Features
1. Pilot Roster Management
Query pilot availability by skills, certifications, and location
View current pilot assignments
Update pilot status (Available / On Leave / Unavailable) with live Google Sheets sync

2. Assignment Tracking
Match pilots to missions based on skill, location, and availability
Match drones to missions based on capabilities and weather conditions
Track active assignments in real-time
Handle urgent reassignments in case of conflicts

3. Drone Fleet Management
Query drones by capabilities, availability, and location
Flag drones under maintenance or unsuitable for mission weather
Update drone status with live Google Sheets sync

4. Conflict Detection
Detect double-booking of pilots or drones
Warn about skill or certification mismatches
Alert for equipment-location mismatches
Weather risk and budget overrun warnings
PROJECT STRUCTURE 
SkylarkDroneAI/
│
├─ app.py   
├─ assignment.py            
├─ conflicts.py              
├─ reassignment.py          
├─ sheets.py                           
└─ README.md               
