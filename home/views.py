from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView,api_view
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from django.conf import settings
from home.models import registration
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from home.serializer import *
from datetime import datetime
from datetime import timedelta

class register_user(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        passcode = request.data.get('passcode')
        
        type=request.data.get('type')
        

        if type=="admin":
            departmentId=request.data.get('departmentId')
            if User.objects.filter(username=email).exists():
                return Response({"error": "Email is already taken"}, status=status.HTTP_400_BAD_REQUEST)
             
            user = User.objects.create_user(username=email)
            user.set_password(passcode)
            user.save()
            token, created = Token.objects.get_or_create(user=user)

            registration_instance = registrationforadmin.objects.create(
                type=type,
                username=username,
                email=email,
                departmentId=departmentId,
                token=token.key
            )

            registration_instance.save()
            

        
          

            # subject = "Account Verification for CareConnect"
            # message = f"""
            # Dear User,

            # Thank you for registering with CareConnect.

            # To complete the registration process and ensure the security of your account, please verify your email address by clicking the link below:
            # http://127.0.0.1:8000/login/?token={token.key}

            # If you are unable to click the link above, please copy and paste it into your web browser's address bar.

            # Once your email address has been verified, you will gain full access to our platform and its features.

            # If you did not register with CareConnect, please ignore this email.

            # Thank you for choosing CareConnect. If you have any questions or need further assistance, please don't hesitate to contact us at CareConnect.support@gmail.com.

            # Best regards,
            # CareConnect Team
            # """
            subject= "Verify Your Email for Secret Dashboard Access"

            message=f"""

            Dear {username},

            Welcome to Secret!

            To complete your registration and activate your account, please verify your email address by clicking the link below:
            http://127.0.0.1:8000/login/?token={token.key}

            If the link above doesn’t work, copy and paste it into your browser’s address bar.

            Once verified, you’ll have full access to your student dashboard and all its features.

            If you didn’t sign up for Secret, please disregard this email.

            Thank you for joining Secret! If you have any questions or need assistance, feel free to contact us at kadskargaurav@gmail.com.

            Best regards,
            The Secret Team"""
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)

            return Response({"message": "Registration successful, please check your email for verification."}, status=status.HTTP_201_CREATED)
            


        else:
            rollNumber=request.data.get('rollNumber')
        
            if User.objects.filter(username=rollNumber).exists():
                return Response({"error": "Email is already taken"}, status=status.HTTP_400_BAD_REQUEST)
            
            user = User.objects.create_user(username=rollNumber)
            user.set_password(passcode)
            user.save()
            token, created = Token.objects.get_or_create(user=user)

            registration_instance = registration.objects.create(
                
                username=username,
                email=email,
                rollNumber=rollNumber,
                token=token.key
            )

            registration_instance.save()

            

        
            

            # subject = "Account Verification for CareConnect"
            # message = f"""
            # Dear User,

            # Thank you for registering with CareConnect.

            # To complete the registration process and ensure the security of your account, please verify your email address by clicking the link below:
            # http://127.0.0.1:8000/login/?token={token.key}

            # If you are unable to click the link above, please copy and paste it into your web browser's address bar.

            # Once your email address has been verified, you will gain full access to our platform and its features.

            # If you did not register with CareConnect, please ignore this email.

            # Thank you for choosing CareConnect. If you have any questions or need further assistance, please don't hesitate to contact us at CareConnect.support@gmail.com.

            # Best regards,
            # CareConnect Team
            # """
            subject= "Verify Your Email for Secret Dashboard Access"

            message=f"""

            Dear {username},

            Welcome to Secret!

            To complete your registration and activate your account, please verify your email address by clicking the link below:
            http://127.0.0.1:8000/login/?token={token.key}

            If the link above doesn’t work, copy and paste it into your browser’s address bar.

            Once verified, you’ll have full access to your student dashboard and all its features.

            If you didn’t sign up for Secret, please disregard this email.

            Thank you for joining Secret! If you have any questions or need assistance, feel free to contact us at kadskargaurav@gmail.com.

            Best regards,
            The Secret Team"""
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)

            return Response({"message": "Registration successful, please check your email for verification."}, status=status.HTTP_201_CREATED)




     
        


class login_user(APIView):
    def post(self,request):
        password=request.data.get('passcode')
        email=request.data.get('email')
        rollNumber=request.data.get('rollNumber')
     
        # email="kadskargaurav@gmail.com"
        # password="123456"

        
        if email is None: 
                user=authenticate(username=rollNumber,password=password)
                if user is None:
                    return Response({"status":200,"message":"invalid username or password"})
                else:

                    user1=registration.objects.get(rollNumber=rollNumber).isActive
                
                    if(user1==0):
                        
                        return Response({"status":200,"message":"user is not verified"})
                    else:
                        request.session['username']=rollNumber
                        return Response({"status":200,"message":"login"})
        else:
                user=authenticate(username=email,password=password)
                if user is None:
                    return Response({"status":200,"message":"invalid username or password"})
                else:

                    user1=registrationforadmin.objects.get(email=email).isActive
                
                    if(user1==0):
                        
                        return Response({"status":200,"message":"user is not verified"})
                    else:
                        request.session['username']=email
                        return Response({"status":200,"message":"login"})



@api_view(['GET'])
def verify_user(request):
    token=request.GET.get('token')
    user=registration.objects.filter(token=token).update(isActive=1)
    user1=registrationforadmin.objects.filter(token=token).update(isActive=1)
    if user==1 or user1==1:
        return Response({'status':200,"message":"Verification has been done"})
    return Response({'status':200,"message":"invalid token"})



class forgotpassword(APIView):
    def post(self,request):
        email=request.data.get("email")
        user_queryset = User.objects.filter(username=email)

        if user_queryset.exists():
         
            user=user_queryset.first()
           
            Token.objects.filter(user=user).delete()
            
           
            token = Token.objects.create(user=user)
            
           
            obj1= registration.objects.filter(email=email).update(token=token.key)

            if obj1==1:

                subject= "Verify Your Email for Secret Dashboard Access"

                message=f"""

                Dear {email},

                Welcome to Secret!

                To complete your registration and activate your account, please verify your email address by clicking the link below:
                http://127.0.0.1:8000/reset-password/?token={token.key}

                If the link above doesn’t work, copy and paste it into your browser’s address bar.

                Once verified, you’ll have full access to your student dashboard and all its features.

                If you didn’t sign up for Secret, please disregard this email.

                Thank you for joining Secret! If you have any questions or need assistance, feel free to contact us at kadskargaurav@gmail.com.

                Best regards,
                The Secret Team"""
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail(subject, message, from_email, recipient_list)

                return Response({"status":200,"message":"email is sent"})
            return Response({"status":200,"message":"error in token updation"})
            
        return Response({"status":300,"message":"username not exists"})



@api_view(['GET'])
def reset_password(request):
    token=request.GET.get('token')
    password="12345"
    user=registration.objects.filter(token=token)
    if user.exists():
        user=user.first()
        obj1=User.objects.get(username=user.rollNumber)
        obj1.set_password(password)
        obj1.save()
        return Response({"status":200,"message":"password is successfully reset"})
    return Response({"status":200,"message":"invalid token"})



class profiledata(APIView):
    def get(self,request):
        if request.session.has_key('username'):
            rollNumber=request.session['username']
            user=registration.objects.filter(rollNumber=rollNumber)
            serlialier=profileserilaizer(user,many=True)
         
            return Response({"status":200,"message":serlialier.data})
        else:
            return Response({"status":200,"message":"user is not login"})
    

class update_peronalprofile(APIView):

    def post(self,request):
        serializer=personalprofileserializer(data=request.data)
        if not serializer.is_valid():
            return Response({"status":404,"message":serializer.errors})
        serializer.save()
        return Response({"status":200,"message":"data is inserted successfully"})
    

    def get(self,request):
        if request.session.has_key('username'):
            rollNumber=request.session['username']
         
           
            data=personalProfile.objects.get(username=rollNumber)
            serializer=personalprofileserializerforget(data,many=True)
            return Response({"status":200,"message":serializer.data})


class get_branches(APIView):
    def get(self,request):
        if request.session.has_key('username'):
            email=request.session['username']
            obj=registrationforadmin.objects.get(email=email)
            if not obj is None:
                    data=branches.objects.filter(departmentId=obj.departmentId)
                    serializer=branchesserlializer(data,many=True)
                    return Response({"status":200,"message":serializer.data})
            else:
                return Response({'status':44,'message':email})
        else:
            return Response({'status':404,'message':'user not login'})
    
@api_view(['GET'])

def studentListformarks(request):
    branchId=request.GET.get('branchId')
    DepartmentID=request.GET.get('DepartmentId')
    data=studentlist.objects.filter(branchId=branchId)
    subjectdata=stubjects.objects.filter(departmentId=DepartmentID)
    serializer=studentlistserializer(data,many=True)
    serializerforsubjects=subjectlistserializer(subjectdata,many=True)
    return Response({'status':200,'studentinfo':serializer.data,'subjectinfo':serializerforsubjects.data})


class enterstudetnmarks(APIView):

    def post(self,request):
        serializer=marksserializer(data=request.data)
        if not serializer.is_valid():
            return Response({"status":404,"message":serializer.errors})
        serializer.save()
        return Response({"status":200,"message":"data is successfully inserted"})
    

class Dispalymarks(APIView):
    def get(self,request):
        if request.session.has_key('username'):
            rollNumber=request.session['username']
            data=studentmarkes.objects.filter(rollNumber=rollNumber)
            serializer=marksserializer(data,many=True)

            return Response({"status":200,"message":serializer.data})
        else:
            return Response({"status":404,"message":"user not login"})
        



from datetime import datetime, timedelta


def get_attendance_percentage(student, start_date, end_date):
    total_days = Attendance.objects.filter(
        student=student,
        date__range=(start_date, end_date)
    ).count()

    present_days = Attendance.objects.filter(
        student=student,
        present=True,
        date__range=(start_date, end_date)
    ).count()

    if total_days == 0:
        return 0

    return (present_days / total_days) * 100

class get_attendance(APIView):
    def get(self, request):
        if request.session.has_key('username'):
            student = request.session['username']
            

            

            today = datetime.today().date()

            # Daily Attendance
            daily_percentage = get_attendance_percentage(student, today, today)

            # Weekly Attendance
            start_of_week = today - timedelta(days=today.weekday())
            weekly_percentage = get_attendance_percentage(student, start_of_week, today)

            # Monthly Attendance
            start_of_month = today.replace(day=1)
            monthly_percentage = get_attendance_percentage(student, start_of_month, today)

            # Custom Date Range Attendance
            # Assuming custom start and end dates are passed as query parameters (YYYY-MM-DD)
            custom_start_date_str = request.query_params.get('start_date')
            custom_end_date_str = request.query_params.get('end_date')

            if custom_start_date_str and custom_end_date_str:
                try:
                    custom_start_date = datetime.strptime(custom_start_date_str, '%Y-%m-%d').date()
                    custom_end_date = datetime.strptime(custom_end_date_str, '%Y-%m-%d').date()
                    custom_percentage = get_attendance_percentage(student, custom_start_date, custom_end_date)
                except ValueError:
                    return Response({"status": 400, "message": "Invalid date format. Use YYYY-MM-DD."})
            else:
                custom_percentage = None

            return Response({
                "daily": daily_percentage,
                'weekly': weekly_percentage,
                'monthly': monthly_percentage,
                'custom': custom_percentage
            })
        else:
            return Response({"status": 404, "message": "User not logged in"})
    
class send_message(APIView):
    def post(self,request):
        serializer=messageserializer(data=request.data)
        if not serializer.is_valid():
            return Response({"status":404,"message":serializer.errors})
        serializer.save()
        return Response({"status":200,"message":"Message has been successfully sent"})
    
class receiver_message(APIView):

    def get(self,request):
        if request.session.has_key('username'):
            email=request.session['username']
            user=message_send.objects.filter(sender=email)
            serializer=messageserializer(user,many=True)
            return Response({'status':200,'message':serializer.data})
        return Response({'status':404,'message':'login required'})


class send_pdf(APIView):

    def post(self,request):
        title=request.data.get('message')
        sender=request.data.get('sender')
        receiver=request.data.get('receiver')
        serializer=pdfserializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':404,'message':serializer.errors})
        data=serializer.save()
        id=data.id
        user=messageviewstatus.objects.create(
            sender=sender,
            message_id=id,
            receiver=receiver
        )
        user.save()
        return Response({'status':200,'message':'Message is successfully sent'})

class receiver_message_pdf(APIView):

    def get(self,request):
        if request.session.has_key('username'):
            email=request.session['username']
            email="0832AD211015"
            Bid=studentlist.objects.get(rollNumber=email).branchId          
            user=sendpdf.objects.filter(receiver_branch_id=Bid)
            serializer=pdfserializer(user,many=True)
            pdf_ids = [pdf['id'] for pdf in serializer.data]
            return Response({'status':200,'message':serializer.data})
        return Response({'status':404,'message':'login required'})

class displayavailablebooks(APIView):
    def get(self,request):
        data=newbook.objects.all()
        serializer=bookserilaizer(data,many=True)
        return Response({'status':200,'message':serializer.data})


