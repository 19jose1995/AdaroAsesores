from django.urls import path
from . import views

urlpatterns = [
    path('cargar_excel/', views.cargar_excel, name='cargar_excel'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('movimientos/crear/', views.crear_movimiento, name='crear_movimiento'),
    path('movimientos/historial/', views.historial_movimientos, name='historial_movimientos'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('productos/editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path("productos/etiqueta/<int:producto_id>/", views.generar_etiqueta, name="generar_etiqueta"),
    path("buscar/", views.buscar_producto, name="buscar_producto"),
    path("productos/<int:id>/detalle/", views.detalle_producto, name="detalle_producto"),
    path("conteo/nuevo/", views.crear_conteo, name="crear_conteo"),
    path("conteo/", views.lista_conteos, name="lista_conteos"),
    path("conteo/<int:conteo_id>/", views.detalle_conteo, name="detalle_conteo"),
    path("conteo/<int:conteo_id>/cerrar/", views.cerrar_conteo, name="cerrar_conteo"),
    path("conteo/<int:conteo_id>/ajustar/", views.ajustar_stock_conteo, name="ajustar_stock_conteo"),
    path("conteo/<int:conteo_id>/reporte/", views.generar_reporte_conteo_pdf, name="reporte_conteo_pdf"),
    path("conteo/<int:conteo_id>/ajustar/", views.ajustar_stock_conteo, name="ajustar_stock_conteo"),
    path("plantilla/excel/", views.descargar_plantilla_excel, name="descargar_plantilla_excel"),



]