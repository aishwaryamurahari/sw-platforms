from locust import HttpUser, task, between

class BlogUser(HttpUser):
    wait_time = between(1, 2)  # Wait between 1-2 seconds between requests

    @task
    def load_home(self):
        self.client.get("/")

    @task
    def load_posts(self):
        self.client.get("/1")

    @task
    def load_posts_create(self):
        self.client.get("/create")

    @task
    def load_posts_edit(self):
        self.client.get("/1/edit")

    @task
    def load_posts_delete(self):
        self.client.get("/1/delete")
