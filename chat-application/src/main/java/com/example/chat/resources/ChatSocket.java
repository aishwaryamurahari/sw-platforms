// // package com.example.chat.resources;

// // import java.io.IOException;
// // import java.util.Collections;
// // import java.util.Set;
// // import java.util.concurrent.ConcurrentHashMap;

// // import javax.websocket.OnClose;
// // import javax.websocket.OnMessage;
// // import javax.websocket.OnOpen;
// // import javax.websocket.Session;
// // import javax.websocket.server.ServerEndpoint;

// // @ServerEndpoint("/chat")
// // public class ChatSocket {

// //     private static Set<Session> clients = Collections.newSetFromMap(new ConcurrentHashMap<>());

// //     @OnOpen
// //     public void onOpen(Session session) {
// //         clients.add(session);
// //     }

// //     @OnMessage
// //     public void onMessage(String message, Session session) throws IOException {
// //         for (Session client : clients) {
// //             if (client.isOpen()) {
// //                 client.getBasicRemote().sendText(message);
// //             }
// //         }
// //     }

// //     @OnClose
// //     public void onClose(Session session) {
// //         clients.remove(session);
// //     }
// // }





// package com.example.chat.resources;

// import java.io.IOException;
// import java.util.Collections;
// import java.util.Set;
// import java.util.concurrent.ConcurrentHashMap;

// import jakarta.websocket.OnClose;
// import jakarta.websocket.OnMessage;
// import jakarta.websocket.OnOpen;
// import jakarta.websocket.Session;
// import jakarta.websocket.server.ServerEndpoint;

// @ServerEndpoint("/chat")
// public class ChatSocket {

//     private static Set<Session> clients = Collections.newSetFromMap(new ConcurrentHashMap<>());

//     @OnOpen
//     public void onOpen(Session session) {
//         clients.add(session);
//     }

//     @OnMessage
//     public void onMessage(String message, Session session) throws IOException {
//         for (Session client : clients) {
//             if (client.isOpen()) {
//                 client.getBasicRemote().sendText(message);
//             }
//         }
//     }

//     @OnClose
//     public void onClose(Session session) {
//         clients.remove(session);
//     }
// }


package com.example.chat.resources;  // Keep your original package

import java.io.IOException;
import java.util.Collections;
import java.util.Set;
import java.util.concurrent.ConcurrentHashMap;

import jakarta.websocket.OnClose;
import jakarta.websocket.OnError;  // Added this import
import jakarta.websocket.OnMessage;
import jakarta.websocket.OnOpen;
import jakarta.websocket.Session;
import jakarta.websocket.server.ServerEndpoint;

@ServerEndpoint("/chat")
public class ChatSocket {
    private static Set<Session> clients = Collections.newSetFromMap(new ConcurrentHashMap<>());

    @OnOpen
    public void onOpen(Session session) {
        System.out.println("WebSocket opened: " + session.getId());
        clients.add(session);
    }

    @OnMessage
    public void onMessage(String message, Session session) throws IOException {
        System.out.println("Message received: " + message);
        for (Session client : clients) {
            if (client.isOpen()) {
                try {
                    client.getBasicRemote().sendText(message);
                } catch (IOException e) {
                    System.err.println("Error sending message to client: " + e.getMessage());
                }
            }
        }
    }

    @OnClose
    public void onClose(Session session) {
        System.out.println("WebSocket closed: " + session.getId());
        clients.remove(session);
    }

    @OnError
    public void onError(Session session, Throwable throwable) {
        System.err.println("WebSocket error for session " + session.getId() + ": " + throwable.getMessage());
        clients.remove(session);
    }
}