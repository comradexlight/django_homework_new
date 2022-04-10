from django.urls import path
from .views import ListSensorView, CreateSensorView, ModifySensorView, CreateMeasurementView, SensorView

urlpatterns = [
    path('sensor_list/', ListSensorView.as_view()),
    path('create_sensor/', CreateSensorView.as_view()),
    path('modify_sensor/<pk>', ModifySensorView.as_view()),
    path('create_measurement/', CreateMeasurementView.as_view()),
    path('sensor/<pk>', SensorView.as_view()),

]
