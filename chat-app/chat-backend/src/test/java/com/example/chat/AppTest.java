import static org.junit.jupiter.api.Assertions.assertNotNull;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.RegisterExtension;

import com.example.chat.ChatApplication;
import com.example.chat.ChatConfiguration;

import io.dropwizard.testing.junit5.DropwizardAppExtension;
public class AppTest {

    @RegisterExtension
    public static final DropwizardAppExtension<ChatConfiguration> APP =
            new DropwizardAppExtension<>(ChatApplication.class, "chat-app/chat-backend/src/main/java/com/example/chat/resources/config.yml");

    @Test
    public void testAppStartsSuccessfully() {
        // Verify that the application context is not null
        assertNotNull(APP.getApplication(), "The application should start and not be null");
    }

    @Test
    public void testConfigurationLoads() {
        // Verify that the configuration is loaded successfully
        ChatConfiguration config = APP.getConfiguration();
        assertNotNull(config, "Configuration should not be null");
    }
}
