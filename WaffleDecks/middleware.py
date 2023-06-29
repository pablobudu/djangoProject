from WaffleDecks.models import Carrito, Usuario


# class CarritoMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # Obtiene o crea el usuario
#         usuario, _ = Usuario.objects.get_or_create(
#             username='testuser',
#             # Asigna un valor válido para comuna_id
#             defaults={'comuna_id': 1, 'region_id': 2}
#         )

#         # Obtiene o crea el carrito del usuario
#         carrito, _ = Carrito.objects.get_or_create(usuario=usuario)

#         # Agrega el carrito al contexto de la solicitud
#         request.carrito = carrito

#         response = self.get_response(request)
#         return response
