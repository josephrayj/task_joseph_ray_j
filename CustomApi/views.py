
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework import status


@api_view(['POST'])
def create_employee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        try:
            employee = serializer.save()
            return Response({
                "message": "Employee created successfully",
                "regid": employee.regid,
                "success": True
            }, status=200)
        except Exception as e:
            return Response({
                "message": "Employee creation failed",
                "success": False
            }, status=500)
    elif "email" in serializer.errors and "unique" in str(serializer.errors["email"]).lower():
        return Response({
            "message": "Employee already exists",
            "success": False
        }, status=200)
    else:
        return Response({
            "message": "Invalid body request",
            "success": False
        }, status=400)



@api_view(['PUT'])
def update_employee(request, regid):
    try:
        # Retrieve the employee from the database
        employee = Employee.objects.get(regid=regid)
        
        # Update the employee's details with the request data
        serializer = EmployeeSerializer(employee, data=request.data)
        
        # Validate and save the updated employee
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Employee details updated successfully", "success": True}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid body request", "success": False}, status=status.HTTP_400_BAD_REQUEST)
        
    except Employee.DoesNotExist:
        return Response({"message": "No employee found with this regid", "success": False}, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({"message": f"Employee updation failed {e}", "success": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['DELETE'])
def delete_employee(request):
    regid = request.data.get('regid')

    # Check if regid is provided
    if not regid:
        return Response({"message": "Invalid body request", "success": False}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Retrieve the employee from the database
        employee = Employee.objects.get(regid=regid)

        # Delete the employee
        employee.delete()

        return Response({"message": "Employee deleted successfully", "success": True}, status=status.HTTP_200_OK)

    except Employee.DoesNotExist:
        return Response({"message": "No employee found with this regid", "success": False}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"message": f"Employee deletion failed: {e}", "success": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET'])
def get_employee(request):
    regid = request.query_params.get('regid', None)
    
    if regid:
        # Single employee request
        try:
            employee = Employee.objects.get(regid=regid)
            serializer = EmployeeSerializer(employee)
            return Response({
                "message": "Employee details found",
                "success": True,
                "employees": [serializer.data]
            }, status=200)
        except Employee.DoesNotExist:
            return Response({
                "message": "Employee details not found",
                "success": False,
                "employees": []
            }, status=200)
    else:
        # All employee request
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response({
            "message": "Employee details found",
            "success": True,
            "employees": serializer.data
        }, status=200)
