import csv
from django.db import models

# School table

class School(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "School"

# Class table

class Class(models.Model):
    class_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Class"

# AssessmentArea table 
class AssessmentArea(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "AssessmentArea"

# Student table 
class Student(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Student"

# Answers table
class Answers(models.Model):
    answer = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Answer"

# Award table
class Awards(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Award"

#Subject table
class Subject(models.Model):
    subject = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Subject"


# Summary table
class Summary(models.Model):
    school_id = models.IntegerField()
    sydney_participant = models.IntegerField()
    sydney_percentile = models.FloatField()
    assessment_area_id = models.IntegerField()
    award_id = models.IntegerField()
    class_id = models.IntegerField()
    correct_answer_percentage_per_class = models.FloatField()
    correct_answer = models.CharField(max_length=100)
    student_id = models.IntegerField()
    participant = models.CharField(max_length=100)
    student_score = models.FloatField()
    subject_id = models.IntegerField()
    category_id = models.IntegerField()
    year_level_name = models.CharField(max_length=100)
    answer_id = models.IntegerField()
    correct_answer_id = models.IntegerField()
