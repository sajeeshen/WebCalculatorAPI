from django.urls import path
from reports import views


app_name = 'reports'

urlpatterns = [
    path('daily/', views.DailyReportView.as_view(), name='daily'),
    path('monthly/<int:month>/<int:year>',
         views.MonthlyReportView.as_view(), name='monthly'),
    path('yearly/<int:year>', views.YearlyReportView.as_view(), name='yearly'),

]
