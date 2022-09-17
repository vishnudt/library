from urllib import response
from django.shortcuts import render
from rest_framework import generics
from.models import *
from.serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework . response import Response

# Create your views here.


class CreateBook(generics.CreateAPIView):
    permission_classes = (IsAdminUser,)

    serializer_class = BookSerializer

class ListBook(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class SingleBook(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class UpdateBook(generics.UpdateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class DeleteBook(generics.DestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Book.objects.all()




class CreateStudent(generics.CreateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer

class ListStudent(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_admin = False)

class SingleStudent(generics.RetrieveAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_admin = False)

class UpdateStudent(generics.UpdateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_admin = False)

class DeleteStudent(generics.DestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = User.objects.filter(is_admin = False)


class CartCreate(generics.CreateAPIView):

    permission_classes = (IsAdminUser,)

    def create(self, request, *args, **kwargs):

        serializer = CartSerializer(data=request.data)
        print(serializer)
        try:
            book = Book.objects.get(id = request.data.get('book'))
            required_qty = request.data.get('qty')

            if not book.is_available:
                return Response('This book is Out of stock')
            if required_qty>book.qty:
                return Response('limited stock available!',book.qty)

            elif serializer.is_valid():
                book.qty-=required_qty
                book.save()
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except:
            return Response('book unavailable')

class CartList(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = CartSerializer
    queryset = Cart.objects.all()