from django.urls import path
from . import views

urlpatterns = [
    path('sticky_notes/', views.sticky_notes_list, name='sticky_notes_list'),
    path('sticky_notes/add/', views.add_edit_sticky_note, name='add_sticky_note'),  # For creating new sticky notes
    path('sticky_notes/<int:note_id>/edit/', views.add_edit_sticky_note, name='edit_sticky_note'),  # For editing sticky notes
    path('sticky_notes/<int:note_id>/delete/', views.delete_sticky_note, name='delete_sticky_note'),
    path('sticky_notes/<int:note_id>/attachments/', views.view_attachments, name='view_attachments'),
    path('sticky_notes/<int:note_id>/add_attachment/', views.add_attachment, name='add_attachment'),
    path('attachments/<int:attachment_id>/delete/', views.delete_attachment, name='delete_attachment'),
    
    path('lecture-notes/', views.lecture_notes_list, name='lecture_notes_list'),
    path('lecture-note/<int:note_id>/', views.lecture_note_detail, name='lecture_note_detail'),
    path('lecture-note/add/', views.add_edit_lecture_note, name='add_lecture_note'),
    path('lecture-note/<int:pk>/edit/', views.add_edit_lecture_note, name='edit_lecture_note'),
    path('lecture-note/<int:pk>/delete/', views.delete_lecture_note, name='delete_lecture_note'),
    path('lecture-note/<int:pk>/attachment/<int:attachment_id>/delete/', views.delete_attachment, name='delete_attachment'),
]
