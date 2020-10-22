from App.ext import models


class User(models.Model):
    id = models.Column(models.Integer, primary_key=True)
    username = models.Column(models.String(16), nullable=False)
    password = models.Column(models.String(50), nullable=False)
