import scrapy
import re
from scrapymodule.clearSpace import clear_space, clear_space_str, clear_space_list
from scrapymodule.items import SchoolItem2
from scrapymodule.getItem import get_item1

class KingsMastersSchoolSpider(scrapy.Spider):
    name = "kingsMasters"
    start_urls = ["https://www.kcl.ac.uk/study/subject-areas/arts-culture-and-media/index.aspx",
"https://www.kcl.ac.uk/study/subject-areas/law/index.aspx",
"https://www.kcl.ac.uk/study/subject-areas/biomedical-and-life-sciences/index.aspx",
"https://www.kcl.ac.uk/study/subject-areas/management/index.aspx",
"https://www.kcl.ac.uk/study/subject-areas/chemistry/index.aspx",
"https://www.kcl.ac.uk/study/subject-areas/mathematics/index.aspx",
"https://www.kcl.ac.uk/study/subject-areas/computer-science/index.aspx",
"https://www.kcl.ac.uk/study/subject-areas/medicine/index.aspx",
"https://www.kcl.ac.uk/study/subject-areas/conflict-and-security/index.aspx",
"https://www.kcl.ac.uk/study/subject-areas/nursing-and-midwifery/index.aspx",
"https://www.kcl.ac.uk/study/subject-areas/dental-training-and-science/index.aspx",
"https://www.kcl.ac.uk/study/subject-areas/pharmacy-pharmacology-and-forensic-science/index.aspx",
"https://www.kcl.ac.uk/study/subject-areas/dentistry/index.aspx",
"https://www.kcl.ac.uk/study/subject-areas/philosophy-and-religion/index.aspx",
"https://www.kcl.ac.uk/study/subject-areas/education-management-and-policy/index.aspx",
"https://www.kcl.ac.uk/study/subject-areas/physics/index.aspx",
"https://www.kcl.ac.uk/study/subject-areas/engineering/index.aspx",
"https://www.kcl.ac.uk/study/subject-areas/policy-and-society/index.aspx",
"https://www.kcl.ac.uk/study/subject-areas/finance/index.aspx",
"https://www.kcl.ac.uk/study/subject-areas/politics-and-economics/index.aspx",
"https://www.kcl.ac.uk/study/subject-areas/geography-and-the-environment/index.aspx",
"https://www.kcl.ac.uk/study/subject-areas/psychiatry-psychology-and-neuroscience/index.aspx",
"https://www.kcl.ac.uk/study/subject-areas/history-and-classics/index.aspx",
"https://www.kcl.ac.uk/study/subject-areas/public-health/index.aspx",
"https://www.kcl.ac.uk/study/subject-areas/imaging-sciences/index.aspx",
"https://www.kcl.ac.uk/study/subject-areas/specialist-training-for-medical-professionals/index.aspx",
"https://www.kcl.ac.uk/study/subject-areas/intercalated/index.aspx",
"https://www.kcl.ac.uk/study/subject-areas/summer-school/index.aspx",
"https://www.kcl.ac.uk/study/subject-areas/international-affairs-and-development/index.aspx",
"https://www.kcl.ac.uk/study/subject-areas/teaching/index.aspx",
"https://www.kcl.ac.uk/study/subject-areas/languages-and-literature/index.aspx",
"https://www.kcl.ac.uk/study/subject-areas/therapeutic-health/index.aspx",]
    count = 0

    def parse(self, response):
        # 筛选研究生的链接
        links = response.xpath("//div[@id='main']/div[@class='contentpage-main-content']/div[@class='wrapper']/table/tbody/tr/td//a/@href").extract()
        # print(links)
        alllinks = []
        for link in links:
            strurl = re.findall(r"/study/postgraduate/taught-courses/.*", link)
            alllinks.append(''.join(strurl))
        # print(response.url)
        while '' in alllinks:
            alllinks.remove('')
        # print(alllinks)
        # self.count += 1
        # print(self.count)
        # print("============================================================")
        for link in alllinks:
            url = "https://www.kcl.ac.uk" + link
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item1(SchoolItem2)
        item['country'] = "England"
        item["website"] = "https://www.kcl.ac.uk/"
        item['degree_level'] = '1'
        item['university'] = "King's College London"
        item['create_person'] = 'yangyaxia'
        item['url'] = response.url
        print("===============================")
        print(response.url)
        try:
            # //div[@id='container']/div[@class='hero clearfix']/div[@class='wrapper']/div[@class='inner']/h1
            # 专业、学位类型
            programmeDegree = response.xpath("//div[@id='container']/div[@class='hero clearfix']/div[@class='wrapper']/div[@class='inner']/h1//text()").extract()
            clear_space(programmeDegree)
            programmeDegreeStr = ''.join(programmeDegree)
            # print(programmeDegreeStr) (\s\w+)$|(\s\w+\s\(.*\))$
            degree_type = list(re.findall(r"(\s\w+)$|(\s\w+\s\(.*\))$|(\s\w+/\w+)$|(\s\w+/\w+/\w+)$", programmeDegreeStr)[0])
            while '' in degree_type:
                degree_type.remove('')
            # print("degree_type = ", degree_type)
            item['degree_type'] = ''.join(degree_type)
            programme = programmeDegreeStr.split(''.join(degree_type))
            item['programme'] = programme[0]
            # print("programme = ", programme)
            # print("item['degree_type'] = ", item['degree_type'])
            # print("item['programme'] = ", item['programme'])

            # //div[@id='tabs-key-info']/div[@class='tab tab-1 active-tab']/p[2]/span
            duration = response.xpath("//div[@id='tabs-key-info']/div[@class='tab tab-1']/p[2]/span//text()").extract()
            item['duration'] = ''.join(duration)
            print("item['duration'] = ", item['duration'])

            # //div[@id='tabs-key-info']/div[@class='tab tab-1 active-tab']/p[3]/span
            mode = response.xpath("//div[@id='tabs-key-info']/div[@class='tab tab-1']/p[3]/span//text()").extract()
            item['mode'] = ''.join(mode)
            print("item['mode'] = ", item['mode'])

            # //div[@id='tabs-key-info']/div[@class='tab tab-2']
            includeDepartment = response.xpath("//div[@id='tabs-key-info']/div[@class='tab tab-2']//text()").extract()
            clear_space(includeDepartment)

            item['department'] = ""
            department = ""
            if "Faculty" in includeDepartment:
                facultyIndex = includeDepartment.index("Faculty")
                department += includeDepartment[facultyIndex+2] + ", "
            if "Department" in includeDepartment:
                departmentIndex = includeDepartment.index("Department")
                department += includeDepartment[departmentIndex+1]
            item['department'] = department
            # print("item['department'] = ", item['department'])

            # //div[@id='coursepage-overview']/div[@class='wrapper clearfix']/div[@class='inner left lop-to-truncate']
            overview = response.xpath("//div[@id='coursepage-overview']/div[@class='wrapper clearfix']/div[@class='inner left lop-to-truncate']//text()").extract()
            item['overview'] = ''.join(overview).strip()
            # print("item['overview'] = ", item['overview'])

            # //div[@id='coursepage-course-detail']/div[@class='wrapper clearfix']/div
            modules = response.xpath("//div[@id='coursepage-course-detail']/div[@class='wrapper clearfix']/div//text()").extract()
            item['modules'] = ''.join(modules).strip()
            # print("item['modules'] = ", item['modules'])

            # //div[@id='coursepage-fees-and-funding']/div[@class='wrapper clearfix']/div[@class='inner left lop-to-truncate lopped-off']/ul[1]/li[2]
            tuition_fee = response.xpath("//div[@id='coursepage-fees-and-funding']/div[@class='wrapper clearfix']/div/ul[1]/li[2]//text()").extract()
            # print("tuition_fee = ", tuition_fee)
            item['tuition_fee'] = ''.join(tuition_fee)
            # print("item['tuition_fee'] = ", item['tuition_fee'])

            # //div[@id='coursepage-entry-requirements']/div[@class='wrapper clearfix']/div[@class='inner left lop-to-truncate lopped-off expanded']
            entry_requirements = response.xpath("//div[@id='coursepage-entry-requirements']/div[@class='wrapper clearfix']/div[1]//text()").extract()
            clear_space(entry_requirements)
            # print(entry_requirements)
            item['entry_requirements'] = '\n'.join(entry_requirements).strip()
            # print("item['entry_requirements'] = ", item['entry_requirements'])

            # //div[@id='coursepage-entry-requirements']/div[@class='wrapper clearfix']/div[@class='inner left lop-to-truncate lopped-off expanded']
            # Rntry_requirements = response.xpath("//div[@class='requirements uk clearfix']/div[@class='copy'][1]/table/tbody/tr[1]//text()").extract()
            # clear_space(Rntry_requirements)
            # # print(Rntry_requirements)
            # item['Rntry_requirements'] = ''.join(Rntry_requirements)

            # //div[@id='coursepage-entry-requirements']/div[@class='wrapper clearfix']/div[@class='inner left lop-to-truncate lopped-off expanded']
            average_score = response.xpath("//div[@id='coursepage-entry-requirements']/div[@class='wrapper clearfix']/div[1]/div[@class='requirements uk clearfix']/div[@class='copy'][1]/table/tbody/tr[2]//text()").extract()
            clear_space(average_score)
            # print(average_score)
            item['chinese_requirements'] = ''.join(average_score)
            # print("item['average_score'] = ", item['average_score'])

            item['IELTS'] = ''
            # //div[@id='coursepage-entry-requirements']/div[@class='wrapper clearfix']/div[@class='inner left lop-to-truncate lopped-off expanded']
            IELTS = response.xpath("//div[@id='coursepage-entry-requirements']/div[@class='wrapper clearfix']/div[1]/div[1]/div[@class='copy'][1]/table/tbody/tr[3]/td[1]//text()").extract()
            clear_space(IELTS)
            # print(IELTS)
            item['IELTS'] = ''.join(IELTS)
            # print("item['IELTS'] = ", item['IELTS'])

            item['application_fee'] = ''
            # //div[@id='coursepage-entry-requirements']/div[@class='wrapper clearfix']/div[@class='inner left lop-to-truncate lopped-off expanded']/div[@class='requirements uk clearfix']/div[@class='copy'][2]/p[1]
            application_fee = response.xpath("//div[@id='coursepage-entry-requirements']/div[@class='wrapper clearfix']/div[1]/div[@class='requirements uk clearfix']/div[@class='copy'][2]/p[1]//text()").extract()
            clear_space(application_fee)
            # print(application_fee)
            item['application_fee'] = ''.join(application_fee)
            # print("item['application_fee'] = ", item['application_fee'])

            item['application_documents'] = ''
            # //div[@id='coursepage-entry-requirements']/div[@class='wrapper clearfix']/div[@class='inner left lop-to-truncate lopped-off expanded']/div[@class='requirements uk clearfix']/div[@class='copy'][2]/p[1]
            application_documents = response.xpath("//div[@id='coursepage-entry-requirements']/div[@class='wrapper clearfix']/div[1]/div[@class='requirements uk clearfix']/div[@class='copy'][3]//text()").extract()
            clear_space(application_documents)
            # print(application_documents)
            item['application_documents'] = ''.join(application_documents).strip()
            # print("item['application_documents'] = ", item['application_documents'])

            item['deadline'] = ''
            # //div[@id='coursepage-entry-requirements']/div[@class='wrapper clearfix']/div[@class='inner left lop-to-truncate lopped-off expanded']/div[@class='requirements uk clearfix']/div[@class='copy'][2]/p[1]
            deadline = response.xpath("//div[@id='coursepage-entry-requirements']/div[@class='wrapper clearfix']/div[1]/div[@class='requirements uk clearfix']/div[@class='copy'][4]//text()").extract()
            clear_space(deadline)
            # print(deadline)
            item['deadline'] = ''.join(deadline).strip()
            # print("item['deadline'] = ", item['deadline'])

            # //div[@id='coursepage-career-prospect']/div[@class='wrapper clearfix']/div[@class='inner left lop-to-truncate']
            item['career'] = ''
            career = response.xpath("//div[@id='coursepage-career-prospect']/div[@class='wrapper clearfix']/div[@class='inner left lop-to-truncate']//text()").extract()
            clear_space(career)
            # print(career)
            item['career'] = '\n'.join(career).strip()
            # print("item['career'] = ", item['career'])
            yield item
        except Exception as e:
            with open("kingsMastersSchoolerror.txt", 'a+', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)

