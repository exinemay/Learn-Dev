course = 'Python for Beginners'
len_course = len(course)
#len: đếm số kí tự trong string
up_course = course.upper()
#().upper() để viết hoa toàn bộ
#tương tự với .lower(viết thường toàn bộ)
course_p = 'Python' in course
#"..." in a str nếu "..." có trong str thì giá trị sẽ là True và ngược lại
course_test = course.title()
#.title() sẽ viết hoa toàn bộ chữ cái đầu tiên của các từ trong str

print(len_course)
print(up_course)
print(course_p)

print(course.find('Python'))
#.find() để tìm điểm bắt đầu của một kí tự(chuỗi kí tự) trong str

print(course.replace('Beginners', 'Absolute Beginners'))
#.replace(,) để thay thế kí tự trong str

print(course_test)