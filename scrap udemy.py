from selenium import webdriver
import time
path=input("Enter the complete path(without .txt extension) of TxT file containing links of Courses")
driver=webdriver.Chrome()
with open (path, 'r') as myfile:
    data = myfile.read().splitlines()
course=open(r'udemy.txt','w')
n=1
for line in data:
    url=line
    if(url=="end"):
        break
    driver.get(url)
    time.sleep(4)
    headings=driver.find_elements_by_xpath("//*[@id='udemy']/div[1]/div[3]/div[2]/div[3]/div/div/div[4]/div/div[1]/div[1]/h1")
    for heading in headings:
        course.write(heading.text)
    infos1=driver.find_elements_by_xpath("//*[@id='udemy']/div[1]/div[3]/div[2]/div[3]/div/div/div[4]/div/div[1]/div[1]/div")
    course.write("\n\n\n")
    for info1 in infos1:
        course.write(info1.text)
    course.write("\n\n\n")
    rates=driver.find_elements_by_xpath("//*[@id='udemy']/div[1]/div[3]/div[2]/div[3]/div/div/div[4]/div/div[1]/div[2]/div")
    for rate in rates:
        course.write(rate.text)
    course.write("\n\n\n")
    details=driver.find_elements_by_xpath("//*[@id='udemy']/div[1]/div[3]/div[2]/div[4]/div[10]/div/div/div/div/div[1]/div/span")
    for detail in details:
        course.write(detail.text)
    course.write("\n\n\n")
    course.write("click here \n")
    course.write(driver.current_url)
    course.write("\n\n\n")
    course.write("\n\n\n")
    course.write("\n\n\n\n")
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[n])
    n=n+1
    print("done ")
        


course.close()
driver.close()