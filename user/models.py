from django.db import models

class User(models.Model):
	name = models.CharField(max_length=40)
	last_name = models.CharField(max_length = 40)
	email = models.EmailField(unique=True)
	number_phone = models.CharField(max_length = 15, unique = True)
	psswd = models.CharField(max_length = 20)
	verified = models.BooleanField(default= False)

	def Validate_Login(self,email,psswd):
		try:
			user = User.objects.get(email=email,psswd=psswd)
		except User.DoesNotExist:
			user = None
		result = False
		if user is not None:
			result = True
		return result

	def Register_User(self,data):
		result = False
		if not self.Validate_Login(data['email'],data['psswd']):
			try:
				User(
					name = data['name'],
					last_name = data['last_name'],
					email = data['email'],
					number_phone = data['number_phone'],
					psswd = data['psswd']
				).save()
				result = True
			except Exception as e:
				result = False
		return result


		
		



