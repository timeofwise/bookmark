from django.urls import path
from .views import * #BookmarkListView, BookmarkCreateView, BookmarkDetailView #임포트를 모두 하고싶다면 *로

urlpatterns = [
    # http://127.0.0.1/bookmark/???이곳???
    path('', BookmarkListView.as_view(), name='list'), #클래스형 뷰를 보여줄땐 꼭 .as_view() 써야함
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),
]