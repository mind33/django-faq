from django.db import models
from django.db.models.query import QuerySet

class QuestionQuerySet(QuerySet):
    def active(self):
        """
        Return only "active" (i.e. published) questions.
        """
        return self.filter(status__exact=self.model.ACTIVE)

class QuestionManager(models.Manager):
    def get_queryset(self):
        return QuestionQuerySet(self.model)

    def active(self):
        return self.getquery_set().active()
