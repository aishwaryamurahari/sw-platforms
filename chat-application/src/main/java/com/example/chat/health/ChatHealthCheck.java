import com.codahale.metrics.health.HealthCheck;

public class ChatHealthCheck extends HealthCheck {
    @Override
    protected Result check() {
        return Result.healthy();
    }
}
