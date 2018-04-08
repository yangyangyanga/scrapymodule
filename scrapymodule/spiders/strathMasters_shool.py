import scrapy
import re
from scrapymodule.clearSpace import clear_space, clear_space_str
from scrapymodule.items import SchoolItem2
from scrapymodule.getItem import get_item1

class StrathMastersSchoolSpider(scrapy.Spider):
    name = "strathMasters"
    # allowed_domains = ['baidu.com']
    url_start = "https://www.strath.ac.uk"
    start_urls = ['https://www.strath.ac.uk/courses/?delivery=attendance&attendance=full-time&level_ug=false&level_pgr=false']

    def parse(self, response):
        # 获得链接
        # print(response.text)
        contentText = response.text
        # with open("strathhtml.txt", "a+", encoding='utf-8') as f:
        #     f.write(contentText)

        taughtUrl = re.findall(r"/courses/postgraduatetaught/.*/", contentText)
        # print(len(taughtUrl))
        # print(taughtUrl)

        for link in taughtUrl:
            url = "https://www.strath.ac.uk" + link
            yield scrapy.Request(url, callback=self.parse_data, errback=self.error_back)
    def error_back(self, response):
        with open("err.txt", "a+") as f:
            f.write(response.url+"\n==============")
    def parse_data(self, response):
        item = get_item1(SchoolItem2)
        item['country'] = "England"
        item["website"] = "https://www.strath.ac.uk/"
        item['degree_level'] = '1'
        item["university"] = "University of Strathclyde"
        item['create_person'] = "yangyaxia"
        item['url'] = response.url
        print("==========================")
        print(response.url)
        try:
            # 学位类型
            degree_type = response.xpath("//main[@id='content']/section[@class='PGtPage']/header[@class='page-summary has-img']/div[@class='wrap']/h1/span/text()").extract()
            # print("degree_type = ", degree_type)
            item['degree_type'] = ''.join(degree_type)
            # print("item['degree_type'] = ", item['degree_type'])

            # 专业名
            programme = response.xpath(
                "//main[@id='content']/section[@class='PGtPage']/header[@class='page-summary has-img']/div[@class='wrap']/h1/text()").extract()
            # print("programme = ", programme)
            item['programme'] = ''.join(programme)
            # print("item['programme'] = ", item['programme'])

            if "Engineering" in item['programme']:
                item['department'] = "Faculty of Engineering"
            elif "Science" in item['programme']:
                item['department'] = "Faculty of Science"
            elif "Business" in item['programme'] or "Finance" in item['programme'] or "Marketing" in item['programme']:
                item['department'] = "Strathclyde Business School"
            # print("item['department'] = ", item['department'])

            # 课程长度、开学时间、截止日期
            durationStartdateDeadline = response.xpath("//section[@class='related-link-group']//text()").extract()
            clear_space(durationStartdateDeadline)
            # print(durationStartdateDeadline)
            item['start_date'] = ""
            item['duration'] = ""
            if "Study mode and duration" in durationStartdateDeadline:
                durationIndex = durationStartdateDeadline.index("Study mode and duration")
                if "Start date" in durationStartdateDeadline:
                    startDateIndex = durationStartdateDeadline.index('Start date')
                    duration = durationStartdateDeadline[durationIndex+2:startDateIndex]
                    # print(duration)
                    item['duration'] = ''.join(duration)
                    start_date = durationStartdateDeadline[startDateIndex+1]
                    item['start_date'] = ''.join(start_date).strip(":")
            # print("item['start_date'] = ", item['start_date'])
            item['mode'] = item['duration']
            # print("item['duration'] = ", item['duration'])
            durationtmp = re.findall(r"\d+\s\w+", item['duration'])
            # print(durationtmp)
            item['duration'] = ', '.join(durationtmp)
            print("item['duration']1 = ", item['duration'])

            if len(durationtmp) != 0:
                for d in durationtmp:
                    item['mode'] = item['mode'].strip(d)
            print("item['mode']1 = ", item['mode'])

            # 截止日期
            if "Application deadline" in durationStartdateDeadline:
                deadlineIndex = durationStartdateDeadline.index("Application deadline")
                item['deadline'] = durationStartdateDeadline[deadlineIndex+1].strip(":")
            else:
                item['deadline'] = ""
            # print("item['deadline'] = ", item['deadline'])

            # 专业描述
            overview1 = response.xpath("//article[@id='why-this-course']//text()").extract()
            clear_space(overview1)
            overview = '\n'.join(overview1).strip()
            # overview = clear_space_str(overview)
            item['overview'] = overview
            # print("item['overview'] = ", item['overview'])

            # 课程设置、评估方式
            modulesAssessment = response.xpath("//article[@id='course-content']//text()").extract()
            clear_space(modulesAssessment)
            # print(modulesAssessment)
            if "Learning & teaching" in modulesAssessment:
                assessmentIndex = modulesAssessment.index("Learning & teaching")
                item['modules'] = '\n'.join(modulesAssessment[:assessmentIndex-1]).strip()
                item["teaching_assessment"] = '\n'.join(modulesAssessment[assessmentIndex:]).strip()
            else:
                item['modules'] = '\n'.join(modulesAssessment).strip()
                item["teaching_assessment"] = ''
            # print("item['modules'] = ", item['modules'])
            # print("item['teaching_assessment'] = ", item['teaching_assessment'])

            # 学术要求、英语要求
            entryRequirement = response.xpath("//article[@id='entry-requirements']//text()").extract()
            clear_space(entryRequirement)
            # print(entryRequirement)
            item['other'] = '\n'.join(entryRequirement).strip()
            # print("item['other'] = ", item['other'])
            templist = ["English language requirements for international students", "English Language Requirements for International Students",
                        "English language requirements"]
            entryIndex = 0
            for temp in templist:
                if temp in entryRequirement:
                    entryIndex = entryRequirement.index(temp)
            if "Pre-Masters preparation course" in entryRequirement:
                entryIndexEnd = entryRequirement.index("Pre-Masters preparation course")
            else:
                entryIndexEnd = -1
            ielts = entryRequirement[entryIndex:entryIndexEnd]
            item["IELTS"] = ''.join(ielts)
            # print("item['IELTS'] = ", item['IELTS'])
            ielts = re.findall(r"IELTS.{1,130}", item['IELTS'])
            # print(ielts)
            ielts = ''.join(ielts)
            ieltlsrw = re.findall(r"\d\.\d", ielts)
            # print(ieltlsrw)
            if len(ieltlsrw) >= 2:
                item['IELTS'] = ieltlsrw[0]
                item['IELTS_L'] = ieltlsrw[1]
                item['IELTS_S'] = ieltlsrw[1]
                item['IELTS_R'] = ieltlsrw[1]
                item['IELTS_W'] = ieltlsrw[1]
            elif len(ieltlsrw) == 1:
                item['IELTS'] = ieltlsrw[0]
                item['IELTS_L'] = ieltlsrw[0]
                item['IELTS_S'] = ieltlsrw[0]
                item['IELTS_R'] = ieltlsrw[0]
                item['IELTS_W'] = ieltlsrw[0]
            # print("item['IELTS'] = %s item['IELTS_L'] = %s item['IELTS_S'] = %s item['IELTS_R'] = %s item['IELTS_W'] = %s " %(item['IELTS'], item['IELTS_L'], item['IELTS_S'], item['IELTS_R'], item['IELTS_W']))
            if entryIndex == 0:
                if "Pre-Masters preparation course" in entryRequirement:
                    entryIndex = entryRequirement.index("Pre-Masters preparation course")
                else:
                    entryIndex = -1
            Rntry_requirements = entryRequirement[:entryIndex]
            item['entry_requirements'] = '\n'.join(Rntry_requirements).strip()
            # print("item['entry_requirements'] = ", item['entry_requirements'])

            # 学费    //article[@id='fees-and-funding']/ul[3]/li
            tuition_fee = response.xpath("//article[@id='fees-and-funding']/ul[3]/li//text()").extract()
            tuition_fee = ''.join(tuition_fee)
            item['tuition_fee'] = tuition_fee
            # print("item['tuition_fee'] = ", item['tuition_fee'])

            # 就业    //article[@id='careers']
            career = response.xpath("//article[@id='careers']//text()").extract()
            career = ''.join(career)
            item['career'] = career
            # print("item['career'] = ", item['career'])

            # item['type'] = "Taught"
            yield item
        except Exception as e:
            with open("./error/" + item['university'] + ".txt", 'a+', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)



