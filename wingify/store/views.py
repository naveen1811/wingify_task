from django.shortcuts import render

# Create your views here.
from rest_framework import status, authentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from store.models import Products, OnlineStore
from store.serializers import ProductsSerializer

'''All the CRUD operation are done on store'''

@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes((IsAuthenticated,))
def get_product(request):
    '''

    :param request: request contains the method
    :param q: query search string
    :return: if success return serialized data else response with status code
    '''
    try:
        if request.method == 'GET':
            q = request.GET.get('q')     #q is query string encoded in url
            query = Products.objects.filter(name__icontains = q, store_id__user = request.user, is_active = True)
            serialized_data = ProductsSerializer(query, many=True)    #serializing the query data
            return Response(serialized_data.data)
        else:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    except Exception as e:
        print(e)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes((IsAuthenticated,))
def add_product(request):
    '''

    :param request: get post data in request
    :return: response having status code
    '''

    try:
        if request.method == 'POST':
            name = request.data['name']
            sku_id = request.data['sku_id']
            quantity = request.data['quantity']
            price = request.data['price']
            store = OnlineStore.objects.get(user = request.user)
            Products.objects.create(name = name, sku_id  = sku_id, quantity = quantity, price = price,
                                    store_id = store)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes((IsAuthenticated,))
def edit_product(request, id):


    '''
    Edit Product using PUT i have searched for that product having that id and then update their values
    '''

    if request.method == 'PUT':
        try:
            Products.objects.filter(id = id).update(name = request.data['name'],
                                                                        sku_id = request.data['sku_id'],
                                                                        quantity = request.data['quantity'],
                                                                        price = request.data['price'])
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes((IsAuthenticated,))
def delete_product(request):


    '''
    Delete Products using DELETE we are not physically delete anything so that we will make is_active false
    '''

    if request.method == 'DELETE':
        try:
            id = request.data['id']
            Products.objects.filter(id = id).update(is_active = False)

            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)





