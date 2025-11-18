from django.db import models


class Pizza(models.Model):
    """A topic the user is learning about."""
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name

class Topping(models.Model):
    """Something specific learned about a topic."""
    Pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'toppings'


    def __str__(self):
        """Return a simple string representing the entry."""
        if len(self.name) < 50:
             return f"{self.name[:50]}"
        else:
             return f"{self.name[:50]} ..."