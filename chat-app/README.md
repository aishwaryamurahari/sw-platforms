# React and Dropwizard Chat Application

A real-time chat application built using **React** for the frontend and **Dropwizard** for the backend. The application enables multiple users to connect and exchange messages in real-time via WebSockets.

## Table of Contents
- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [Future Improvements](#future-improvements)
- [Troubleshooting](#troubleshooting)

## Features
- Real-time messaging using WebSocket
- Multiple user support
- Clean and responsive UI
- Message broadcasting
- Efficient message handling

## Architecture

### Model (Backend - Dropwizard)
- Handles WebSocket session management
- Manages message routing and broadcasting
- Implements core business logic

### View (Frontend - React)
- Real-time chat interface
- Message display and input components
- WebSocket connection management
- Responsive design

### Controller
- **Backend**: ChatSocket manages WebSocket connections
- **Frontend**: React components handle user interactions

## Prerequisites
- Java JDK 17 or later
- Maven 3.6 or later
- Node.js (Latest LTS version)
- npm (Latest stable version)

## Installation

### Backend Setup
Clone the repository

```bash
git clone <repository-url>
cd chat-app/chat-backend
```

#### Build the project

```bash
mvn clean install
```

### Frontend Setup  

#### Navigate to frontend directory

```bash
cd ../frontend
```

#### Install dependencies

```bash
npm install
```

#### Running the Application
Start Backend Server

```bash
java -jar target/chat-application-1.0-SNAPSHOT.jar server
```

#### The server will start at:
```bash
Application: http://localhost:8080
Admin Console: http://localhost:8081
```

#### Start Frontend Application

```bash
npm start
The application will open at http://localhost:3000
```