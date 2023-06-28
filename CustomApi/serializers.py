from rest_framework import serializers
from .models import *


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class WorkExperienceSerializer(serializers.ModelSerializer):
    fromDate = serializers.DateField(format='%d-%m-%Y', input_formats=['%d-%m-%Y'])
    toDate = serializers.DateField(format='%d-%m-%Y', input_formats=['%d-%m-%Y'])

    class Meta:
        model = WorkExperience
        fields = '__all__'


class QualificationSerializer(serializers.ModelSerializer):
    fromDate = serializers.DateField(format='%d-%m-%Y', input_formats=['%d-%m-%Y'])
    toDate = serializers.DateField(format='%d-%m-%Y', input_formats=['%d-%m-%Y'])

    class Meta:
        model = Qualification
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    addressDetails = AddressSerializer()
    workExperience = WorkExperienceSerializer(many=True)
    qualifications = QualificationSerializer(many=True)
    projects = ProjectSerializer(many=True)
    photo = serializers.CharField(allow_null=True, allow_blank=True)

    def create(self, validated_data):
        address_data = validated_data.pop('addressDetails')
        work_experience_data = validated_data.pop('workExperience')
        qualifications_data = validated_data.pop('qualifications')
        projects_data = validated_data.pop('projects')
        
        # Generate regid
        last_employee = Employee.objects.order_by('id').last()
        if last_employee:
            last_regid = last_employee.regid
            last_number = int(last_regid[3:])
            new_number = last_number + 1
            new_regid = f"EMP{new_number:03}"
        else:
            new_regid = "EMP001"

        address = Address.objects.create(**address_data)
        work_experience = [WorkExperience.objects.create(**exp_data) for exp_data in work_experience_data]
        qualifications = [Qualification.objects.create(**qual_data) for qual_data in qualifications_data]
        projects = [Project.objects.create(**project_data) for project_data in projects_data]
        
        employee = Employee.objects.create(regid=new_regid, addressDetails=address, **validated_data)
        # employee = Employee.objects.create(addressDetails=address, **validated_data)
        employee.workExperience.set(work_experience)
        employee.qualifications.set(qualifications)
        employee.projects.set(projects)

        return employee

    def update(self, instance, validated_data):
        address_data = validated_data.pop('addressDetails', None)
        work_experience_datas = validated_data.pop('workExperience', [])
        qualifications_data = validated_data.pop('qualifications', [])
        projects_data = validated_data.pop('projects', [])

        if address_data:
            address_serializer = AddressSerializer(instance.addressDetails, data=address_data)
            address_serializer.is_valid(raise_exception=True)
            address_serializer.save()
            
        # Delete existing work_experience_data
        instance.workExperience.all().delete()

        # Create new work_experience
        work_experiences = []
        for work_experience_data in work_experience_datas:
            work_experience = WorkExperience.objects.create(employee=instance, **work_experience_data)
            work_experiences.append(work_experience)

        instance.workExperience.set(work_experiences)
        
        
        # ...............
        
         # Delete existing qualifications
        instance.qualifications.all().delete()

        # Create new qualifications
        qualifications = []
        for qualification_data in qualifications_data:
            qualification = Qualification.objects.create(employee=instance, **qualification_data)
            qualifications.append(qualification)

        instance.qualifications.set(qualifications)
        
        # .............
        
         # Delete existing projects_data
        instance.projects.all().delete()

        # Create new projects
        projects = []
        for project_data in projects_data:
            project = Project.objects.create(employee=instance, **project_data)
            projects.append(project)

        instance.projects.set(projects)
        
        
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.phoneNo = validated_data.get('phoneNo', instance.phoneNo)
        instance.photo = validated_data.get('photo', instance.photo)

        instance.save()
        return instance


    class Meta:
        model = Employee
        # fields = '__all__'
        exclude = ('regid',)
        list_serializer_class = serializers.ListSerializer
