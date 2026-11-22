from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class ModalAuthor(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    contact_info = models.EmailField()
    rating = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(5)])

    def __str__(self):
        return self.name

class AIModel(models.Model):
    MODEL_TYPES = [
        ('NLP', 'Natural Language Processing'),
        ('CV', 'Computer Vision'),
        ('RL', 'Reinforcement Learning'),
        ('OTHER', 'Other'),
    ]

    FRAMEWORKS = [
        ('PT', 'PyTorch'),
        ('TF', 'TensorFlow'),
        ('KRS', 'Keras'),
        ('OTHERS', 'Other'),
    ]

    name = models.CharField(max_length=200)
    model_type = models.CharField(max_length=50, choices=MODEL_TYPES)
    description = models.TextField()
    framework = models.CharField(max_length=50, choices=FRAMEWORKS)
    version = models.CharField(max_length=50)
    download_url = models.URLField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    tags = models.JSONField()
    author = models.ForeignKey(ModalAuthor, on_delete=models.CASCADE, related_name='models_uploaded')

    def __str__(self):
        return f"{self.name} - {self.version}"

class ModelPurchase(models.Model):
    user = models.CharField(max_length=200)
    ai_model = models.ForeignKey(AIModel, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    price_paid = models.DecimalField(max_digits=10, decimal_places=2)
    license_key = models.CharField(max_length=100)
    download_link = models.URLField()

    def __str__(self):
        return f"{self.user}-{self.ai_model.name}"

class UsageScenario(models.Model):
    ai_model = models.ForeignKey(AIModel, on_delete=models.CASCADE, related_name='usage_scenarios')
    title = models.CharField(max_length=200)
    description = models.TextField()
    code_snippet = models.TextField()
    usage_frequency = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.ai_model.name} - {self.title}"

class ModelBenchmark(models.Model):
    ai_model = models.ForeignKey(AIModel, on_delete=models.CASCADE,related_name='benchmarks')
    metric_name = models.CharField(max_length=100)
    value = models.FloatField()
    benchmark_date = models.DateTimeField(auto_now_add=True)
    hardware_used = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.ai_model.name} - {self.metric_name}:{self.value}"


