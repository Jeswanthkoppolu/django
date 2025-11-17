from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse 
from django.db import connection
import json
from django.views.decorators.csrf import csrf_exempt
from basic.models import newstudent
# Create your views here.

def sample(request):
    return HttpResponse('hello world')

def sample1(request):
    return HttpResponse('welcome to django')

def sampleInfo(request):
    # data={'name':'bobby','age':23,'city':'nellore'}
    # return JsonResponse(data)
    data=[4,5,6,7] 
    return JsonResponse(data,safe=False)  ## for list type of data we need to use 

def dynamicresponse(request):
    name=request.GET.get('name','bobby')
    city=request.GET.get('city','nellore')
    return HttpResponse(f'hello{name} from {city}')

#to test database connection 
def health(request):
    try:
        with connection.cursor() as c:
            c.execute("select 1")
        return JsonResponse({'status':'ok','db':'connected'})
    except Exception as e:
        return JsonResponse({'status':'error','db':str(e)})

# @csrf_exempt
# def addstudent(request):
#     if request.method =="POST":
#         data=json.loads(request.body)
#         student=newstudent.objects.create(
#             name=data.get("name"),
#             age=data.get("age"),
#             email=data.get("email")
#         )
#         return JsonResponse({"status":"success","id":student.id},status=200)
    
#     elif request.method=="GET":
#         result=list(newstudent.objects.values())
#         print(result)
#         return JsonResponse({'status':'ok','students': result},status=200)
    
#     elif request.method=="PUT":
#         data=json.loads(request.body)
#         ref_id=data.get('id')#getting id
#         new_email=data.get('email')#getting email
#         existing_student=newstudent.objects.get(id=ref_id)#fetched the object as per id
#         existing_student.email=new_email #updating with new email
#         existing_student.save()
#         updated_data=newstudent.objects.filter(id=ref_id).values().first()
#         return JsonResponse({'status':'upated successflly','updated_data':updated_data},status=200)
    
#     elif request.method=="DELETE":
#         data=json.loads(request.body)
#         ref_id=data.get("id")#getting id
#         get_deleting_data=newstudent.objects.filter(id=ref_id).values().first()
#         to_be_delete=newstudent.objects.get(id=ref_id)
#         to_be_delete.delete()
#         return JsonResponse({'status':'success','message':'student record deleted','deleted_data':get_deleting_data},status=200)
#     return JsonResponse ({'error':'use post method'},status=400)


@csrf_exempt
def addstudent(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            student = newstudent.objects.create(
                name=data.get("name"),
                age=data.get("age"),
                email=data.get("email")
            )
            return JsonResponse({"status": "success", "id": student.id}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    elif request.method == "GET":
        action = request.GET.get("action")  # e.g., action=all, get_by_id, age_gte_26, etc.

        # Get all students
        if action == "all":
            students = list(newstudent.objects.values())
            return JsonResponse({"status": "ok", "students": students}, status=200)

        # Get a specific student by id
        elif action == "get_by_id":
            student_id = request.GET.get("id")
            student = newstudent.objects.filter(id=student_id).values().first()
            return JsonResponse({"status": "ok", "student": student}, status=200)

        # Filter students with age >= 26
        elif action == "age_gte_26":
            students = list(newstudent.objects.filter(age__gte=26).values())
            return JsonResponse({"status": "ok", "students": students}, status=200)

        # Filter students with age <= 25
        elif action == "age_lte_25":
            students = list(newstudent.objects.filter(age__lte=25).values())
            return JsonResponse({"status": "ok", "students": students}, status=200)

        # Order students by name
        elif action == "order_name":
            students = list(newstudent.objects.all().order_by('name').values())
            return JsonResponse({"status": "ok", "students": students}, status=200)

        # Get unique ages
        elif action == "unique_ages":
            ages = list(newstudent.objects.values_list('age', flat=True).distinct())
            return JsonResponse({"status": "ok", "unique_ages": ages}, status=200)

        # Count total students
        elif action == "count":
            count = newstudent.objects.count()
            return JsonResponse({"status": "ok", "total_students": count}, status=200)
        else:
            return JsonResponse({"error": "Invalid action"}, status=400)

    elif request.method == "PUT":
        try:
            data = json.loads(request.body)
            ref_id = data.get('id')        # getting id
            new_email = data.get('email')  # new email
            existing_student = newstudent.objects.get(id=ref_id)
            existing_student.email = new_email
            existing_student.save()
            updated_data = newstudent.objects.filter(id=ref_id).values().first()
            return JsonResponse({'status': 'updated successfully', 'updated_data': updated_data}, status=200)
        except newstudent.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    elif request.method == "DELETE":
        try:
            data = json.loads(request.body)
            ref_id = data.get("id")  # getting id
            get_deleting_data = newstudent.objects.filter(id=ref_id).values().first()
            if get_deleting_data:
                to_be_delete = newstudent.objects.get(id=ref_id)
                to_be_delete.delete()
                return JsonResponse({'status': 'success', 'message': 'Student record deleted', 'deleted_data': get_deleting_data}, status=200)
            else:
                return JsonResponse({'error': 'Student not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


    else:
        return JsonResponse({'error': 'Use POST, GET, PUT or DELETE method'}, status=400)


@csrf_exempt
def job1(request):
    return JsonResponse({"message":"you have successfully applied for job1"},status=200)

def job2(request):
    return JsonResponse({"message":"you have successfully applied for job2"},status=200)