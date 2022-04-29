from rest_framework import serializers

from students.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        if data.get('students') and len(data.get('students')) >= 20 and Course.objects.filter(id=data.get('id'), students__gte=20):
            raise ValueError('максимальное число студентов на курсе – 20')
        return data
