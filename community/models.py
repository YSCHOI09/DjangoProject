from django.db import models

class UserData(models.Model):
    height = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    action_lv = models.CharField(max_length=50)
    action_cl = models.CharField(max_length=50)
    action_pp = models.CharField(max_length=50)
    action_tm = models.CharField(max_length=50)
    action_wk = models.CharField(max_length=50)
    action_pc = models.CharField(max_length=50)
    health = models.CharField(max_length=200)
    today_feel=models.CharField(max_length=1000)

    def to_input_text(self):
        return f"""
        <설문지>
        1. 키: {self.height}
        2. 몸무게: {self.weight}
        3. 현재 신체 활동 수준: {self.action_lv}
        4. 운동 선호: {self.action_cl}
        5. 운동 목적: {self.action_pp}
        6. 하루 운동 선호 시간: {self.action_tm}
        7. 일주일 운동 선호 횟수: {self.action_wk}
        8. 운동 장소 선호: {self.action_pc}
        9. 건강 상태: {self.health}
        <오늘의 일기>
        {self.today_feel}
        """

class ResultFeedback(models.Model):
    user_data = models.ForeignKey('UserData', on_delete=models.CASCADE)
    rec_ac = models.TextField(blank=True)
    rec_fd = models.TextField(blank=True)
    rec_pd = models.TextField(blank=True)
    rec_ta = models.TextField(blank=True)
    body_parts_result=models.TextField(blank=True)
    body_check_image = models.ImageField(null=True, blank=True)
        


# class ResultFeedback(models.Model):
#     feedback_ac = models.JSONField(blank=True, null=True)
#     feedback_fd = models.JSONField(blank=True, null=True)
#     feedback_pd = models.TextField(blank=True, null=True)  
#     feedback_ta = models.JSONField(blank=True, null=True)