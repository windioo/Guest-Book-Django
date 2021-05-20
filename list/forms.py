from django import forms

class PostForm(forms.Form):
    nama = forms.CharField(
        widget = forms.TextInput(attrs={'placeholder':'Masukkan Nama','class':'form-control border border-dark col-6','style':'margin:20px'}))
    
    email = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Masukkan Email','class':'form-control border border-dark','style':'margin:20px'}))
    alamat = forms.CharField(
        widget = forms.Textarea(attrs={'placeholder':'Masukkan Alamat','class':'form-control border border-dark','style':'margin:20px'})
    )

    # nama = forms.CharField(max_length=20)
    # email = forms.CharField(max_length=20)
    # alamat = forms.CharField(
    #     widget = forms.Textarea
    # )