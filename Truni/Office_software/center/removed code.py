
'''
def Registration_view(request):
    mess = ''
    form = Registration_model()
    if request.method == 'POST':
        data= request.POST

        user = Registration(user_id=data.get('user_id'),password=data.get('password'),first_name=data.get('first_name'),
                            last_name=data.get('last_name'),gender=data.get('gender'), email_id=data.get('gender'),
                            father_name=data.get('father_name'),joining_date=data.get('joining_date'),dob=data.get('dob'),
                            spouse_name=data.get('spouse_name'),current_residency_address=data.get('current_residency_address'),
                            current_zip_code=data.get('current_zip_code'),current_state=data.get('current_state'),
                            current_country=data.get('current_country'),permanent_address=data.get('permanent_address'),
                            permanent_zip_code=data.get('permanent_zip_code'),permanent_state=data.get('permanent_state'),
                            permanent_country=data.get('permanent_country'),personal_contact_no=data.get('personal_contact_no'),
                            emergency_contact_no=data.get('emergency_contact_no'),highest_education=data.get('highest_education'),
                            educational_institute_name=data.get('educational_institute_name'),year_of_passing=data.get('year_of_passing'),
                            previous_employee_name=data.get('previous_employee_name'),previous_empoyee_from=data.get('previous_empoyee_from'),
                            previous_empoyee_to=data.get('previous_empoyee_to'),pan_no=data.get('pan_no'),banke_details_for_salary=
                            data.get('banke_details_for_salary'),active_user=data.get('active_user'),employee_info=data.get('employee_info'),
                            agreeterms=data.get('agreeterms'))
    #pdb.set_trace()
    try:
        if user:
            user.save()
            # to encrypt the password
            msg="user created successfully"
    except Exception as err:
        msg = str(err)
    return render(request,'center/RegistrationForm.html',{'form':form}) #RegistrationForm
    '''
