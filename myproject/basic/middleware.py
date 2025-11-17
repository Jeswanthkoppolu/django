from django.http import JsonResponse


class basicMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self, request):
        # print(request,'hi')
        if(request.path=='/add'):
            print(request.method,'method')
            print(request.path)
        response=self.get_response(request)
        return response
    

class SscMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if(request.path in ["/job1/","/job2/"]):
            ssc_result=request.GET.get("ssc")
            if( ssc_result !="True"):
                return JsonResponse({"erroe":"you should qualify atleast scc for applying this job "},status=400)
        return self.get_response(request)

class MedicalMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if(request.path=="/job1/"):
            medical_fit_result=request.GET.get("medical_fit")
            if( medical_fit_result != "True"):
                return JsonResponse({"erroe":"you not medically fit to aply for this job"},status=400)
        return self.get_response(request)

class AgeMiddlewarepass:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if(request.path in["/job1/","/job2/"]):
            Age_checker=int(request.GET.get("age",17))
            if not (18 <= Age_checker <= 25):
                return JsonResponse({"error":"age must be in b/w 18 to 25"},status=400)
        return self.get_response(request)
    