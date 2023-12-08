import matplotlib.pyplot as plt
import csv

def reset_data():
    csv_file_path = '..//BARD_API1//BMI//bmi_records.csv'

    # 데이터 초기화: 빈 파일로 덮어쓰기
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
        pass  # 아무 내용도 쓰지 않음

    print(f'데이터가 초기화되었습니다.')
def bmishow():
    csv_file_path = '../BARD_API1/BMI/bmi_records.csv'
    bmi_values = []
    day_values = []
    weight_values = []

    with open(csv_file_path, mode='r',encoding='utf=8') as csv_file:
        reader = csv.reader(csv_file)

        bmi_index = 3
        weight_index = 2
        day_index = 0

        for i, row in enumerate(reader):
            day_values.append(row[day_index])
            bmi_values.append(float(row[bmi_index]))
            weight_values.append(float(row[weight_index]))

    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False

    plt.plot(day_values, bmi_values, color='green', marker='o', linestyle='solid')
    plt.title("날짜별 BMI지수")
    plt.xlabel("날짜")
    plt.ylabel("BMI")
    plt.yticks(range(0, 101, 5))

    # Adding text labels one unit above each point
    for day, bmi_value in zip(day_values, bmi_values):
        plt.text(day, bmi_value, f'{bmi_value:.2f}', ha='left', va='bottom')

    plt.show()