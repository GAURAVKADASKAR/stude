from home.models import *
from rest_framework import serializers



# Display the data of registration model
class profileserilaizer(serializers.ModelSerializer):
    class Meta:
        model=registration
        fields="__all__"



# Display the profile data
class personalprofileserializer(serializers.ModelSerializer):
    class Meta:
        model=personalProfile
        fields="__all__"
    

    def create(self,data):
        rollNumber=data.get('rollNumber')
        user=registration.objects.filter(username=rollNumber).first()
        

        firstName=data.get('firstName')
        lastName=data.get('lastName')
        mobileNumber=data.get('mobileNumber')
        dateOfBirth=data.get('dateOfBirth')
        telePhone=data.get('telePhone')
        permanentAddress=data.get('permanentAddress')
        presentAddress=data.get('presentAddress')
        maritalStatus=data.get('maritalStatus')
        gender=data.get('gender')

        obj=personalProfile.objects.create(
            username=user,
            firstName=firstName,
            lastName=lastName,
            mobileNumber=mobileNumber,
            dateOfBirth=dateOfBirth,
            telePhone=telePhone,
            permanentAddress=permanentAddress,
            presentAddress=presentAddress,
            maritalStatus=maritalStatus,
            gender=gender
        )
        obj.save()
        return data

# updating the profile
class personalprofileserializerforget(serializers.ModelSerializer):
    class Meta:
        model=personalProfile
        fields="__all__"

    
# Display the list of all branches
class branchesserlializer(serializers.ModelSerializer):
    class Meta:
        model=branches
        fields="__all__"
        
# displaying  the student list of a perticular batch 
class studentlistserializer(serializers.ModelSerializer):

    class Meta:
        model=studentlist
        fields="__all__"

class subjectlistserializer(serializers.ModelSerializer):
    class Meta:
        model=stubjects
        fields="__all__"
    
class marksserializer(serializers.ModelSerializer):
    class Meta:
        model=studentmarkes
        fields="__all__"
    
class messageserializer(serializers.ModelSerializer):
    class Meta:
        model=message_send
        fields="__all__"
        
    


    


        
        
                                                                                                                                                                                        