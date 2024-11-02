// package com.example.chat;

// import io.dropwizard.core.Application;
// import io.dropwizard.core.setup.Environment;
// import org.glassfish.jersey.server.ResourceConfig;
// import org.glassfish.jersey.servlet.ServletContainer;

// public class ChatApplication extends Application<ChatConfiguration> {
//     public static void main(String[] args) throws Exception {
//         new ChatApplication().run(args);
//     }

//     @Override
//     public void run(ChatConfiguration configuration, Environment environment) {
//         environment.getApplicationContext()
//                   .getServletContext()
//                   .addServlet("chat", new ServletContainer(
//                       new ResourceConfig().register(ChatSocket.class)
//                   ));
//     }
// }

// package com.example.chat;

// import io.dropwizard.core.Application;
// import io.dropwizard.core.setup.Environment;
// import org.glassfish.jersey.server.ResourceConfig;
// import org.glassfish.jersey.servlet.ServletContainer;

// public class ChatApplication extends Application<ChatConfiguration> {
//     @Override
//     public void run(ChatConfiguration configuration, Environment environment) {
//         ResourceConfig config = new ResourceConfig();
//         config.register(ChatSocket.class);
//         ServletContainer servlet = new ServletContainer(config);
//         environment.getApplicationContext()
//                   .getServletContext()
//                   .addServlet("chat", servlet)
//                   .addMapping("/chat/*");
//     }

//     public static void main(String[] args) throws Exception {
//         new ChatApplication().run(args);
//     }
// }


package com.example.chat;

import org.eclipse.jetty.server.Server;
import org.eclipse.jetty.servlet.ServletContextHandler;
import org.eclipse.jetty.websocket.jakarta.server.config.JakartaWebSocketServletContainerInitializer;

import com.example.chat.resources.ChatSocket;

import io.dropwizard.core.Application;
import io.dropwizard.core.setup.Environment;

public class ChatApplication extends Application<ChatConfiguration> {
    @Override
    public void run(ChatConfiguration configuration, Environment environment) {
        Server server = environment.getApplicationContext().getServer();
        ServletContextHandler context = environment.getApplicationContext();
        
        // Configure WebSocket
        JakartaWebSocketServletContainerInitializer.configure(context, (servletContext, wsContainer) -> {
            wsContainer.addEndpoint(ChatSocket.class);
        });
    }

    public static void main(String[] args) throws Exception {
        new ChatApplication().run(args);
    }
}