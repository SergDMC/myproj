from django import forms

class SearchForm(forms.Form):
    FIO = forms.CharField(label='ФИО', min_length=4, max_length=100, widget=forms.TextInput(attrs={'size' : '40' }), required=False)
    number = forms.CharField(label='Номер', min_length=2, max_length=80, widget=forms.TextInput(attrs={'size' : '20' }), required=False)
    text = forms.CharField(label='Должность', min_length=11, max_length=50, widget=forms.TextInput(attrs={'size' : '20' }), required=False)

    def is_valid(self):
        
      
        return forms.Form.is_valid(self) and ((self.cleaned_data['FIO'].strip() != '') or (self.cleaned_data['number'].strip() != '') or (self.cleaned_data['text'].strip() != ''))