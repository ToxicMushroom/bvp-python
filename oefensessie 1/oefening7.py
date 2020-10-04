grade1 = float(input('Grade /20: '))
grade2 = float(input('Grade /20: '))

grade_sum = grade1 + grade2
result_scale_100 = grade_sum * (5/2)
result_string = "Gradle /100 = " + str(result_scale_100)
print(result_string)
