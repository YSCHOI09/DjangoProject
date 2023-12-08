# community/views.py
from django.shortcuts import render
from community.forms import Form
from .chatgpt import ChatGPTAssistant
from .rec_ac import *
from .models import *
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
def write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            user_data = form.save(commit=False)
            user_data.save()
            
            chatgpt_assistant = ChatGPTAssistant(api_key='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')
            rec_ac, rec_fd, rec_pd, rec_ta = chatgpt_assistant.result_feedback(user_data.to_input_text())
            body_parts_result = chatgpt_assistant.result_bodyparts(rec_ac)
            body_check_image = chatgpt_assistant.body_check(body_parts_result)
            


            result_feedback = ResultFeedback.objects.create(
                user_data=user_data,
                rec_ac=rec_ac,
                rec_fd=rec_fd,
                rec_pd=rec_pd,
                rec_ta=rec_ta,
                body_parts_result=body_parts_result,
                body_check_image=body_check_image  # Save the filename in the model
            )
            
            return render(request, 'result_feedback.html', {'rec_ac': rec_ac, 'rec_fd': rec_fd, 'rec_pd': rec_pd, 'rec_ta': rec_ta, 'body_parts_result': body_parts_result, 'body_check_image': body_check_image})
    else:
        form = Form()

    return render(request, 'write.html', {'form': form})

def list(request):
    UserDataList = UserData.objects.all()
    return render(request, 'list.html', {'UserDataList': UserDataList})

def view(request, num):
    userdata = UserData.objects.get(id=num)
    return render(request, 'view.html', {'userdata': userdata})