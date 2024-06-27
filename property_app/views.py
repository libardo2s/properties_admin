import json
import os

from django.conf import settings
from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from property_app.models import Property, PropertyType
from property_app.serializer.property import PropertySerializer
from property_app.serializer.property_type import PropertyTypeSerializer


def property_view(request):
    return render(request, "property_template.html", context={})


@api_view(["GET"])
def get_property_type(request):
    """
    Retrieve all property types.

    This view handles GET requests to fetch all property types from the database.
    It serializes the data and returns it in a structured response.

    Returns:
        Response: A Response object containing a list of serialized property types
                  and a status code indicating the outcome of the operation.
    """
    try:
        type_properties_list = PropertyType.objects.all()
        type_property_serializer = PropertyTypeSerializer(
            type_properties_list, many=True
        )
        return Response(
            {"content": type_property_serializer.data}, status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response(
            {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


class PropertyApiView(APIView):
    """
    PropertyApiView handles the CRUD operations for Property objects.

    Methods:
        get(request, id=None, format=None):
            Retrieves a list of non-deleted properties.
        post(request, format=None):
            Creates a new property.
        put(request, id=None, format=None):
            Updates an existing property.
        delete(request, id=None, format=None):
            Deletes an existing property.
    """

    def get(self, request, id=None, format=None):
        try:

            properties_list = Property.objects.filter(deleted=False).order_by("id")
            properties_serializer = PropertySerializer(properties_list, many=True)

            response = {
                "message": "",
                "content": properties_serializer.data,
            }

            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            response = {
                "message": str(e),
                "content": {},
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, format=None):
        try:
            property_serializer = PropertySerializer(data=request.data)
            if property_serializer.is_valid():
                property_serializer.save()
                response = {
                    "message": "Propiedad registrada correctamente",
                    "content": property_serializer.data,
                }
                return Response(
                    response,
                    status=status.HTTP_201_CREATED,
                )

            response = {
                "message": property_serializer.errors,
                "content": {},
            }
            return Response(
                response,
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as e:
            response = {
                "message": str(e),
                "content": {},
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id=None, format=None):
        try:
            property = Property.objects.get(id=id)
            property_serializer = PropertySerializer(data=request.data)
            if property_serializer.is_valid():
                property_serializer_data = property_serializer.data
                property.name = property_serializer_data.get("name", property.name)
                property.address = property_serializer_data.get(
                    "address", property.address
                )
                property.country = property_serializer_data.get(
                    "country", property.country
                )
                property.city = property_serializer_data.get("city", property.city)
                property.zip_code = property_serializer_data.get(
                    "zip_code", property.zip_code
                )
                property.area = property_serializer_data.get("area", property.area)

                if property_serializer_data.get("type"):
                    type_property = PropertyType.objects.get(
                        id=property_serializer_data.get("type")
                    )
                    property.type = type_property

                property.save()

                property_serializer = PropertySerializer(property, many=False)
                response = {
                    "message": "Propiedad actualizada correctamente",
                    "content": property_serializer.data,
                }

                return Response(response, status=status.HTTP_200_OK)

            response = {
                "message": property_serializer.errors,
                "content": {},
            }
            return Response(
                response,
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Property.DoesNotExist:
            response = {
                "message": "La propiedad no existe",
                "content": {},
            }
            return Response(
                response,
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        except Exception as e:
            response = {
                "message": str(e),
                "content": {},
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, id=None, format=None):
        try:
            property = Property.objects.get(id=id)
            property.deleted = True
            property.save()

            response = {
                "message": "Propiedad eliminada correctamente",
                "content": {},
            }

            return Response(response, status=status.HTTP_200_OK)

        except Property.DoesNotExist:
            response = {
                "message": "La propiedad no existe",
                "content": {},
            }
            return Response(
                response,
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            response = {
                "message": str(e),
                "content": {},
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
