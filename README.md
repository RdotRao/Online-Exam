Django Online Examination Project
===============
Project Created By,
 

Name |
-----|
Raj Rao
Kashish Gandhi
Harsh N Patel  
Harsh S Patel
					
<b>Requirements</b>
------------
django-model-utils

Pillow


<b>Installation</b>
------------
1) Install virtualEvn using pip install virtualenv
2) Make virtualEvn using virtualenv <name>
3) Download oequiz.zip and unzip it.
4) Use `pip install -r requirement.txt` to install necessary package for requirement.txt
5) Go to your CMD and run `django-admin startproject Online Exam` .
6) Add `'quiz', 'multichoice', 'true_false', 'essay'` to your `INSTALLED_APPS`  in `setting.py` File.

    INSTALLED_APPS = (
        ...
        'quiz',
        'multichoice',
        'true_false',
		'essay',
        ...
    )

7) Add the following to your projects `urls.py` file, substituting `q` for whatever you want the quiz base url to be.

    urlpatterns = patterns('',
        ...
        url(r'^q/', include('quiz.urls')),
    	...
    )



