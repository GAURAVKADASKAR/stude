from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

marital_status=(("Unmarried","Unmarried"),("Married","Married"))
Gender=(("Male","Male"),("Female","Female"),("Other","Other"))
user_type=(("student","student"),("admin","admin"))
class registration(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    user_id=models.IntegerField
    rollNumber=models.CharField(max_length=100,primary_key=True)
    username=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    isActive=models.IntegerField(default=0)
    token=models.CharField(max_length=100,default=0)
    created_data=models.DateTimeField(auto_now_add=True)
    type=models.CharField(max_length=100,choices=user_type,default="student")

    def __str__(self):
        return self.rollNumber
    




class registrationforadmin(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    username=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    isActive=models.IntegerField(default=0)
    token=models.CharField(max_length=100,default=0)
    created_data=models.DateTimeField(auto_now_add=True)
    type=models.CharField(max_length=100,choices=user_type)
    departmentId=models.CharField(max_length=100)

    def __str__(self):
        return self.username


class personalProfile(models.Model):
    username=models.OneToOneField(registration,on_delete=models.SET_NULL,null=True)
    firstName=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)
    mobileNumber=models.CharField(max_length=100)
    dateOfBirth=models.DateField()
    telePhone=models.CharField(max_length=100)
    permanentAddress=models.TextField()
    presentAddress=models.TextField()
    maritalStatus=models.CharField(max_length=100,choices=marital_status,default="Unmarried")
    gender=models.CharField(max_length=100,choices=Gender)




class Department(models.Model):
    departmentId=models.CharField(primary_key=True,max_length=100)


    def __str__(self):
        return self.departmentId
    

class branches(models.Model):
    departmentId=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True,unique=False)
    branchId=models.CharField(max_length=100,unique=True,primary_key=True)
    bhanchName=models.CharField(max_length=200)
    duration=models.IntegerField()
    startdate=models.DateField()
    enddate=models.DateField(null=True,blank=True)


    def __str__(self):
        return self.branchId
        
    
    def save(self, *args, **kwargs):
       
        if self.duration and self.startdate:
            self.enddate = self.startdate + timedelta(days=365 * self.duration)
        super(branches, self).save(*args, **kwargs)

    


class studentlist(models.Model):
    branchId=models.ForeignKey(branches,on_delete=models.SET_NULL,null=True)
    username=models.CharField(max_length=100)
    rollNumber=models.CharField(max_length=100)
    branchName=models.CharField(max_length=200)



    def __str__(self):
        return self.rollNumber

class stubjects(models.Model):
    departmentId=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)
    subjectCode=models.CharField(max_length=100,primary_key=True)
    stubjectName=models.CharField(max_length=200)


    def __str__(self):
        return self.subjectCode


class studentmarkes(models.Model):
    rollNumber=models.CharField(max_length=100)
    SubjectCode=models.CharField(max_length=100)
    subjectName=models.CharField(max_length=100)
    marks=models.IntegerField(default=0)


    def __str__(self):
        return self.rollNumber
    

class Attendance(models.Model):
    student = models.ForeignKey(registration, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.rollNumber} - {self.date}"

class facultyDetails(models.Model):
    username=models.OneToOneField(registrationforadmin,on_delete=models.SET_NULL,null=True)
    firstName=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)
    mobileNumber=models.CharField(max_length=100)
    dateOfBirth=models.DateField()
    telePhone=models.CharField(max_length=100)
    permanentAddress=models.TextField()
    presentAddress=models.TextField()
    maritalStatus=models.CharField(max_length=100,choices=marital_status,default="Unmarried")
    gender=models.CharField(max_length=100,choices=Gender)


    def __str__(self) -> str:
        return self.username.email
    

class message_send(models.Model):
    sender=models.CharField(max_length=200)
    receiver=models.CharField(max_length=200)
    message=models.TextField()

    def __str__(self):
        return self.sender


class sendpdf(models.Model):
    title=models.CharField(max_length=200)
    message=models.TextField()
    pdf_data=models.FileField(upload_to='pdfs/',default=None,null=True)
    sender=models.TextField()
    receiver_branch_id=models.ForeignKey(branches,on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return self.title

class messageviewstatus(models.Model):
    sender=models.CharField(max_length=200)
    view_status=models.IntegerField(default=0)
    message_id=models.CharField(max_length=200)
    receiver=models.CharField(max_length=200)

    def __str__(self):
        return self.sender  

class newbook(models.Model):
    book_code=models.TextField(max_length=200)
    book_subject=models.TextField(max_length=200)
    book_name=models.TextField(max_length=200)
    auther_name=models.TextField(max_length=200)
    book_pdf=models.FileField(upload_to='books/',default=True,null=True)
    def __str__(self):
        return self.book_code

class bookrequest(models.Model):
    rollnumber=models.CharField(max_length=300)
    branch_id=models.CharField(max_length=300)
    branch_name=models.CharField(max_length=300)
    book_name=models.CharField(max_length=200)
    auther_name=models.CharField(max_length=300)
    Date_for_request=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=200,default="Pending",null=True)
    



    def __str__(self):
        return self.rollnumber

class busdetails(models.Model):
    rollnumber=models.TextField(default='',null=True)
    Bus_number=models.IntegerField()
    college_shift=models.IntegerField()
    Boarding_point=models.TextField()
    Dropping_point=models.TextField()

    
